from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        pos=[np.array([0,3,0]),np.array([-2,0,0]),np.array([0,-.8,0]),np.array([2,0,0]),np.array([-2.5,2,0]),np.array([2.5,2,0])];people=VGroup(*[self.person(chr(65+i),p) for i,p in enumerate(pos)]);self.add(people,self.text('Choose one person: A.'))
        self.at('five connections');edges=VGroup(*[self.edge(pos[0],pos[i],'primary' if i<4 else 'secondary') for i in range(1,6)]);self.play(LaggedStart(*[Create(x) for x in edges],lag_ratio=.15),run_time=1.5)
        self.at('At least three');self.play(*[e.animate.set_stroke(width=8) for e in edges[:3]],run_time=.8);self.note('5 CONNECTIONS → 3 OF ONE TYPE',-2.3)
        self.at('forget everyone else');self.play(FadeOut(people[4]),FadeOut(people[5]),FadeOut(edges[3]),FadeOut(edges[4]),run_time=.7)
        self.at('If B and C know');bc=self.edge(pos[1],pos[2]);self.play(Create(bc),run_time=1);self.play(edges[2].animate.set_opacity(.2),people[3].animate.set_opacity(.25),run_time=.5)
        self.at('triangle of acquaintances');self.rule('A — B — C — A',-3.3)
        self.finish()
