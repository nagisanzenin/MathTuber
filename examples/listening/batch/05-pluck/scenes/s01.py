from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];fraction=ValueTracker(.5);motion=ValueTracker(0);clock=self.process_clock(rate=.35)
        board=RoundedRectangle(width=6.5,height=1.3,corner_radius=.25,fill_color='#D6BB8F',fill_opacity=1,stroke_color='#B29977',stroke_width=2).move_to([0,2.2,0]);self.add(board)
        for x in [-3,3]:self.add(Rectangle(width=.13,height=1,fill_color='#8D775A',fill_opacity=1,stroke_width=0).move_to([x,2.2,0]))
        def coeff(n,r):return 2*np.sin(n*PI*r)/(n*n*PI*PI*r*(1-r))
        def curve():
            r=fraction.get_value();points=[]
            for x in np.linspace(0,1,241):
                triangular=x/r if x<=r else (1-x)/(1-r);dynamic=sum(coeff(n,r)*np.sin(n*PI*x)*np.cos(TAU*n*clock.value) for n in range(1,13));y=(1-motion.get_value())*triangular+motion.get_value()*dynamic;points.append([6*x-3,2.2+.45*y,0])
            return VMobject().set_points_as_corners(points).set_stroke(INK,3)
        self.add(always_redraw(curve));pluck=always_redraw(lambda:Dot([6*fraction.get_value()-3,2.65,0],radius=.07,color=CORAL));self.add(pluck)
        position=always_redraw(lambda:self.label('midpoint' if abs(fraction.get_value()-.5)<.001 else 'one third' if abs(fraction.get_value()-1/3)<.001 else 'moving pluck',[0,3.55,0]).scale(.8));self.add(position)
        def spectrum():
            g=VGroup()
            for n in range(1,7):
                height=1.6*abs(coeff(n,fraction.get_value()));x=-2.5+(n-1);g.add(Rectangle(width=.38,height=max(.003,height),fill_color=TEAL,fill_opacity=.85,stroke_width=0).move_to([x,-.3+height/2,0]));g.add(self.label(str(n),[x,-.65,0]).scale(.75))
            return g
        bars=always_redraw(spectrum);self.add(bars,self.label('mode number',[0,-1.2,0]).scale(.7),self.label('string motion shown slowly',[0,4.5,0]).scale(.75))
        self.at('The same string');self.at('Its length and tension');self.at('Listen to a simple');duration=self.listen('middle');motion.set_value(1);self.wait(duration)
        self.at('A string has');self.at('The starting shape');motion.set_value(0);self.at('A midpoint pluck');missing=self.label('2, 4, 6 … absent',[0,-2.1,0],role='claim');self.play(FadeIn(missing),run_time=.5)
        self.at('Now pluck one third');self.play(FadeOut(missing),fraction.animate.set_value(1/3),run_time=1);self.at('Modes three, six');self.play(FadeIn(self.label('3, 6, 9 … absent',[0,-2.1,0],role='claim')),run_time=.5)
        self.at('Their pattern has');mode=VMobject().set_points_as_corners([[6*x-3,2.2+.45*np.sin(3*PI*x),0] for x in np.linspace(0,1,100)]).set_stroke(CORAL,2);self.play(Create(mode),run_time=.6);node=Circle(radius=.13,color=CORAL).move_to([-1,2.2,0]);self.play(Create(node),run_time=.4)
        self.at('The allowed frequencies');self.play(FadeOut(mode),FadeOut(node),run_time=.5);self.at('What changes is');self.at('Here is the one-third');duration=self.listen('third');motion.set_value(1);self.wait(duration)
        self.at('Mathematically, each share');eq=self.label('sin(n × π × pluck fraction)',[0,-3.25,0],role='claim').scale(.77);self.play(FadeIn(eq),run_time=.5);self.at('When that sine');self.at('Real strings and');self.at('Where a small gesture');self.finish()
