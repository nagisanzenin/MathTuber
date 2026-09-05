from scenes._shared.design import *
class Shot4(Stage):
 sid="s04"
 def construct(self):
  self.title('METHOD 3 · UNIFORM AREA','Choose a point in the disk.')
  c,r,circ,tri=circle_diagram();self.add(circ)
  rng=np.random.default_rng(72);dots=VGroup()
  for _ in range(100):
   a=rng.uniform(0,TAU);rho=r*np.sqrt(rng.uniform());dots.add(Dot(c+rho*np.array([np.cos(a),np.sin(a),0]),radius=.035,color=GOLD if rho<r/2 else MUTED))
  self.play(LaggedStart(*[FadeIn(m) for m in dots],lag_ratio=.005),run_time=1.3)
  self.at('The same geometric test');small=Circle(radius=r/2,color=GOLD,fill_color=GOLD,fill_opacity=.18).move_to(c);self.play(Create(small),run_time=.7)
  self.at('But its area');self.play(Write(equation(r'P=\frac{\pi(R/2)^2}{\pi R^2}=\frac14')),run_time=1)
  self.at('Before asking');self.show(text('Define the experiment first.',27,WHITE,True).move_to(DOWN*4.4))
  self.finish()
