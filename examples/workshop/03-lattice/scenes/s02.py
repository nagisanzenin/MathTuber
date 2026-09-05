from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        shape,grid,inside,boundary=lattice(self,[(0,0),(4,0),(4,3),(0,3)]);self.add(shape,grid,self.text('First, test a rectangle.'))
        self.at('four units across');self.show(self.text('4 × 3 = 12',3.55,'primary'))
        self.at('three columns of two');self.play(LaggedStart(*[GrowFromCenter(x) for x in inside],lag_ratio=.15),run_time=1.5);self.note('I = 6',-1.8,'primary')
        self.at('fourteen distinct dots');self.play(LaggedStart(*[Create(x) for x in boundary],lag_ratio=.06),run_time=1.5);self.note('B = 14',-2.5,'secondary')
        self.at('Six plus seven');self.rule('6 + 14/2 − 1 = 12',-3.4)
        self.at('any whole number width');self.show(self.text('I = (w−1)(h−1)    B = 2w+2h',-4.1,'muted','detail'))
        self.finish()
