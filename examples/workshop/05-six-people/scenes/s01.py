from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        pos=[np.array([2.3*np.cos(PI/2+i*TAU/6),.5+2.3*np.sin(PI/2+i*TAU/6),0]) for i in range(6)];people=VGroup(*[self.person(chr(65+i),p) for i,p in enumerate(pos)]);self.add(people,self.text('Six people. An unavoidable triangle.'))
        self.at('either they know');edges=VGroup(*[self.edge(pos[i],pos[j],'primary' if (i+j)%3 else 'secondary') for i in range(6) for j in range(i+1,6)]);self.play(LaggedStart(*[Create(x) for x in edges],lag_ratio=.06),run_time=2)
        self.at('three people must all know');self.note('3 MUTUAL ACQUAINTANCES',-2.8,'primary')
        self.at('three must all be strangers');self.note('OR 3 MUTUAL STRANGERS',-3.5,'secondary')
        self.at('solid teal line');self.play(edges.animate.set_opacity(.22),run_time=.5);leg=VGroup(self.edge(LEFT*2+DOWN*4.3,LEFT*.7+DOWN*4.3),self.edge(RIGHT*.7+DOWN*4.3,RIGHT*2+DOWN*4.3,'secondary'));self.show(leg)
        self.at('triangle with three matching');triangle=VGroup(*[self.edge(pos[i],pos[j]) for i,j in [(0,1),(1,4),(0,4)]]);self.play(Create(triangle),run_time=1.5);self.finish()
