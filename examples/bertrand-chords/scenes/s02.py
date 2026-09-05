from scenes._shared.design import *
class Shot2(Stage):
 sid="s02"
 def construct(self):
  self.title('METHOD 1 · UNIFORM ANGLE','Choose the endpoints.')
  c,r,circ,tri=circle_diagram();self.add(circ,tri);a=c+UP*r;t=ValueTracker(0)
  chord=always_redraw(lambda:Line(a,c+r*np.array([np.cos(t.get_value()),np.sin(t.get_value()),0]),color=GOLD,stroke_width=4));self.add(chord,Dot(a,color=WHITE))
  self.play(t.animate.set_value(TAU),run_time=4,rate_func=linear)
  self.at('The chord is long enough');arc=Arc(radius=r,start_angle=7*PI/6,angle=2*PI/3,color=GOLD,stroke_width=10).shift(c);self.play(Create(arc),t.animate.set_value(3*PI/2),run_time=.8)
  self.at('That arc occupies');self.play(Write(equation(r'\frac{120^\circ}{360^\circ}=\frac13')),run_time=1)
  self.finish()
