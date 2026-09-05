from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        shape,grid,inside,boundary=lattice(self,POLY);self.add(shape,grid,self.text('Area, without measuring sides.'))
        self.at('Count the dots strictly inside');self.play(LaggedStart(*[GrowFromCenter(x) for x in inside],lag_ratio=.18),run_time=2);self.note('● INSIDE: 6',-1.8,'primary')
        self.at('dots on the boundary');self.play(LaggedStart(*[Create(x) for x in boundary],lag_ratio=.08),run_time=2);self.note('○ BOUNDARY: 12',-2.5,'secondary')
        self.at('not just the corners');self.play(Circumscribe(boundary[1],color=self.palette['accent']),run_time=1)
        self.at('Six plus half');self.rule('6 + 12/2 − 1 = 11',-3.4)
        self.at('Pick');self.show(self.text('PICK’S THEOREM',3.5,'muted','detail'))
        self.finish()
