from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        c=self.coin(1.65).move_to(UP*1.2);ground=Line(LEFT*2.7+DOWN*.45,RIGHT*2.7+DOWN*.45,color=self.palette['ink']);self.add(c,ground,self.text('No slipping means cancellation.'))
        contact=Dot(DOWN*.45,color=self.palette['secondary'],radius=.12);self.show(contact)
        self.at('The center moves forward');a=Arrow(UP*1.2,RIGHT*2.2+UP*1.2,color=self.palette['primary'],buff=0);self.show(a);self.note('CENTER MOTION →',-1.5,'primary')
        self.at('spinning moves the touching point backward');b=Arrow(DOWN*.45,LEFT*2.2+DOWN*.45,color=self.palette['secondary'],buff=0);self.show(b);self.note('← MOTION FROM SPIN',-2.2,'secondary')
        self.at('Those motions cancel');self.play(Indicate(contact,color=self.palette['accent']),run_time=1);self.note('CONTACT SPEED = 0',-3)
        self.at('speed equals the spin rate');self.show(self.text('v = rω',3.5,'primary'))
        self.at('gives the number of turns');self.rule('TURNS = DISTANCE ÷ 2πr',-3.8)
        self.finish()
