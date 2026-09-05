from scenes._shared.design import *

class Shot5(Stage):
    sid="s05"
    def construct(self):
        self.title('TRY A DIFFERENT SHOP')
        self.show(label('Boxes of 3 and 5',2.7,BLUE,38))
        self.at('Eight, nine, and ten');rows=VGroup(*[txt(s,35,GREEN) for s in ['8 = 5 + 3','9 = 3 + 3 + 3','10 = 5 + 5']]).arrange(DOWN,buff=.5).move_to(UP*.65);self.show(rows)
        self.at('seven is the last');answer=self.note('Last impossible: 7',-1.6,GOLD)
        self.at('boxes of four and six');self.play(FadeOut(rows),FadeOut(answer),run_time=.6);self.show(label('Boxes of 4 and 6',.9,RED,39))
        self.at('every odd order');self.show(label('1, 3, 5, 7, 9, … impossible',-.6,RED,32))
        self.at('without leaving a gap');self.note('Prove the continuation, not a trend.',-3.6,GREEN)
        self.finish()
