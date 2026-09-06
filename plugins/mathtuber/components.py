"""Small optional helpers. The host agent owns the animation design."""
from manim import *
from mathtuber.process_clock import ProcessClock
TARGET_DURATION = 0.0
BG = "#10121B"
INK = "#F3F0E8"
GOLD = "#E9B96E"
BLUE = "#75B9CF"
CORAL = "#E68D82"

class NarratedScene(Scene):
    def setup(self):
        self.camera.background_color = BG
    @property
    def target_duration(self):
        return TARGET_DURATION
    def cue(self, fraction):
        """Hold until a normalized cue. Explicitly fails if preceding motion overruns."""
        target = TARGET_DURATION * fraction
        remaining = target - self.renderer.time
        if remaining < -.15:
            raise ValueError(f"Animation overran cue {fraction}: {self.renderer.time:.2f} > {target:.2f}")
        if remaining > 0:
            self.wait(remaining)
    def finish(self):
        self.cue(1.0)
    def process_clock(self, rate=1.0, initial=0.0):
        """Advance through play AND wait; pause/resume explicitly for inspection.

        Add this clock before the objects that read it. Keep its invisible driver
        in the scene while it is needed; clearing the scene also removes clocks.
        """
        clock = ProcessClock(rate, initial, time_source=lambda: self.renderer.time)
        driver = Mobject()
        driver.add_updater(lambda _, dt: clock.value)
        self.add(driver)
        return clock
    def heading(self, title, subtitle=None):
        label = Text(title, font_size=38, color=INK).to_edge(UP, buff=1.1)
        if label.width > 6.6:
            label.scale_to_fit_width(6.6)
        self.add(label)
        if subtitle:
            sub = Text(subtitle, font_size=23, color=GOLD).next_to(label, DOWN, buff=.25)
            if sub.width > 6.5:
                sub.scale_to_fit_width(6.5)
            self.add(sub)
        return label


PROFILE = None

class WorkshopScene(NarratedScene):
    """Profile-aware primitives, not a shot template. Coordinates use Manim units."""
    def setup(self):
        super().setup()
        if not PROFILE:
            raise ValueError("WorkshopScene requires a bound channel profile")
        self.profile = PROFILE
        self.palette = PROFILE["identity"]["colors"]
        self.camera.background_color = self.palette["background"]
        import manimpango
        typography = PROFILE["identity"]["type"]
        fonts = set(manimpango.list_fonts())
        self.profile_font = typography["font"] if typography["font"] in fonts else typography["fallback"]

    def lettering(self, text, role="label", color="ink", max_width=6.5):
        item = Text(text, font=self.profile_font,
                    font_size=self.profile["identity"]["type"]["roles"][role],
                    color=self.palette.get(color, color))
        if item.width > max_width:
            item.scale_to_fit_width(max_width)
        return item

    def tile(self, width=1, height=1, color="primary", label=None):
        face = RoundedRectangle(width=width, height=height, corner_radius=min(.12,width/8,height/8),
                                fill_color=self.palette.get(color,color), fill_opacity=1,
                                stroke_color=self.palette["ink"], stroke_width=1.6)
        shadow = face.copy().set_fill(self.palette["ink"],opacity=.13).set_stroke(opacity=0).shift(DR*.07)
        group = VGroup(shadow,face)
        if label is not None:
            group.add(self.lettering(str(label),color="background",max_width=width*.8).move_to(face))
        return group

    def replace_label(self, previous, replacement, run_time=.4):
        """Fade between phrases without distorting glyphs. Returns the new label."""
        if previous is not None:
            self.play(FadeOut(previous), run_time=run_time / 2)
        self.play(FadeIn(replacement), run_time=run_time / 2 if previous is not None else run_time)
        return replacement

    def focus_outline(self, target, color="secondary", buff=.12, run_time=1):
        """Draw attention without changing the target's geometry, fill or glyphs."""
        self.play(Circumscribe(target, color=self.palette.get(color,color),
                               buff=buff, stroke_width=3), run_time=run_time)

    def stage_focus(self, subject, center, width=6.4, height=7.2, run_time=1.5):
        """Move/fit an existing subject while captions and camera stay fixed.

        Include context necessary to understand the subject. Pause the process
        and remove its geometry updaters before calling; rebuild their coordinate
        mapping before resuming. This helper never silently disables simulation.
        """
        from mathtuber.framing import fit_scale
        if any(item.updaters for item in subject.get_family()):
            raise ValueError("Pause and remove subject updaters before focal staging")
        scale = fit_scale(float(subject.width), float(subject.height), width, height)
        self.play(subject.animate.scale(scale).move_to(center), run_time=run_time)
        return subject

    def trace_curve(self, point_at, parameter, start=0.0, end=1.0,
                    samples=601, color="primary", stroke_width=4):
        """Return an updating cached polyline; add it to the scene explicitly.

        `parameter` is a callable. Keep its range inside start/end. Sampling
        error depends on the curve: inspect live-point alignment at the intended
        output size. The cache uses parameter space, not constant arc speed.
        """
        from mathtuber.curve_trace import CurveTrace
        trace = CurveTrace(point_at, start, end, samples)
        item = VMobject(stroke_color=self.palette.get(color, color),
                        stroke_width=stroke_width)
        def update(line):
            line.set_points_as_corners(trace.through(float(parameter())))
        update(item)
        item.add_updater(update)
        return item

    def bead(self, radius=.25, color="primary", layers=18):
        """Painted depth cue for tangible round objects, with profile colors.

        Keep mathematical marks and magnitude encodings flat. This is stylized
        shading, not a physical irradiance model. Moving it preserves its light
        direction; rotate physical markers separately if needed.
        """
        from mathtuber.materials import painted_bead
        return painted_bead(radius, self.palette.get(color,color),
                            self.palette["ink"], self.palette["background"], layers)
