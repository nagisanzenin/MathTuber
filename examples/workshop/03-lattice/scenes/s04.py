from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        shape,grid,inside,boundary=lattice(self,POLY);self.add(shape,grid,inside,boundary,self.text('Move a corner. Count again.'))
        self.at('one grid step outward');new,_,ni,nb=lattice(self,NEW);self.play(FadeOut(inside),FadeOut(boundary),run_time=.3);self.play(Transform(shape,new),run_time=1);self.play(FadeIn(ni),FadeIn(nb),run_time=.5)
        self.at('eight interior points');self.note('● INSIDE: 8',-1.8,'primary')
        self.at('twelve boundary points');self.note('○ BOUNDARY: 12',-2.5,'secondary')
        self.at('Eight plus six');self.rule('8 + 12/2 − 1 = 13',-3.4)
        self.at('conditions matter');self.note('GRID VERTICES • SIMPLE • NO HOLES',-4.2,'muted')
        self.finish()
