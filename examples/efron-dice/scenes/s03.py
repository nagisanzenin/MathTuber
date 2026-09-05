from scenes._shared.design import *
class Shot3(Stage):
 sid="s03"
 def construct(self):
  self.title('FOLLOW THE ADVANTAGE','Winning goes in a circle.')
  positions=[[-1.65,2,0],[1.65,2,0],[1.65,-.5,0],[-1.65,-.5,0]]
  b=VGroup(*[die(i,width=2.4).scale(.75).move_to(positions[i]) for i in range(4)]);self.add(b)
  pairs=[(0,1),(1,2),(2,3),(3,0)];arrows=VGroup(*[Arrow(b[a].get_center(),b[c].get_center(),buff=1,color=COLORS[a],stroke_width=4) for a,c in pairs])
  self.play(Create(arrows[0]),run_time=.5)
  self.at('Orange beats purple');self.play(Create(arrows[1]),run_time=.5)
  self.at('Purple beats green');self.play(Create(arrows[2]),run_time=.5)
  self.at('Finally');self.play(Create(arrows[3]),run_time=.5)
  self.at('Count all thirty six');self.play(Write(equation(r'\frac{24}{36}=\frac23\quad\text{on every arrow}')),run_time=1)
  self.finish()
