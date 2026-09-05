from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        a=band(self,1.55,center=UP*2.1,scale=.75);b=band(self,2.7,center=DOWN*.8,scale=.75);self.add(a,b,self.text('Every slice matches in area.'))
        self.at('from the bottom');self.play(LaggedStart(*[Indicate(a[i],color=self.palette['accent']) for i in range(0,28,4)],lag_ratio=.25),LaggedStart(*[Indicate(b[i],color=self.palette['accent']) for i in range(0,28,4)],lag_ratio=.25),run_time=2.4)
        self.at('volumes must match');self.rule('EQUAL SLICES → EQUAL VOLUMES',-3.4)
        self.at('solid sphere of radius b');self.play(FadeOut(a),FadeOut(b),run_time=.6);sphere=VGroup(*[Ellipse(width=2*np.sqrt(max(0,1.2**2-z*z)),height=.45*np.sqrt(max(0,1.2**2-z*z)),color=self.palette['primary'],fill_color=self.palette['primary'],fill_opacity=.15,stroke_width=1).shift(UP*(z+.7)) for z in np.linspace(-1.19,1.19,30)]);self.show(sphere)
        self.at('diameter equals its height');h=DoubleArrow(LEFT*1.7+DOWN*.5,LEFT*1.7+UP*1.9,buff=0,color=self.palette['secondary']);self.show(h);self.note('SPHERE DIAMETER = BAND HEIGHT',-2.3)
        self.at('Different shapes');self.show(self.text('V = πh³ / 6',3.5,'primary'));self.finish()
