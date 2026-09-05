from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        g=self.board(4,1.15);self.add(g);self.add(self.text('Every domino makes a pair.'))
        d=RoundedRectangle(width=2.24,height=1.08,corner_radius=.12,stroke_color=self.palette['secondary'],stroke_width=6,fill_opacity=0).move_to((g[5].get_center()+g[6].get_center())/2);self.show(d)
        self.at('one dark square and one light square');self.note('ONE DARK + ONE LIGHT',-2.2)
        self.at('Turn it vertically');self.play(d.animate.rotate(PI/2).move_to((g[5].get_center()+g[9].get_center())/2),run_time=1.4)
        self.at('Every legal placement');self.play(d.animate.move_to((g[6].get_center()+g[10].get_center())/2),run_time=1);self.play(d.animate.rotate(PI/2).move_to((g[10].get_center()+g[11].get_center())/2),run_time=1)
        self.at('thirty one dark squares');self.rule('31 DARK ↔ 31 LIGHT')
        self.at('cannot negotiate');self.play(Circumscribe(d,color=self.palette['accent']),run_time=1);self.finish()
