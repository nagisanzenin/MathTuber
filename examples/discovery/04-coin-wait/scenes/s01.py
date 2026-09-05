from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        self.title('SAME ODDS. SAME WAIT?')
        a=pattern('HT').move_to(LEFT*1.65+UP);b=pattern('HH').move_to(RIGHT*1.65+UP);self.show(VGroup(a,b));self.show(label('My target          Your target',2.55,BLUE,28))
        self.at('probability one quarter');self.show(eq(r'P(HH)=P(HT)=\frac14',y=-.8,size=45))
        self.at('heads then tails takes four');self.show(label('HT: 4 flips on average',-2.4,GREEN))
        self.at('Two heads takes six');self.show(label('HH: 6 flips on average',-3.5,RED))
        self.finish()
