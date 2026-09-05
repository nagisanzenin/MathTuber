from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        g=self.board();self.add(g);self.add(self.text('Change the cut. Change the answer.'))
        self.at('two neighboring corners');self.play(FadeOut(g[56],shift=UL*.4),FadeOut(g[63],shift=UR*.4),run_time=1)
        self.at('one dark and one light');self.note('31 DARK + 31 LIGHT',-2.7)
        self.at('The six squares left');pieces=VGroup(*[RoundedRectangle(width=1.29,height=.62,corner_radius=.1,fill_color=self.palette['accent'],fill_opacity=.8,stroke_width=2,stroke_color=self.palette['ink']).move_to((g[j].get_center()+g[j+1].get_center())/2) for j in (57,59,61)]);self.play(LaggedStart(*[FadeIn(x) for x in pieces],lag_ratio=.25),run_time=1.5)
        self.at('every complete row');more=VGroup(*[RoundedRectangle(width=1.29,height=.62,corner_radius=.1,fill_color=self.palette['accent'],fill_opacity=.8,stroke_width=2,stroke_color=self.palette['ink']).move_to((g[y*8+x].get_center()+g[y*8+x+1].get_center())/2) for y in range(7) for x in range(0,8,2)]);self.play(LaggedStart(*[FadeIn(x) for x in more],lag_ratio=.04),run_time=2.4)
        self.at('unequal counts immediately prove');self.rule('An invariant can end the search.')
        self.finish()
