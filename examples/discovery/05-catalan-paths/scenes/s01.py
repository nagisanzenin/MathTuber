from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        self.title('HOW MANY SAFE ROUTES?')
        g=grid();self.show(g);robot=Dot([-2,-1.5,0],radius=.14,color=GOLD);home=Star(n=5,outer_radius=.18,color=GOLD,fill_opacity=1).move_to([1.75,2.25,0]);self.show(VGroup(robot,home))
        self.at('never go above');forbidden=Polygon([-2,-1.5,0],[-2,2.25,0],[1.75,2.25,0],fill_color=RED,fill_opacity=.13,stroke_width=0);self.show(forbidden)
        self.at('How many safe routes');p=path('RRURUU');self.play(Create(p),MoveAlongPath(robot,p),run_time=1.6)
        self.at('There are twenty routes');self.show(label('20 routes before adding the fence',-2.9,BLUE,30))
        self.at('A mirror will do');self.note('Count the bad ones with a mirror.',-4,GOLD)
        self.finish()
