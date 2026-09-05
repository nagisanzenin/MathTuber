from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        g=self.board();self.add(g);self.add(self.text('Count what cannot change.'))
        self.at('same color');self.play(Indicate(g[0],color=self.palette['secondary']),Indicate(g[63],color=self.palette['secondary']),run_time=1)
        self.at('removed two dark');self.play(FadeOut(g[0]),FadeOut(g[63]),run_time=.7)
        self.at('thirty dark squares');dark=[g[i] for i in range(64) if i not in (0,63) and ((i%8)+(i//8))%2==0];light=[g[i] for i in range(64) if ((i%8)+(i//8))%2==1]
        self.play(*[t.animate.scale(.48).move_to([-2.55+(j%5)*.43,2.5-(j//5)*.6,0]) for j,t in enumerate(dark)],*[t.animate.scale(.48).move_to([.6+(j%5)*.43,2.5-(j//5)*.6,0]) for j,t in enumerate(light)],run_time=2)
        self.show(self.text('30 dark',3.55,'primary','label').shift(LEFT*1.65),self.text('32 light',3.55,'ink','label').shift(RIGHT*1.65))
        self.at('two light squares have no partner');self.play(*[Circumscribe(t,color=self.palette['secondary']) for t in light[-2:]],run_time=1.4);self.rule('2 LIGHT SQUARES LEFT OVER')
        self.at('every arrangement fails');self.play(*[t.animate.set_fill(self.palette['secondary']) for t in light[-2:]],run_time=.8)
        self.finish()
