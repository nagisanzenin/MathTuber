from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        pos=[np.array([2.25*np.cos(PI/2+i*TAU/5),.7+2.25*np.sin(PI/2+i*TAU/5),0]) for i in range(5)];people=VGroup(*[self.person(str(i+1),p) for i,p in enumerate(pos)]);self.add(people,self.text('Five people can escape.'))
        self.at('neighboring pairs');pent=VGroup(*[self.edge(pos[i],pos[(i+1)%5]) for i in range(5)]);self.play(LaggedStart(*[Create(x) for x in pent],lag_ratio=.12),run_time=1.5)
        self.at('all diagonal pairs');star=VGroup(*[self.edge(pos[i],pos[(i+2)%5],'secondary') for i in range(5)]);self.play(LaggedStart(*[Create(x) for x in star],lag_ratio=.12),run_time=1.5)
        self.at('solid edges form');self.play(star.animate.set_opacity(.16),run_time=.5)
        self.at('dashed diagonals form');self.play(star.animate.set_opacity(1),pent.animate.set_opacity(.15),run_time=.5)
        self.at('Crossings are not extra people');self.play(pent.animate.set_opacity(1),run_time=.5);self.note('ONLY THE FIVE DOTS ARE PEOPLE.',-2.6,'muted')
        self.at('while six cannot');self.rule('FIVE CAN ESCAPE. SIX CANNOT.',-3.6)
        self.finish()
