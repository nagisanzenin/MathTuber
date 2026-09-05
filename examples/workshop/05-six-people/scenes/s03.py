from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        pos=[np.array([0,3,0]),np.array([-2,0,0]),np.array([0,-1.1,0]),np.array([2,0,0])];people=VGroup(*[self.person(chr(65+i),p) for i,p in enumerate(pos)]);spokes=VGroup(*[self.edge(pos[0],pos[i]) for i in range(1,4)]);self.add(people,spokes,self.text('The other case gives a triangle too.'))
        self.at('none of those three pairs');other=VGroup(*[self.edge(pos[i],pos[j],'secondary') for i,j in [(1,2),(2,3),(1,3)]]);self.play(LaggedStart(*[Create(x) for x in other],lag_ratio=.3),run_time=2)
        self.at('three mutual strangers');self.play(spokes.animate.set_opacity(.2),run_time=.5);caption=self.note('B, C, D: ALL STRANGERS',-2.3,'secondary')
        self.at('swap the roles');replacement=VGroup(*[self.edge(pos[0],pos[i],'secondary') for i in range(1,4)]);new=VGroup(*[self.edge(pos[i],pos[j]) for i,j in [(1,2),(2,3),(1,3)]]);self.play(FadeOut(spokes),FadeOut(other),FadeIn(replacement),FadeIn(new),Transform(caption,self.text("B, C, D: ALL ACQUAINTANCES",-2.3,"primary","label")),run_time=1.5)
        self.at('Every possible room');self.rule('ONE CASE OR THE OTHER.',-3.3)
        self.finish()
