from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        f=1.;offset=np.array([0,-1.5,0])
        def point(x):return np.array([x,x*x/(4*f),0])+offset
        curve=ParametricFunction(lambda x:point(x),t_range=[-2.6,2.6],color=self.palette['ink'],stroke_width=7)
        back=ParametricFunction(lambda x:point(x)+DOWN*.12,t_range=[-2.6,2.6],color=self.palette['muted'],stroke_width=3)
        focus=Dot(offset+UP*f,radius=.075,color=self.palette['accent']);axis=DashedLine(offset+DOWN*.3,offset+UP*5,color=self.palette['muted'],stroke_width=1)
        subject=VGroup(curve,back,focus,axis).scale(.72).shift(UP*.9)
        self.add(subject);self.at('A curved mirror');self.play(Create(curve),run_time=1.3)
        opening=VGroup(*[VGroup(Arrow(.72*(point(t)+UP*2.8)+UP*.9,.72*point(t)+UP*.9,buff=0,tip_length=.12,color=self.palette['primary'],stroke_width=3),Arrow(.72*point(t)+UP*.9,focus.get_center(),buff=0,tip_length=.12,color=self.palette['secondary'],stroke_width=3)) for t in [-2,0,2]]);self.play(Create(opening),run_time=.9)
        self.at('But not every');self.play(FadeOut(opening),run_time=.5);self.at('Look along');self.stage_focus(subject,UP*.8,width=6.3,height=6.8,run_time=1.7)
        # Recover the uniform affine coordinates after staging from the axis.
        origin=axis.get_start();scale=axis.get_length()/5.3;vertex=origin+UP*.3*scale;F=vertex+UP*f*scale
        P=lambda x:vertex+scale*np.array([x,x*x/(4*f),0])
        scope=self.label('parabolic cross section • ideal rays',[0,5.35,0],'muted','label').scale(.85);fl=self.label('focus',F+UP*.65,'ink','label');axis.set_opacity(.15);self.add(scope,fl)
        self.at('Its surface');self.at('At each point')
        x=-1.9;p=P(x);n=np.array([-x/(2*f),1,0]);n/=np.linalg.norm(n)
        self.at('Follow one ray');incoming=Arrow(p+UP*2.8*scale,p,buff=0,tip_length=.12,color=self.palette['primary'],stroke_width=4);self.play(GrowArrow(incoming),run_time=1.2)
        self.at('The normal');normal=self.line(p-n*.65,p+n*.65,'muted',3);self.play(Create(normal),run_time=.8)
        self.at('The reflected');outgoing=Arrow(p,F,buff=0,tip_length=.12,color=self.palette['secondary'],stroke_width=4);self.play(GrowArrow(outgoing),run_time=1.1)
        self.at('Move the meeting');position=ValueTracker(x)
        def live_paths():
            t=position.get_value();q=P(t);normal_vector=np.array([-t/(2*f),1,0]);normal_vector/=np.linalg.norm(normal_vector)
            return VGroup(Arrow(q+UP*2.8*scale,q,buff=0,tip_length=.12,color=self.palette['primary'],stroke_width=4),self.line(q-normal_vector*.65,q+normal_vector*.65,'muted',3),Arrow(q,F,buff=0,tip_length=.12,color=self.palette['secondary'],stroke_width=4))
        moving=always_redraw(live_paths);self.remove(incoming,outgoing,normal);self.add(moving)
        self.play(position.animate.set_value(1.9),run_time=1.6)
        moving.clear_updaters();incoming,normal,outgoing=moving;self.remove(moving);self.add(incoming,normal,outgoing)
        self.at('The new ray');self.focus_outline(focus,run_time=.7)
        self.at('For this ideal');self.play(FadeOut(incoming),FadeOut(outgoing),FadeOut(normal),run_time=.4)
        paths=VGroup(*[VGroup(Arrow(P(t)+UP*2.8*scale,P(t),buff=0,tip_length=.12,color=self.palette['primary'],stroke_width=3),Arrow(P(t),F,buff=0,tip_length=.12,color=self.palette['secondary'],stroke_width=3)) for t in [-2.3,-1.45,-.65,.65,1.45,2.3]])
        self.play(LaggedStart(*[Create(v) for v in paths],lag_ratio=.1),run_time=2)
        self.at('A three dimensional');self.at('Real mirrors');self.at('Now reverse');self.play(FadeOut(paths),run_time=.6)
        self.at('Place the source');self.play(focus.animate.scale(1.6),run_time=.6)
        self.at('After reflection');reverse=VGroup(*[VGroup(Arrow(F,P(t),buff=0,tip_length=.12,color=self.palette['secondary'],stroke_width=3),Arrow(P(t),P(t)+UP*2.8*scale,buff=0,tip_length=.12,color=self.palette['primary'],stroke_width=3)) for t in [-2.3,-1.45,-.65,.65,1.45,2.3]]);self.play(LaggedStart(*[Create(v) for v in reverse],lag_ratio=.1),run_time=1.8)
        self.at('The same shape');close=self.label('one shape • two journeys',[0,-3.4,0],'ink','claim').scale(.9);self.play(FadeIn(close),run_time=.6);self.finish()
