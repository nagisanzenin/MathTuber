from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        self.title('WHY EIGHT SHUFFLES?')
        powers=VGroup(*[txt(str(2**k),27,BLUE).move_to([(-2.6+(k-1)%4*1.7),2.6-((k-1)//4)*1.15,0]) for k in range(1,9)]);self.play(LaggedStart(*[FadeIn(m) for m in powers],lag_ratio=.18),run_time=2)
        self.at('multiplied by two hundred fifty six');self.play(Circumscribe(powers[-1],color=GOLD),run_time=.8)
        self.at('five times fifty one');equ=eq(r'256=5\times51+1',y=-.25,size=51);self.show(equ)
        self.at('five full turns');laps=VGroup(*[Circle(radius=.23,color=BLUE).move_to([(i-2)*.7,-1.5,0]) for i in range(5)]);self.show(laps);self.play(LaggedStart(*[FadeOut(x,shift=UP*.2) for x in laps],lag_ratio=.15),run_time=1)
        self.at('starting position');self.show(eq(r'256p\equiv p\pmod {51}',y=-2.2,size=45,color=GREEN))
        self.at('Every card returns together');self.note('52 cards. One shared return.',-3.5)
        self.at('Perfect order');self.play(Indicate(equ,color=GREEN),run_time=1)
        self.finish()
