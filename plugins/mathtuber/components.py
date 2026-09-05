"""Small optional helpers. The host agent owns the animation design."""
from manim import *
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
