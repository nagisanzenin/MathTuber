from scenes._shared.design import *
class Shot1(Stage):
 sid="s01"
 def construct(self):
  self.title('BERTRAND’S PARADOX','What does “random” mean?')
  c,r,circ,tri=circle_diagram();self.add(circ);self.play(Create(tri),run_time=.9)
  chord=Line(c+LEFT*r,c+RIGHT*r,color=GOLD,stroke_width=5);self.show(chord)
  self.at('One third');answers=VGroup(*[equation(s,color=col,size=53).move_to([x,-2.7,0]) for s,col,x in [(r'\frac13',BLUE,-2),(r'\frac12',GOLD,0),(r'\frac14',ORANGE,2)]]);self.show(answers)
  self.at('All three');self.show(chip('THREE EXPERIMENTS. THREE ANSWERS.',WHITE,y=-4,size=25))
  self.finish()
