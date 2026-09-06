from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];source=ValueTracker(-2.3);q=ValueTracker(0)
        cliffx=2.5;cliff=Polygon([cliffx,-1.7,0],[cliffx,3.7,0],[3.2,4.3,0],[3.8,3.8,0],[4.2,4.5,0],[4.2,-1.7,0],fill_color='#B5A98F',fill_opacity=1,stroke_width=0);ground=Line([-4,-1.7,0],[4.2,-1.7,0],color='#BBA98E',stroke_width=3);self.add(cliff,ground)
        for y in [-.8,.3,1.6,2.7]:self.add(Line([2.55,y,0],[3.8,y+.2,0],color='#968B76',stroke_width=1.5))
        def bell():
            x=source.get_value();return VGroup(Arc(radius=.3,start_angle=0,angle=PI,color=INK,stroke_width=3).move_to([x,.2,0]),Line([x-.3,0,0],[x+.3,0,0],color=INK,stroke_width=3),Dot([x,-.08,0],radius=.06,color=CORAL),Line([x,-.25,0],[x,-1.7,0],color='#9B8060',stroke_width=3))
        self.add(always_redraw(bell));path=always_redraw(lambda:DashedLine([source.get_value(),.8,0],[cliffx,.8,0],color='#A0ACA0',stroke_width=2));self.add(path)
        marker=always_redraw(lambda:self.bead(.11,'secondary').move_to([source.get_value()+(cliffx-source.get_value())*(1-abs(2*q.get_value()-1)),.8,0]));self.add(marker)
        label=self.label('1.0 s round trip',[0,4.7,0],role='claim');self.add(label)
        def pulse(emit,echo,delay):
            q.set_value(0);self.listen(emit);self.play(q.animate.set_value(1),run_time=delay,rate_func=linear);self.wait(self.listen(echo))
        self.at('A sound reaches');self.at('The quiet gap');self.at('Listen to this');pulse('emit', 'echo',1)
        self.at('The pulse has');out=Arrow([-2.3,1.4,0],[cliffx,1.4,0],buff=0,color=TEAL);back=Arrow([cliffx,2.1,0],[-2.3,2.1,0],buff=0,color=CORAL)
        self.at('Half the waiting');self.play(Create(out),run_time=.5);a=self.label('½ second',[0,1.05,0]).scale(.85);self.play(FadeIn(a),run_time=.3);self.at('The other half');self.play(Create(back),run_time=.5);b=self.label('½ second',[0,2.5,0]).scale(.85);self.play(FadeIn(b),run_time=.3)
        self.at('At twenty degrees');speed=self.label('sound speed ≈ 343 m/s',[0,-2.5,0]).scale(.85);self.play(FadeIn(speed),run_time=.5);self.at('A one-second echo');distance=self.label('distance ≈ 172 m',[0,-3.3,0],role='claim');self.play(FadeIn(distance),run_time=.5);self.at('We divide by two')
        self.at('Move the listener');self.play(FadeOut(VGroup(out,back,a,b)),source.animate.set_value(.1),run_time=1.5);label=self.replace_label(label,self.label('0.5 s round trip',[0,4.7,0],role='claim'),run_time=.25);distance=self.replace_label(distance,self.label('distance ≈ 86 m',[0,-3.3,0],role='claim'),run_time=.25)
        self.at('The round trip');self.at('Hear how the reply');pulse('near-emit','near-echo',.5)
        self.at('Distance is sound');formula=self.label('d = c × delay / 2',[0,2.1,0],role='claim');self.play(FadeIn(formula),run_time=.5);self.at('This model keeps');self.at('Our tones are');self.at('Even a moment');self.finish()
