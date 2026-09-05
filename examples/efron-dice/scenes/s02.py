from scenes._shared.design import *
class Shot2(Stage):
 sid="s02"
 def construct(self):
  self.title('COUNT EVERY OUTCOME','Blue beats orange.')
  a=die(0).scale(.8).move_to([-1.7,3,0]);b=die(1).scale(.8).move_to([1.7,3,0]);self.add(a,b)
  grid=VGroup()
  for i,x in enumerate(DICE[0]):
   for j,y in enumerate(DICE[1]):
    square=Square(side_length=.55,fill_color=BLUE if x>y else ORANGE,fill_opacity=.85,stroke_color=DARK,stroke_width=2).move_to([(j-2.5)*.59,(2.5-i)*.59-.15,0]);grid.add(square)
  self.at('So blue wins');self.play(LaggedStart(*[FadeIn(m,scale=.7) for m in grid],lag_ratio=.015),run_time=1.3)
  self.at('In this grid');self.show(text('6 faces × 6 faces = 36 pairs',26,MUTED).move_to(DOWN*2.4))
  self.at('Twenty four');self.play(Write(equation(r'P(A>B)=\frac{24}{36}=\frac23')),run_time=1)
  self.at('The advantage is exact');self.play(Indicate(grid[:24],color=BLUE),run_time=.9)
  self.finish()
