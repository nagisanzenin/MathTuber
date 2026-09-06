"""Mechanical recipe: animate the entire group changed by an updater."""
from manim import Scene, Dot, Text, Line, VGroup, UpdateFromAlphaFunc, UP, LEFT, RIGHT
import numpy as np

class AttachedMarker(Scene):
    def construct(self):
        start=LEFT*2;end=RIGHT*2
        track=Line(start,end)
        marker=Dot(start)
        label=Text('same object',font_size=28).next_to(marker,UP,buff=.25)
        moving=VGroup(marker,label)
        self.add(track,moving)
        def position(group,alpha):
            group[0].move_to((1-alpha)*start+alpha*end)
            group[1].next_to(group[0],UP,buff=.25)
        self.play(UpdateFromAlphaFunc(moving,position),run_time=1.8)
        assert np.allclose(marker.get_center(),end)
        assert abs(label.get_center()[0]-marker.get_center()[0])<1e-8
        self.wait(.6)
