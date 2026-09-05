from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        A=np.array([-2.7,-.6,0]);B=np.array([-.8,3.6,0]);C=np.array([2.6,.2,0]);handle=VectorizedPoint(B);t=ValueTracker(0)
        def data():
            u=t.get_value();b=handle.get_center();p=(1-u)*A+u*b;q=(1-u)*b+u*C;return p,q,(1-u)*p+u*q
        def curve():
            b=handle.get_center();return ParametricFunction(lambda u:(1-u)**2*A+2*u*(1-u)*b+u*u*C,t_range=[0,1,.01],color=self.palette['primary'],stroke_width=7)
        stroke=curve();self.play(Create(stroke),run_time=2.2);self.say('Straight choices. A flowing line.')
        self.at('Place three points');controls=always_redraw(lambda:VGroup(self.line(A,handle.get_center(),'muted',3),self.line(handle.get_center(),C,'muted',3),Dot(A,radius=.09,color=self.palette['ink']),Dot(handle.get_center(),radius=.11,color=self.palette['secondary']),Dot(C,radius=.09,color=self.palette['ink'])));self.add(controls);self.play(stroke.animate.set_stroke(opacity=.22),run_time=.5)
        self.at('The middle point');self.add(always_redraw(lambda:self.label('handle',handle.get_center()+UP*.4,'secondary','detail')))
        self.at('Now choose the same fraction');t.set_value(.5);p,q,z=data();first=Dot(p,radius=.11,color=self.palette['accent']);second=Dot(q,radius=.11,color=self.palette['accent']);self.play(FadeIn(first),run_time=.5)
        self.at('Halfway on the second');self.play(FadeIn(second),run_time=.5)
        self.at('Join those new points');bridge=self.line(p,q,'accent',4);final=Dot(z,radius=.13,color=self.palette['primary']);self.play(Create(bridge),run_time=.7);self.play(FadeIn(final),run_time=.5)
        self.at('Let the fraction change');self.remove(first,second,bridge,final);dynamic=always_redraw(lambda:VGroup(self.line(data()[0],data()[1],'accent',4),Dot(data()[0],radius=.09,color=self.palette['accent']),Dot(data()[1],radius=.09,color=self.palette['accent']),Dot(data()[2],radius=.12,color=self.palette['primary'])));self.add(dynamic);self.play(t.animate.set_value(0),run_time=1)
        self.at('Watch the final point');trace=TracedPath(lambda:data()[2],stroke_color=self.palette['primary'],stroke_width=7);self.add(trace);self.play(t.animate.set_value(1),run_time=5,rate_func=linear);trace.clear_updaters()
        self.at('At fraction zero');self.play(t.animate.set_value(0),run_time=1.6)
        self.at('At fraction one');self.play(t.animate.set_value(1),run_time=1.6)
        self.at('Move it');self.remove(trace,stroke);livecurve=always_redraw(curve);self.add(livecurve);self.play(t.animate.set_value(.45),run_time=.6);self.play(handle.animate.move_to([1.3,3.1,0]),run_time=2);self.play(handle.animate.move_to(B),run_time=2)
        self.at('stays inside the triangle');hull=always_redraw(lambda:self.poly(A,handle.get_center(),C,color='surface',opacity=.35).set_z_index(-1));self.add(hull);self.say('Every choice stays inside.');self.play(t.animate.set_value(.15),run_time=1.2)
        self.at('Each new point stays');self.play(t.animate.set_value(.8),run_time=2.5)
        self.at('Repeating the choice');self.play(t.animate.set_value(.35),run_time=1.7)
        self.at('This is one reason');self.say('A small set of handles.')
        self.at('fraction is not distance');self.say('Equal fractions ≠ equal distances')
        self.at('Three points, the same small choice');self.play(FadeOut(dynamic),FadeOut(hull),run_time=.8);self.say('A line learns to flow.');self.finish()
