from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        self.title('SUPPOSE SECOND CAN WIN')
        g=chocolate();self.show(g)
        self.at('just the top right square');self.play(g[-1].animate.set_fill(BLUE),run_time=.35);self.play(FadeOut(g[-1]),run_time=.65)
        self.at('a winning reply');b=txt('B',35,GOLD).move_to(g[7]);self.show(b)
        self.at('Your bite removes B');region=bite(g,2,1);self.play(*[t.animate.set_fill(GOLD).set_opacity(.55) for t in region if t is not g[-1]],run_time=.7)
        self.at('the corner I already ate');outline=SurroundingRectangle(g[-1],color=BLUE,buff=.02);self.show(outline);self.play(Indicate(outline,color=BLUE),run_time=.7)
        self.at('Remember the shape');self.play(FadeOut(region),FadeOut(b),FadeOut(outline),run_time=.8);self.note('After: corner, then B',-2.7,GOLD)
        self.finish()
