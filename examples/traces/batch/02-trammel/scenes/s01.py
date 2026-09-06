from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];O=np.array([0,.7,0]);q=ValueTracker(0);f=ValueTracker(1/3);L=3
        def A(t):return O+np.array([L*np.cos(t),0,0])
        def B(t):return O+np.array([0,L*np.sin(t),0])
        def point(t,frac=1/3):return (1-frac)*A(t)+frac*B(t)
        for u in [RIGHT,UP]:
         self.add(Line(O-3.25*u,O+3.25*u,color='#CDB991',stroke_width=18),Line(O-3.25*u,O+3.25*u,color='#EEE4CB',stroke_width=5))
        self.add(self.label('straight tracks',[0,4.45,0]).scale(.85))
        trace=self.trace_curve(point,q.get_value,0,TAU,801,stroke_width=5);self.add(trace)
        rod=always_redraw(lambda:Line(A(q.get_value()),B(q.get_value()),color='#A9895F',stroke_width=9));sliders=always_redraw(lambda:VGroup(self.tile(.3,.3,'ink').move_to(A(q.get_value())),self.tile(.3,.3,'ink').move_to(B(q.get_value()))));pen=always_redraw(lambda:self.bead(.13,'secondary').move_to(point(q.get_value(),f.get_value())));self.add(rod,sliders,pen)
        self.at('Two sliders move');self.play(q.animate.set_value(.35),run_time=2,rate_func=smooth);self.at('One moves sideways');self.play(q.animate.set_value(.6),run_time=2.4,rate_func=smooth);self.at('A pencil between');self.play(q.animate.set_value(.8),run_time=2.3,rate_func=smooth)
        self.at('The sliders and pencil');self.at('Our pencil is');first=Line(A(.8),point(.8),color=CORAL,stroke_width=5);second=Line(point(.8),B(.8),color=TEAL,stroke_width=5);self.play(Create(first),Create(second),run_time=.6);measure=self.label('1 unit + 2 units',[0,-3.25,0],role='claim');self.play(FadeIn(measure),run_time=.4);self.at('Those two fixed');self.play(FadeOut(VGroup(first,second)),run_time=.4)
        self.at('Turn back until');self.play(q.animate.set_value(0),run_time=1.7,rate_func=smooth);self.at('The pencil reaches');measure=self.replace_label(measure,self.label('horizontal reach: 2',[0,-3.25,0],role='claim'),.4)
        self.at('Turn the bar upright');self.play(q.animate.set_value(PI/2),run_time=1.4,rate_func=smooth);self.at('Now it reaches');measure=self.replace_label(measure,self.label('vertical reach: 1',[0,-3.25,0],role='claim'),.4)
        self.at('Continue turning');measure=self.replace_label(measure,self.label('ellipse',[0,-3.25,0],role='claim'),.3);self.play(q.animate.set_value(PI),run_time=3.1,rate_func=smooth)
        self.at('The bar keeps');self.play(q.animate.set_value(1.6*PI),run_time=3,rate_func=smooth);self.at('A curved path');self.play(q.animate.set_value(TAU),run_time=2.5,rate_func=smooth)
        self.at('Now move the pencil');trace.clear_updaters();trace.set_stroke(color=INK,opacity=.3,width=3);q.set_value(0);self.play(f.animate.set_value(.5),run_time=1,rate_func=smooth);measure=self.replace_label(measure,self.label('equal reaches',[0,-3.25,0],role='claim'),.4)
        self.at('It is equally far');circle_trace=self.trace_curve(lambda t:point(t,.5),q.get_value,0,TAU,801,stroke_width=5);self.add(circle_trace)
        self.at('Both reaches become');self.play(q.animate.set_value(PI),run_time=3,rate_func=smooth);self.at('An ellipse and');self.play(q.animate.set_value(TAU),run_time=3,rate_func=smooth);self.finish()
