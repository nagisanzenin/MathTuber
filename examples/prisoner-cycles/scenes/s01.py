from scenes._shared.design import *
class Shot1(Stage):
 sid="s01"
 def construct(self):
  self.title('100 PRISONERS · 100 BOXES','Fifty tries. Everyone wins?')
  b=boxes();self.play(LaggedStart(*[FadeIn(x) for x in b],lag_ratio=.005),run_time=1.4)
  self.at('Each prisoner');self.show(chip('OPEN AT MOST 50 BOXES',GOLD))
  self.at('Everyone must succeed');self.play(Indicate(b,color=ORANGE),run_time=.7)
  self.at('Independent random');self.show(equation(r'P(\text{all win})=2^{-100}',y=-4.4,color=ORANGE,size=37))
  self.finish()
