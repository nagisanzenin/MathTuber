from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];clock=self.process_clock(rate=.65);amp=[ValueTracker(0),ValueTracker(0)]
        beta=4.730040744862704;sigma=(np.cosh(beta)-np.cos(beta))/(np.sinh(beta)-np.sin(beta))
        def phi(x):return (np.cosh(beta*x)+np.cos(beta*x)-sigma*(np.sinh(beta*x)+np.sin(beta*x)))/2
        lengths=[3.6,3.6/np.sqrt(2)];xs=[-1.6,1.6];top=3.5
        rail=RoundedRectangle(width=5.6,height=.25,corner_radius=.08,fill_color='#AF8B64',fill_opacity=1,stroke_width=0).move_to([0,4.6,0]);self.add(rail)
        def tube(j):
            points=[np.array([xs[j]+amp[j].get_value()*.13*phi(x)*np.sin(TAU*clock.value*(j+1)),top-lengths[j]*x,0]) for x in np.linspace(0,1,70)];shape=VMobject().set_points_as_corners(points).set_stroke('#827D68',18);shine=VMobject().set_points_as_corners([p+LEFT*.035 for p in points]).set_stroke('#D1C8A7',5);return VGroup(shape,shine)
        for j in range(2):
            self.add(Line([xs[j],4.45,0],[xs[j],top-lengths[j]*.2242,0],color='#B4A58A',stroke_width=1.5),always_redraw(lambda j=j:tube(j)))
            self.add(self.label(['220 Hz','440 Hz'][j],[xs[j],-.8,0],role='claim'))
        slow=self.label('bending shown slowly • selected mode',[0,-3.5,0]).scale(.72);self.add(slow)
        def hear(identity,j):
            duration=self.listen(identity);amp[j].set_value(1);self.wait(duration);amp[j].set_value(0)
        self.at('Two wind chimes');self.at('One is shorter');self.at('Here is a simple');hear('long',0);hear('short',1)
        self.at('These tubes bend');amp[0].set_value(1);amp[1].set_value(1);self.at('The ends move');nodes=VGroup(*[Circle(radius=.07,color=CORAL,fill_opacity=1).move_to([xs[j],top-lengths[j]*x,0]) for j in range(2) for x in [.2242,.7758]]);self.play(FadeIn(nodes),run_time=.5);self.at('We show that bending');self.at('For this ideal');eq=self.label('f ∝ 1 / L²',[0,-1.8,0],role='claim');self.play(FadeIn(eq),run_time=.5)
        self.at('Make the length');dims=VGroup(self.label('L',[-2.55,1.8,0]),self.label('L / √2',[2.75,2,0]).scale(.8));self.play(FadeIn(dims),run_time=.5);self.at('The shorter tube');self.at('Here the lengths');self.at('Their modeled notes');self.at('Hear that comparison');amp[0].set_value(0);amp[1].set_value(0);hear('long-again',0);hear('short-again',1)
        self.at('These pure tones');amp[0].set_value(1);amp[1].set_value(1);self.at('A real chime');self.at('The rule assumes');self.at('A small change');self.finish()
