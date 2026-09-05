from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        g=self.board();self.add(g);self.add(self.text('31 dominoes. One impossible board.'))
        self.at('remove two opposite corners');self.play(g[0].animate.set_fill(self.palette['secondary']),g[63].animate.set_fill(self.palette['secondary']),run_time=.5);self.play(FadeOut(g[0],shift=DL*.5),FadeOut(g[63],shift=UR*.5),run_time=.8)
        self.at('Every domino must cover');d=self.tile(1.29,.62,'accent').move_to((g[1].get_center()+g[2].get_center())/2);self.show(d)
        self.at('No overlaps');self.play(d.animate.move_to((g[9].get_center()+g[10].get_center())/2),run_time=1);self.play(d.animate.rotate(PI/2).move_to((g[18].get_center()+g[26].get_center())/2),run_time=1)
        self.at('all night rearranging');self.play(d.animate.move_to((g[19].get_center()+g[27].get_center())/2),run_time=1);self.play(d.animate.rotate(-PI/2).move_to((g[35].get_center()+g[36].get_center())/2),run_time=1)
        self.at('reject every arrangement');self.rule('62 squares = 31 × 2')
        self.at('a single domino');self.play(Indicate(d,color=self.palette['secondary']),run_time=1);self.finish()
