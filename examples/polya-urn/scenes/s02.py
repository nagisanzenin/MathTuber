from scenes._shared.design import *
class Shot2(Stage):
 sid="s02"
 def construct(self):
  self.title('AFTER FOUR DRAWS','Every split is equally likely.')
  groups=VGroup(*[VGroup(marbles(k,6-k,.42).arrange_in_grid(rows=2,cols=3,buff=.09),text(str(k),23,WHITE).shift(DOWN*.65)).move_to([(k-3)*1.25,2.7,0]) for k in range(1,6)]);self.add(groups,text("RED MARBLES",20,MUTED).move_to(UP*1.6))
  base=Line([-3.2,-1.5,0],[3.2,-1.5,0],color=MUTED);self.add(base)
  bars=VGroup(*[Rectangle(width=.7,height=2,fill_color=ORANGE,fill_opacity=.8,stroke_width=0).move_to([(k-3)*1.25,-.5,0]) for k in range(1,6)])
  self.at('Every one');self.play(LaggedStart(*[GrowFromEdge(b,DOWN) for b in bars],lag_ratio=.1),run_time=1)
  self.show(equation(r'P(1)=P(2)=\cdots=P(5)=\frac15'))
  self.at('This flat distribution');self.show(text('Exact probabilities · not a simulation',24,MUTED).move_to(DOWN*4.35))
  self.finish()
