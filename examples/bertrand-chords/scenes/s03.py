from scenes._shared.design import *
class Shot3(Stage):
 sid="s03"
 def construct(self):
  self.title('METHOD 2 · UNIFORM RADIUS','Choose a radial distance.')
  c,r,circ,tri=circle_diagram();self.add(circ,tri);d=ValueTracker(r*.85)
  rad=Line(c,c+RIGHT*r,color=MUTED,stroke_width=3);self.add(rad)
  chord=always_redraw(lambda:Line(c+[d.get_value(),-np.sqrt(max(0,r*r-d.get_value()**2)),0],c+[d.get_value(),np.sqrt(max(0,r*r-d.get_value()**2)),0],color=GOLD if d.get_value()<r/2 else ORANGE,stroke_width=5));dot=always_redraw(lambda:Dot(c+RIGHT*d.get_value(),color=WHITE,radius=.1));self.add(chord,dot)
  self.at('The closer');self.play(d.animate.set_value(.12*r),run_time=2.3)
  self.at('It beats');self.play(Create(Line(c,c+RIGHT*r/2,color=GOLD,stroke_width=9)),run_time=.6)
  self.at('Half the allowed');self.play(Write(equation(r'P=\frac{R/2}{R}=\frac12')),run_time=1)
  self.finish()
