from scenes._shared.design import *
class Shot4(Stage):
 sid="s04"
 def construct(self):
  self.title('COUNT THE BAD LOOPS','From almost zero to 31%.')
  formula=equation(r'1-\sum_{k=51}^{100}\frac1k',y=1.9,size=64);self.play(Write(formula),run_time=1.2)
  self.at('Two such long cycles');self.show(chip('TWO LONG LOOPS CANNOT FIT',WHITE,y=-1.4,size=27))
  self.at('The result');big=text('31.18%',76,GREEN,True).move_to(DOWN*.1);self.show(big)
  self.at('Still risky');self.show(text('Uniform random shuffle · cycle strategy',23,MUTED).move_to(DOWN*2.4))
  self.at('The rescue');self.show(chip('COORDINATE THE FAILURES.',GOLD))
  self.finish()
