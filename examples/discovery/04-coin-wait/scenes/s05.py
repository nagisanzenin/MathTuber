from scenes._shared.design import *

class Shot5(Stage):
    sid="s05"
    def construct(self):
        self.title('AVERAGE ≠ PROMISE')
        a=pattern('HH').move_to(UP*1.7);self.show(a);self.show(label('Can finish in only 2 flips',.25,GOLD))
        self.at('Now predict two tails');self.play(FadeOut(a),run_time=.4);a=pattern('TT').move_to(LEFT*1.65+UP*1.7);b=pattern('TH').move_to(RIGHT*1.65+UP*1.7);self.show(VGroup(a,b))
        self.at('Two tails still averages six');self.show(txt('6',62,RED).move_to([-1.65,-1,0]))
        self.at('tails then heads averages four');self.show(txt('4',62,GREEN).move_to([1.65,-1,0]))
        self.at('track what a failure leaves behind');self.note('Waiting remembers the last flip.',-3.4,BLUE)
        self.finish()
