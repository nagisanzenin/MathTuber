from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        self.title('WHAT DOES FAILURE LEAVE?')
        ht=pattern('HT').move_to(LEFT*1.65+UP*2.5);hh=pattern('HH').move_to(RIGHT*1.65+UP*2.5);self.show(VGroup(ht,hh))
        left=coin('H').move_to(LEFT*1.65);right=coin('H').move_to(RIGHT*1.65);self.show(VGroup(left,right))
        self.at('a tail finishes');tail=coin('T').move_to(LEFT*.45);self.show(tail);self.play(Indicate(ht,color=GREEN),run_time=.6);self.play(FadeOut(tail),run_time=.4)
        self.at('Another head does not finish');fresh=coin('H').move_to(LEFT*.45);self.show(fresh);self.play(FadeOut(left),fresh.animate.move_to(LEFT*1.65),run_time=.7)
        self.at('keeps us ready');self.show(label('Still ready',-1.3,GREEN).shift(LEFT*1.6))
        self.at('A tail wipes out');bad=coin('T').move_to(RIGHT*2.8);self.show(bad);self.play(FadeOut(right),FadeOut(bad),run_time=.7);self.show(txt('RESET',31,RED).move_to([1.65,-1.3,0]))
        self.at('preserve a useful beginning');self.note('Retain progress       Lose progress',-3.4,GOLD)
        self.finish()
