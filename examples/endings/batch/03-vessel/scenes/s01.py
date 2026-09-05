from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        f=ValueTracker(.02);cx=ValueTracker(0);scale=ValueTracker(1);H=3.8;R=1.8;bottom=-.4
        
        def pos(x,y):return np.array([cx.get_value()+scale.get_value()*x,bottom+scale.get_value()*y,0])
        def depth():return H*f.get_value()**(1/3)
        outline=always_redraw(lambda:VGroup(self.line(pos(-R,H),pos(0,0),'ink',3),self.line(pos(0,0),pos(R,H),'ink',3),Ellipse(width=2*R*scale.get_value(),height=.35*scale.get_value(),color=self.palette['ink']).move_to(pos(0,H))))
        water=always_redraw(lambda:self.poly(pos(0,0),pos(R*depth()/H,depth()),pos(-R*depth()/H,depth()),color='primary',opacity=.3))
        surface=always_redraw(lambda:Ellipse(width=max(.01,2*R*depth()/H*scale.get_value()),height=.25*scale.get_value(),color=self.palette['primary'],fill_color=self.palette['primary'],fill_opacity=.2).move_to(pos(0,depth())))
        stand=always_redraw(lambda:VGroup(self.line(pos(0,0),pos(0,-.5),'muted',3),self.line(pos(-.7,-.5),pos(.7,-.5),'muted',3)))
        stream=always_redraw(lambda:self.line(pos(0,H+.65),pos(0,depth()+.13),'primary',3))
        self.add(stand,water,surface,outline,stream);clock=self.process_clock();f.add_updater(lambda m:m.set_value(min(.95,.02+.09*clock.value)));self.add(f);self.at('A steady pour');self.wait(.1)
        self.at('In a bowl');self.wait(.1)
        self.at('Imagine a cone');f.clear_updaters();clock.pause();self.remove(stream);self.play(f.animate.set_value(.125),run_time=1);kind=self.label('ideal cone',[0,4.7,0],'muted','label');self.play(FadeIn(kind),run_time=.4)
        self.at('Near the bottom');self.focus_outline(surface,run_time=.6)
        self.at('Higher up');self.play(f.animate.set_value(.7),run_time=2)
        self.at('A larger surface');self.focus_outline(surface,run_time=.6)
        self.at('For a perfect');self.play(f.animate.set_value(.125),run_time=1);half=self.line(pos(-R*.5,H*.5),pos(R*.5,H*.5),'accent',4);self.play(Create(half),run_time=.5)
        self.at('Volume therefore');rule=self.label('volume ∝ depth³',[0,-1.75,0],'ink','claim');self.play(FadeIn(rule),run_time=.5)
        self.at('At half');label=self.label('½ height → ⅛ volume',[0,-2.7,0],'primary','claim');self.play(FadeIn(label),run_time=.5)
        self.at('Half the height');self.focus_outline(label,run_time=.6)
        self.at('This is geometry');self.play(FadeOut(rule),FadeOut(half),run_time=.4)
        self.at('The point');self.wait(.2)
        self.at('Now place');self.play(FadeOut(label),FadeOut(kind),cx.animate.set_value(-1.7),scale.animate.set_value(.7),f.animate.set_value(.02),run_time=2)
        rc=R/(3**.5)*.7;hc=H*.7;xc=1.45
        cylinder=VGroup(self.line([xc-rc,bottom,0],[xc-rc,bottom+hc,0],'ink',3),self.line([xc+rc,bottom,0],[xc+rc,bottom+hc,0],'ink',3),Ellipse(width=2*rc,height=.22,color=self.palette['ink']).move_to([xc,bottom,0]),Ellipse(width=2*rc,height=.22,color=self.palette['ink']).move_to([xc,bottom+hc,0]))
        cwater=always_redraw(lambda:Rectangle(width=2*rc,height=max(.01,hc*f.get_value()),stroke_width=0,fill_color=self.palette['secondary'],fill_opacity=.3).move_to([xc,bottom+hc*f.get_value()/2,0]));csurf=always_redraw(lambda:Ellipse(width=2*rc,height=.2,color=self.palette['secondary']).move_to([xc,bottom+hc*f.get_value(),0]));self.add(cwater,csurf);self.play(FadeIn(cylinder),run_time=.6);self.add(self.label('same height • same capacity',[0,3.75,0],'muted','label').scale(.85))
        self.at('Pour equal');self.add(stream);stream2=always_redraw(lambda:self.line([xc,bottom+hc+.45,0],[xc,bottom+hc*f.get_value()+.1,0],'secondary',3));self.add(stream2);self.play(f.animate.set_value(.5),run_time=3.2,rate_func=linear);self.remove(stream,stream2)
        self.at('In the straight');self.focus_outline(csurf,run_time=.6)
        self.at('When each');self.add(self.label('79% high',[-1.7,-1.25,0],'primary','label'),self.label('50% high',[1.45,-1.25,0],'secondary','label'));result=self.label('both hold ½ their capacity',[0,-2.35,0],'ink','claim').scale(.9);self.play(FadeIn(result),run_time=.6)
        self.at('The water keeps');self.finish()
