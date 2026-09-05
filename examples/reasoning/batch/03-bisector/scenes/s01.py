from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        A=np.array([-1.,3.4,0]);B=np.array([-2.5,-.6,0]);C=np.array([2.7,-.6,0])
        def split(a):
            ab=np.linalg.norm(a-B);ac=np.linalg.norm(a-C);return (ac*B+ab*C)/(ab+ac)
        D=split(A)
        def foot(p,a,b):
            u=b-a;return a+np.dot(p-a,u)/np.dot(u,u)*u
        def diagram(a):
            q=split(a);left=self.poly(a,B,q,opacity=.48);right=self.poly(a,q,C,color='secondary',opacity=.48);bis=self.line(a,q,'ink',3);arcs=VGroup(Angle(Line(a,B),Line(a,q),radius=.55,color=self.palette['ink']),Angle(Line(a,q),Line(a,C),radius=.72,color=self.palette['ink']));names=VGroup(*[self.label(t,v+offset,'ink','label').scale(.85) for t,v,offset in [('A',a,UP*.4),('B',B,LEFT*.3+DOWN*.25),('C',C,RIGHT*.3+DOWN*.25),('D',q,DOWN*.4)]]);return VGroup(left,right,bis,arcs,names)
        fig=diagram(A);self.add(fig);self.at('A line');self.focus_outline(fig[3],run_time=.8);self.at('But it does');self.at('Call the meeting');self.focus_outline(fig[4][-1],run_time=.7)
        self.at('Look at');self.at('With their bases');H=np.array([A[0],B[1],0]);alt=DashedLine(A,H,color=self.palette['ink'],stroke_width=3);square=RightAngle(Line(H,A),Line(H,C),length=.18,color=self.palette['ink']);self.play(Create(alt),Create(square),run_time=.8)
        self.at('Their areas');ratio=self.label('left area : right area = BD : DC',[0,-2,0],'ink','claim').scale(.75);self.play(FadeIn(ratio),run_time=.7)
        self.at('Now use');self.play(FadeOut(alt),FadeOut(square),run_time=.5);self.play(Create(self.line(A,B,'primary',6)),Create(self.line(A,C,'secondary',6)),run_time=.8)
        self.at('Drop a perpendicular');E=foot(D,A,B);F=foot(D,A,C);heights=VGroup(DashedLine(D,E,color=self.palette['ink'],stroke_width=3),DashedLine(D,F,color=self.palette['ink'],stroke_width=3));rights=VGroup(RightAngle(Line(E,D),Line(E,A),length=.15,color=self.palette['ink']),RightAngle(Line(F,D),Line(F,A),length=.15,color=self.palette['ink']));self.play(Create(heights),Create(rights),run_time=1)
        self.at('The small right');self.focus_outline(fig[3],run_time=.8);self.at('So these');self.focus_outline(heights,run_time=.8)
        self.at('The same two');ratio2=self.label('left area : right area = AB : AC',[0,-2.9,0],'ink','claim').scale(.75);self.play(FadeIn(ratio2),run_time=.7)
        self.at('One area');self.at('They must');result=self.label('BD : DC = AB : AC',[0,-2.2,0],'ink','claim');self.play(FadeOut(ratio),FadeOut(ratio2),run_time=.4);self.play(FadeIn(result),run_time=.6)
        self.at('Move the top');self.remove(*self.mobjects);x=ValueTracker(A[0]);moving=always_redraw(lambda:diagram(np.array([x.get_value(),3.4,0])));self.add(moving,result);self.play(x.animate.set_value(.8),run_time=2.5)
        self.at('The base division');self.play(x.animate.set_value(-.4),run_time=2.5);self.at('Equal angles');self.finish()
