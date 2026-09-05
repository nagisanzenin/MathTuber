from components import *
import json, math
from pathlib import Path
import numpy as np
class Stage(WorkshopScene):
    def setup(self):
        super().setup()
        self.times=json.loads((Path(__file__).resolve().parents[2]/'assets/timing.json').read_text())[self.sid]
        brand=self.lettering('I VISUALIZE THINGS',role='detail',color='muted').scale(.55).move_to(UP*6.1)
        self.add(brand)
    def at(self,phrase):
        target=self.times[phrase];remaining=target-self.renderer.time
        if remaining < -.25: raise ValueError(f'{phrase}: overrun {self.renderer.time} > {target}')
        if remaining>0:self.wait(remaining)
    def show(self,*items): self.play(*[FadeIn(x,shift=UP*.08) for x in items],run_time=.5)
    def text(self,text,y=4.7,color='ink',role='claim'):
        return self.lettering(text,role=role,color=color).move_to(UP*y)
    def note(self,text,y=-2.9,color='ink'):
        t=self.text(text,y,color,'label');self.show(t);return t
    def rule(self,text,y=-3.4):
        t=self.text(text,y,'primary','claim');self.show(t);return t
    def board(self,n=8,size=.66):
        g=VGroup()
        for y in range(n):
            for x in range(n):
                c='primary' if (x+y)%2==0 else 'surface'
                t=Square(side_length=size-.025,fill_color=self.palette[c],fill_opacity=1,stroke_color=self.palette["ink"],stroke_width=.8,stroke_opacity=.35)
                t.move_to([(x-(n-1)/2)*size,(y-(n-1)/2)*size+.7,0]);g.add(t)
        return g
    def coin(self,r=1,color='accent'):
        c=Circle(radius=r,fill_color=self.palette[color],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=2)
        inner=Circle(radius=r*.86,stroke_color=self.palette['ink'],stroke_width=1,stroke_opacity=.25)
        arrow=Arrow(DOWN*r*.48,UP*r*.55,buff=0,color=self.palette['ink'],stroke_width=5,max_tip_length_to_length_ratio=.28)
        return VGroup(c,inner,arrow)
    def edge(self,a,b,kind='primary'):
        if kind=='secondary':return DashedLine(a,b,color=self.palette[kind],stroke_width=5,dash_length=.12)
        return Line(a,b,color=self.palette[kind],stroke_width=5)
    def person(self,name,pos):
        c=Circle(radius=.27,fill_color=self.palette['background'],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=2)
        t=self.lettering(name,role='detail').scale(.8);return VGroup(c,t).move_to(pos).set_z_index(5)
