from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        a=band(self,1.5,center=UP*2.1,scale=.8);b=band(self,2.6,center=DOWN*.8,scale=.8);self.add(a,b,self.text('Which one holds more?'))
        self.at('exactly the same height');marks=VGroup(*[DoubleArrow(np.array([2.85,y-.96,0]),np.array([2.85,y+.96,0]),buff=0,color=self.palette['secondary'],stroke_width=3) for y in [2.1,-.8]]);self.show(marks);self.note('SAME HEIGHT',-3,'secondary')
        self.at('volumes are exactly equal');self.rule('SAME VOLUME',-3.8)
        self.at('one thin horizontal slice');self.play(Indicate(a[14],color=self.palette['accent']),Indicate(b[14],color=self.palette['accent']),run_time=1.5)
        self.finish()
