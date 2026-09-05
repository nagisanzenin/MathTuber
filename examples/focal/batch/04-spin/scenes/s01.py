from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        R=1.8;I0=.5;mass=1.;L=(I0+2*R*R)*.35
        platform=VGroup(Circle(radius=2.4,color=self.palette['ink'],fill_color=self.palette['accent'],fill_opacity=.12,stroke_width=3),Circle(radius=2.15,color=self.palette['muted'],stroke_width=1),Circle(radius=.26,color=self.palette['ink'],fill_color=self.palette['background'],fill_opacity=1))
        rail=self.line([-2,0,0],[2,0,0],'ink',4);beads=VGroup(*[Dot([s*R,0,0],radius=.17,color=self.palette[c]) for s,c in [(-1,'primary'),(1,'secondary')]])
        subject=VGroup(platform,rail,beads).scale(.7).shift(UP*1.4);self.add(subject)
        self.at('Two small weights');self.play(Rotate(VGroup(rail,beads),angle=1.1,about_point=platform.get_center()),run_time=2.5,rate_func=linear)
        self.at('Bringing them');self.at('Look down');self.stage_focus(subject,UP*.8,width=6.4,height=6.4,run_time=1.8)
        center=platform.get_center();scale=platform[0].width/4.8
        scope=self.label('top view • no external torque',[0,5.25,0],'muted','label').scale(.85);self.add(scope)
        self.at('We will ignore');self.at('The moving weights')
        self.at('A mass farther');radial=np.array([math.cos(1.1),math.sin(1.1),0]);measure=self.line(center,center+radial*R*scale,'primary',3);distance=self.label('distance',center+radial*R*scale*.55+LEFT*.95,'primary','label');self.play(Create(measure),FadeIn(distance),run_time=.7)
        self.at('For a small');eq=self.label('weight contribution ∝ distance²',[0,-3.3,0],'ink','claim').scale(.8);self.play(FadeIn(eq),run_time=.6)
        self.at('Move it halfway');note=self.label('½ distance → ¼ contribution',[0,-4.15,0],'primary','label');self.play(FadeIn(note),run_time=.5)
        self.at('Draw both');self.play(FadeOut(measure),FadeOut(distance),FadeOut(note),FadeOut(eq),run_time=.4)
        start=self.renderer.time;in_duration=2.;out_start=self.times['Let the weights']-start;out_duration=2.
        def segment_integral(a,b,duration):
            if abs(a-b)<1e-10:return L*duration/(I0+2*a*a)
            k=math.sqrt(2/I0)
            return L*duration/(b-a)/math.sqrt(2*I0)*(math.atan(k*b)-math.atan(k*a))
        def state(t):
            t=max(0,t)
            if t<in_duration:
                r=R+(R/2-R)*t/in_duration;angle=segment_integral(R,r,t) if t else 0
            elif t<out_start:
                r=R/2;angle=segment_integral(R,R/2,in_duration)+L*(t-in_duration)/(I0+2*r*r)
            elif t<out_start+out_duration:
                dt=t-out_start;r=R/2+(R-R/2)*dt/out_duration;angle=segment_integral(R,R/2,in_duration)+L*(out_start-in_duration)/(I0+2*(R/2)**2)+segment_integral(R/2,r,dt)
            else:
                r=R;angle=segment_integral(R,R/2,in_duration)+L*(out_start-in_duration)/(I0+2*(R/2)**2)+segment_integral(R/2,R,out_duration)+L*(t-out_start-out_duration)/(I0+2*R*R)
            return r,angle+1.1
        clock=self.process_clock();self.remove(rail,beads)
        def moving():
            r,a=state(clock.value);direction=np.array([math.cos(a),math.sin(a),0]);line=self.line(center-2*scale*direction,center+2*scale*direction,'ink',4)
            dots=VGroup(*[Dot(center+s*r*scale*direction,radius=.17*scale,color=self.palette[c]) for s,c in [(-1,'primary'),(1,'secondary')]])
            return VGroup(line,dots)
        live=always_redraw(moving);self.add(live);self.wait(2)
        self.at('The total rotational');self.at('Their product');summary=self.label('inertia × angular speed = constant',[0,-3.3,0],'ink','claim').scale(.77);self.play(FadeIn(summary),run_time=.6)
        self.at('The platform itself');self.at('The extra energy');self.at('Conserving angular');self.at('Let the weights');self.at('Distance from');self.finish()
