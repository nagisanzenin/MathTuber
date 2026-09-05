from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        self.title('ONE BITE CHANGES THE GAME')
        g=chocolate();self.show(g)
        self.at('Choose this square');self.play(Indicate(g[7],color=GOLD),run_time=.7)
        self.at('The whole rectangle');region=bite(g,2,1);self.play(region.animate.set_fill(GOLD),run_time=.4);self.play(FadeOut(region,shift=UR*.25),run_time=.8)
        self.at('can have steps');self.note('A bite removes an upper-right region',-2.5,BLUE)
        self.at('Every turn removes chocolate');self.play(Indicate(g[4],color=GOLD),run_time=.6);self.play(FadeOut(g[4]),run_time=.5)
        self.at('There is no draw');self.note('Finite game • no chance • no draws',-3.7,GREEN)
        self.finish()
