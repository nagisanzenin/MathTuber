from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        q=ValueTracker(1);L=4.;origin=UP*.8;cols=['primary','secondary','accent','ink']
        def loc(i,z=None):
         z=max(q.get_value() if z is None else z,1e-5);a=math.pi/4+i*math.pi/2-math.log(z);return origin+L/math.sqrt(2)*z*np.array([math.cos(a),math.sin(a),0])
        paths=VGroup(*[VMobject(color=self.palette[cols[i]],stroke_width=4).set_points_as_corners([loc(i,float(t)) for t in np.geomspace(1,.008,500)]) for i in range(4)])
        frame=always_redraw(lambda:Polygon(*[loc(i) for i in range(4)],stroke_color=self.palette['muted'],stroke_width=2,fill_opacity=0))
        def bug(i):
         a=loc(i);direction=loc((i+1)%4)-a;angle=math.atan2(direction[1],direction[0]);body=Ellipse(width=.29,height=.19,fill_color=self.palette[cols[i]],fill_opacity=1,stroke_color=self.palette['background'],stroke_width=1);head=Dot(RIGHT*.16,radius=.065,color=self.palette[cols[i]]);return VGroup(body,head).rotate(angle).move_to(a)
        bugs=always_redraw(lambda:VGroup(*[bug(i) for i in range(4)]));self.add(frame,bugs);self.play(q.animate.set_value(.25),run_time=4,rate_func=linear);self.play(Create(paths),run_time=1.5)
        self.at('starting square is four');self.say('A 4 m square. A 4 m path?')
        self.at('ignore the whole spiral');self.play(q.animate.set_value(.8),paths.animate.set_stroke(opacity=.18),run_time=1);self.say('Watch one gap.');
        self.at('Watch just one bug');gap=always_redraw(lambda:self.line(loc(0),loc(1),'secondary',8));self.add(gap)
        self.at('keep forming a smaller');self.play(q.animate.set_value(.62),run_time=3,rate_func=linear)
        self.at('chasing bug moves directly');a=loc(0);b=loc(1);c=loc(2);u=(b-a)/np.linalg.norm(b-a);v=(c-b)/np.linalg.norm(c-b);va=Arrow(a,a+u*.8,buff=0,color=self.palette['secondary'],stroke_width=5);vb=Arrow(b,b+v*.8,buff=0,color=self.palette['ink'],stroke_width=5);self.play(GrowArrow(va),run_time=.8)
        self.at('target moves along');right=RightAngle(Line(b,a),Line(b,c),length=.2,color=self.palette['ink']);self.play(GrowArrow(vb),Create(right),run_time=.8)
        self.at('Only the chaser');self.say('Target: 0 speed along this gap');self.play(Indicate(va),run_time=1)
        self.at('Watch the remaining gap');self.play(FadeOut(va),FadeOut(vb),FadeOut(right),q.animate.set_value(1),run_time=.8)
        barorigin=np.array([-2.4,-2.6,0]);bar=always_redraw(lambda:VGroup(self.line(barorigin,barorigin+RIGHT*4.8*q.get_value(),'secondary',13),self.line(barorigin+RIGHT*4.8*q.get_value(),barorigin+RIGHT*4.8,'primary',13)))
        labels=VGroup(self.label('gap left',[-1.5,-3.15,0],'secondary','detail'),self.label('distance traveled',[1.25,-3.15,0],'primary','detail'));self.add(bar,labels);self.say('Gap left + distance traveled = 4 m');self.play(q.animate.set_value(.12),run_time=5,rate_func=linear)
        self.at('four seconds to vanish');self.play(q.animate.set_value(.008),paths.animate.set_stroke(opacity=1),run_time=1.2)
        self.at('ever more tightly');self.say('Tighter turns. Finite distance.')
        self.at('Double the starting square');self.say('Double the square → double the path');small=paths.copy().scale(.35).move_to(LEFT*1.8+UP*2.1);large=paths.copy().scale(.7).move_to(RIGHT*.8+DOWN*.9);self.play(FadeOut(paths),FadeOut(frame),FadeOut(bugs),FadeOut(gap),FadeOut(bar),FadeOut(labels),FadeIn(small),run_time=.6);self.play(TransformFromCopy(small,large),run_time=1.5);self.add(self.label('4 m',[-1.8,3.4,0],'ink','detail'),self.label('8 m',[.8,-3.2,0],'ink','detail'));self.finish()
