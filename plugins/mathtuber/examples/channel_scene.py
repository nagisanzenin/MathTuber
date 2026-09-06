"""Portable starting point. Render through the engine with a bound profile."""
from manim import VGroup, RIGHT, UP
from components import WorkshopScene

class ChannelScene(WorkshopScene):
    def construct(self):
        title = self.lettering("Two views, one total", role="claim").move_to(UP * 4.8)
        pieces = VGroup(*(self.tile(label=str(n)) for n in (1, 2, 3))).arrange(RIGHT, buff=.3)
        conclusion = self.lettering("1 + 2 + 3 = 6").move_to(UP * -2)
        self.assert_safe(title, pieces, conclusion)
        self.add(title, pieces, conclusion)
        self.finish()
