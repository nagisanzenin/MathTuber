"""Mechanical recipe: dim an outline without filling it. Not a film template."""
from manim import Scene, RoundedRectangle, Text, UP, DOWN, VGroup

class OutlineRestore(Scene):
    def construct(self):
        outline=RoundedRectangle(width=3,height=2,corner_radius=.2,fill_opacity=0,stroke_width=4)
        label=Text('stroke opacity only',font_size=28).shift(UP*2)
        self.add(outline,label)
        self.wait(.3)
        self.play(outline.animate.set_stroke(opacity=.15),run_time=.6)
        assert outline.get_fill_opacity()==0
        self.wait(.3)
        self.play(outline.animate.set_stroke(opacity=1),run_time=.6)
        assert outline.get_fill_opacity()==0
        self.wait(.6)
