from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        u=ValueTracker(0);radius=.6;ybase=.25;anchor=4.;hand=2.4
        beam=self.line([-1.25,anchor,0],[-.05,anchor,0],'ink',6);self.add(beam)
        def cy():return ybase+u.get_value()
        rope=always_redraw(lambda:VGroup(self.line([-radius,anchor,0],[-radius,cy(),0],'accent',5),Arc(radius=radius,start_angle=PI,angle=PI,color=self.palette['accent'],stroke_width=5).move_arc_center_to([0,cy(),0]),self.line([radius,cy(),0],[radius,hand+2*u.get_value(),0],'accent',5)))
        wheel=always_redraw(lambda:VGroup(Circle(radius=radius-.045,color=self.palette['ink'],fill_color=self.palette['background'],fill_opacity=1).move_to([0,cy(),0]),Dot([0,cy(),0],radius=.08,color=self.palette['ink'])))
        def basket():
         y=cy()-1.4
         pot=self.poly([-.6,y+.35,0],[.6,y+.35,0],[.42,y-.45,0],[-.42,y-.45,0],color='secondary',opacity=.3)
         handle=Arc(radius=.6,start_angle=0,angle=PI,color=self.palette['ink']).move_arc_center_to([0,y+.35,0]);stem=self.line([0,y+.35,0],[0,y+.85,0],'primary',3)
         leaves=VGroup(*[Ellipse(width=.55,height=.22,color=self.palette['primary'],fill_color=self.palette['primary'],fill_opacity=.3).rotate(s*.4).move_to([s*.2,y+.6,0]) for s in [-1,1]])
         return VGroup(pot,handle,stem,leaves,self.line([0,cy(),0],[0,y+.95,0],'ink',3))
        load=always_redraw(basket);grip=always_redraw(lambda:RoundedRectangle(width=.55,height=.2,corner_radius=.05,color=self.palette['ink']).move_to([radius,hand+2*u.get_value(),0]))
        self.add(load,wheel,rope,grip);self.at('A small pulley');self.play(u.animate.set_value(.65),run_time=3)
        self.at('But it asks');self.play(u.animate.set_value(0),run_time=2)
        self.at('One end');self.focus_outline(beam,run_time=.6)
        self.at('The rope passes');self.focus_outline(wheel,run_time=.6)
        self.at('Two strands');forces=VGroup(*[Arrow([x,.5,0],[x,1.5,0],buff=0,color=self.palette['primary']) for x in [-radius,radius]]);self.play(FadeIn(forces),run_time=.5)
        self.at('For an ideal');eq=self.label('½ weight + ½ weight',[0,-2.35,0],'ink','claim').scale(.85);self.play(FadeIn(eq),run_time=.5)
        self.at('Watch the basket');self.play(FadeOut(forces),FadeOut(eq),u.animate.set_value(1),run_time=2.5)
        self.at('Both supporting');marks=VGroup(DashedLine([-1.3,ybase,0],[-1.3,ybase+1,0],color=self.palette['primary']),self.label('1 m',[-1.8,ybase+.5,0],'primary','label'));self.play(FadeIn(marks),run_time=.6)
        self.at('The free end must');hm=VGroup(DashedLine([1.45,hand,0],[1.45,hand+2,0],color=self.palette['secondary']),self.label('2 m',[2.05,hand+1,0],'secondary','label'));self.play(FadeIn(hm),run_time=.6)
        self.at('Half the force');trade=self.label('½ force × 2 distance',[0,-2.35,0],'ink','claim');self.play(FadeIn(trade),run_time=.5)
        self.at('Force times');work=self.label('same ideal work',[0,-3.2,0],'primary','label');self.play(FadeIn(work),run_time=.5)
        self.at('The energy needed');self.focus_outline(load,run_time=.6)
        self.at('We are ignoring');scope=self.label('ideal slow lift • no friction',[0,5.15,0],'muted','label').scale(.85);self.play(FadeIn(scope),run_time=.5)
        self.at('Now start again');self.play(FadeOut(marks),FadeOut(hm),FadeOut(trade),FadeOut(work),u.animate.set_value(0),run_time=1);self.play(u.animate.set_value(.5),run_time=2)
        self.at('The basket rises');newmarks=VGroup(DashedLine([-1.3,ybase,0],[-1.3,ybase+.5,0],color=self.palette['primary']),self.label('½ m',[-1.85,ybase+.25,0],'primary','label'),DashedLine([1.45,hand,0],[1.45,hand+1,0],color=self.palette['secondary']),self.label('1 m',[2.05,hand+.5,0],'secondary','label'));self.play(FadeIn(newmarks),run_time=.7)
        self.at('The geometry');close=self.label('rope travels twice as far',[0,-2.3,0],'ink','claim').scale(.9);self.play(FadeIn(close),run_time=.5)
        self.at('A simple machine');self.finish()
