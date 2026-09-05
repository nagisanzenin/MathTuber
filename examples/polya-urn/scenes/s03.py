from scenes._shared.design import *
class Shot3(Stage):
 sid="s03"
 def construct(self):
  self.title('COUNT HISTORIES, NOT JUST COLORS','Many unlikely paths add up.')
  self.add(sequence('RRRR',y=3.1));first=equation(r'\frac12\cdot\frac23\cdot\frac34\cdot\frac45=\frac15',y=1.95,size=44);self.play(Write(first),run_time=1.5)
  self.at('Red, red, blue, blue');self.show(sequence('RRBB',y=.7));self.play(Write(equation(r'\frac12\cdot\frac23\cdot\frac14\cdot\frac25=\frac1{30}',y=-.4,size=43)),run_time=1.2)
  self.at('But there are six');patterns=sorted(set(itertools.permutations('RRBB')));rows=VGroup(*[sequence(s).scale(.52) for s in patterns]).arrange_in_grid(rows=2,cols=3,buff=(.65,.35)).move_to(DOWN*2.0);self.show(rows)
  self.at('Six times');self.play(Write(equation(r'6\times\frac1{30}=\frac15',y=-3.7)),run_time=.8)
  self.finish()
