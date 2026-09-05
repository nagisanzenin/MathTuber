from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        c=np.array([0,1.7,0]);b=math.log(1.5)/(PI/2);a=.12;end=3.7*PI
        clock=self.process_clock(rate=1.5);draw_end=[end];phase=ValueTracker(end)
        def P(t):return c+a*math.exp(b*t)*np.array([math.cos(t),math.sin(t),0])
        def curve(lo,hi,color='primary',width=3):return VMobject(color=self.palette[color],stroke_width=width).set_points_as_corners([P(t) for t in np.linspace(lo,max(lo+.001,hi),max(3,int((hi-lo)*45)))])
        self.at('This spiral grows');ink=always_redraw(lambda:curve(0,min(end,clock.value+5.8)));self.add(ink,Dot(c,radius=.04,color=self.palette['ink']))
        self.at('The rule keeps');self.wait(.5)
        self.at('Start at this small');clock.pause();ink.clear_updaters();ink.become(curve(0,end));t=ValueTracker(2*PI)
        rad=always_redraw(lambda:self.line(c,P(t.get_value()),'secondary',3));dot=always_redraw(lambda:Dot(P(t.get_value()),radius=.075,color=self.palette['secondary']));self.add(rad,dot)
        self.at('After one quarter');old=rad.copy().clear_updaters().set_stroke(opacity=.3);self.add(old);self.play(t.animate.set_value(2.5*PI),run_time=1.5,rate_func=linear)
        self.at('After the next');old2=rad.copy().clear_updaters().set_stroke(opacity=.3);self.add(old2);self.play(t.animate.set_value(3*PI),run_time=1.5,rate_func=linear)
        self.at('The added distance');note=self.label('each quarter turn: × 1.5',[0,-1.4,0],'ink','label');self.play(FadeIn(note),run_time=.5)
        # A second continuous clock is the inspection marker, not the growth process.
        self.at('Now follow the direction');self.play(FadeOut(old),FadeOut(old2),FadeOut(note),run_time=.5);marker=self.process_clock(rate=.16,initial=2.3*PI);rad.clear_updaters();dot.clear_updaters();self.remove(rad,dot)
        def directions():
         q=marker.value;p=P(q);er=np.array([math.cos(q),math.sin(q),0]);et=np.array([-math.sin(q),math.cos(q),0]);tangent=(b*er+et)/math.sqrt(b*b+1);angle=math.atan2(1,b)
         return VGroup(Dot(p,radius=.075,color=self.palette['secondary']),self.line(p,p+er*.9,'muted',2),self.line(p-tangent*.35,p+tangent*.9,'secondary',3),Arc(radius=.35,start_angle=q,angle=angle,color=self.palette['accent'],stroke_width=3).shift(p))
        dirs=always_redraw(directions);self.add(dirs)
        self.at('The angle between');angle_label=self.label('same angle',[0,-1.7,0],'ink','label');self.play(FadeIn(angle_label),run_time=.5)
        self.at('The spiral is always');marker.pause()
        self.at('Enlarge a copy');self.play(FadeOut(dirs),FadeOut(angle_label),run_time=.5);copy=curve(0,end-PI/2,'secondary',3);self.add(copy);self.play(copy.animate.scale(1.5,about_point=c),run_time=1.6)
        self.at('Rotate it by');self.play(Rotate(copy,PI/2,about_point=c),run_time=1.7)
        self.at('The overlapping part');note=self.label('scale × 1.5 + turn ¼',[0,-1.7,0],'ink','label');self.play(FadeIn(note),run_time=.5)
        self.at('This family is');self.play(FadeOut(copy),FadeOut(note),run_time=.5);name=self.label('logarithmic spiral',[0,-1.7,0],'ink','label');self.play(FadeIn(name),run_time=.5)
        self.at('Different growth factors');# Change the rate only in a labeled family comparison, keeping the same outer size.
        other=VMobject(color=self.palette['secondary'],stroke_width=2).set_points_as_corners([c+2.15*math.exp(.36*(q-end))*np.array([math.cos(q),math.sin(q),0]) for q in np.linspace(0,end,400)])
        self.play(Create(other),run_time=1.8)
        self.at('No single factor');self.play(FadeOut(other),run_time=.5)
        self.at('The beauty here');self.play(FadeOut(name),run_time=.5);self.finish()
