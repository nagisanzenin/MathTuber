from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];X=.8;Y=-2;q=ValueTracker(0);a=ValueTracker(2)
        def pull(s):return np.array([X,Y+s,0])
        def trail(s,length=2):return np.array([X-length/np.cosh(s/length),Y+s-length*np.tanh(s/length),0])
        track=Line([X,-2.3,0],[X,4.35,0],color='#BBA785',stroke_width=9);self.add(track)
        trace=self.trace_curve(trail,q.get_value,0,6,1001,color='primary',stroke_width=5);self.add(trace)
        thread=always_redraw(lambda:Line(trail(q.get_value(),a.get_value()),pull(q.get_value()),color=CORAL,stroke_width=5));follower=always_redraw(lambda:self.bead(.15,'primary').move_to(trail(q.get_value(),a.get_value())));tractor=always_redraw(lambda:self.tile(.25,.25,'ink').move_to(pull(q.get_value())));self.add(thread,follower,tractor)
        claim=self.label('a fixed thread · a changing direction',[0,4.8,0]).scale(.9);self.add(claim)
        self.at('A small point');self.play(q.animate.set_value(.6),run_time=2,rate_func=smooth);self.at('The other end');self.play(q.animate.set_value(1.2),run_time=2,rate_func=smooth);self.at('The trailing point draws');self.play(q.animate.set_value(1.8),run_time=2.5,rate_func=smooth)
        self.at('In this ideal model');self.play(q.animate.set_value(2.5),run_time=3.5,rate_func=smooth);self.at('The thread does');self.at('Its direction is therefore');pt=trail(q.get_value());direction=(pull(q.get_value())-pt)/2;arrow=Arrow(pt-.45*direction,pt+.45*direction,buff=0,color=INK,stroke_width=4);self.play(Create(arrow),run_time=.5)
        self.at('Pause and look');self.focus_outline(thread,buff=.1,run_time=.7);self.at('It reaches from');measure=self.label('thread length: 2',[0,-3.1,0],role='claim');self.play(FadeIn(measure),run_time=.5)
        self.at('This constant tangent');claim=self.replace_label(claim,self.label('tractrix',[0,4.8,0],role='claim'),.5);self.play(FadeOut(arrow),run_time=.3)
        self.at('Keep pulling');self.play(q.animate.set_value(3.1),run_time=1.5,rate_func=smooth);self.at('The trailing point comes');self.play(q.animate.set_value(4.8),run_time=4,rate_func=smooth);self.at('The gap keeps shrinking');self.play(q.animate.set_value(6),run_time=3.8,rate_func=smooth)
        self.at('Start again');trace.clear_updaters();trace.set_stroke(color=INK,opacity=.35,width=3);self.play(q.animate.set_value(0),run_time=.8,rate_func=smooth);self.play(a.animate.set_value(1),run_time=.5);measure=self.replace_label(measure,self.label('thread length: 1',[0,-3.1,0],role='claim'),.3)
        second=self.trace_curve(lambda s:trail(s,1),q.get_value,0,6,1001,color='primary',stroke_width=5);self.add(second)
        self.at('The point begins');self.play(q.animate.set_value(2.5),run_time=3.8,rate_func=smooth);self.at('At the same pulling');self.play(q.animate.set_value(4.5),run_time=2.8,rate_func=smooth);self.at('A different length');self.play(q.animate.set_value(6),run_time=2.2,rate_func=smooth);self.finish()
