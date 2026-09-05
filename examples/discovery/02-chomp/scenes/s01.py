from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        self.title('POISONED CHOCOLATE')
        g=chocolate();self.show(g);poison=label('X = poison',-2.5,RED);self.show(poison)
        self.at('Two players take turns');self.play(Indicate(g[8],color=GOLD),run_time=.6)
        self.at('eating it and every square');region=bite(g,3,1);self.play(region.animate.set_fill(GOLD),run_time=.4);self.play(FadeOut(region,shift=UP*.3),run_time=.7)
        self.at('Whoever eats the poison');self.play(Indicate(g[0],color=RED),run_time=.9)
        self.at('make a guess');q=self.note('Can FIRST always force a win?',-3.6)
        self.at('The answer is yes');self.play(Transform(q,label('YES — but where is the move?',-3.6,GREEN)),run_time=.7)
        self.finish()
