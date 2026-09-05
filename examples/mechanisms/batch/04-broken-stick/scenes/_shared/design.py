from components import *
from pathlib import Path
import json, math
import numpy as np
class Stage(WorkshopScene):
    def setup(self):
        super().setup()
        self.times=json.loads((Path(__file__).resolve().parents[2]/'assets/timing.json').read_text())['s01']
        self.caption=None
    def at(self,phrase):
        remaining=self.times[phrase]-self.renderer.time
        if remaining < -.25:raise ValueError(f'Cue overrun: {phrase}: {remaining}')
        if remaining>0:self.wait(remaining)
    def label(self,text,pos,color='ink',role='label'):
        return self.lettering(text,role,color).move_to(pos)
    def say(self,text,y=4.9,color='ink'):
        new=self.label(text,UP*y,color,'claim')
        if self.caption is None:self.play(FadeIn(new),run_time=.4)
        else:self.play(ReplacementTransform(self.caption,new),run_time=.4)
        self.caption=new
    def line(self,a,b,color='primary',width=5):
        return Line(a,b,color=self.palette[color],stroke_width=width)
    def poly(self,*pts,color='primary',opacity=.35):
        return Polygon(*pts,fill_color=self.palette[color],fill_opacity=opacity,stroke_color=self.palette['ink'],stroke_width=2)
    def coin(self,r,color='accent'):
        return VGroup(Circle(radius=r,fill_color=self.palette[color],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=3),Arrow(DOWN*r*.45,UP*r*.6,buff=0,stroke_width=5,color=self.palette['ink']))
