from scenes._shared.design import *

class Shot5(Stage):
    sid="s05"
    def construct(self):
        self.title('EXISTENCE ≠ A RECIPE')
        g=chocolate(4,4);self.show(g)
        self.at('On a square bar');self.play(Circumscribe(g,color=BLUE),run_time=.7)
        self.at('remove everything above');self.play(FadeOut(bite(g,1,1)),run_time=1)
        self.at('two equal arms');diag=DashedLine(g[0].get_center()+DL*.35,g[-1].get_center()+UR*.35,color=BLUE);self.show(diag)
        self.at('Mirror every safe move');self.play(FadeOut(VGroup(g[2],g[3])),run_time=.7);self.play(FadeOut(VGroup(g[8],g[12])),run_time=.7)
        self.at('eventually faces only poison');self.play(FadeOut(g[1]),run_time=.5);self.play(FadeOut(g[4]),run_time=.5);self.play(Indicate(g[0],color=RED),run_time=.7)
        self.at('different kinds of knowledge');self.note('“There is” and “Here is how” differ.',-3.4,GREEN)
        self.finish()
