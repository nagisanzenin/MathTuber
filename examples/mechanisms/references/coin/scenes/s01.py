from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        r=1.05;c=UP*.6;t=ValueTracker(0);fixed=self.coin(r,'primary').move_to(c);base=self.coin(r)
        def wheel():return base.copy().rotate(2*t.get_value()).move_to(c+2*r*np.array([np.cos(t.get_value()),np.sin(t.get_value()),0]))
        w=always_redraw(wheel);self.add(fixed,w);self.play(t.animate.set_value(PI),run_time=3,rate_func=linear)
        self.at('By the end');self.play(t.animate.set_value(TAU),run_time=3,rate_func=linear);self.say('1 lap → 2 turns')
        self.at('Now its center');dot=always_redraw(lambda:Dot(w.get_center(),radius=.08,color=self.palette['secondary']));trace=TracedPath(dot.get_center,stroke_color=self.palette['secondary'],stroke_width=5);self.add(trace,dot);self.play(t.animate.set_value(2*TAU),run_time=4.5,rate_func=linear)
        self.at('two coin radii');a=self.line(c,c+RIGHT*r,'ink');b=self.line(c+RIGHT*r,c+RIGHT*2*r,'secondary');self.play(Create(a),Create(b),run_time=1);self.say('r + r = 2r')
        self.at('Freeze the contact');contact=c+RIGHT*r;forward=Arrow(w.get_center(),w.get_center()+UP*1.15,color=self.palette['primary'],buff=0);back=Arrow(contact,contact+DOWN*1.15,color=self.palette['secondary'],buff=0);self.play(FadeIn(forward),FadeIn(back),run_time=.8)
        self.at('cancel at the touching point');mark=Circle(radius=.13,color=self.palette['ink']).move_to(contact);self.play(Create(mark),run_time=.7);self.say('Contact speed = 0')
        self.at('Center speed equals');self.say('v = rω',-3.4)
        self.at('two circumferences');self.play(FadeOut(forward),FadeOut(back),FadeOut(mark),FadeOut(a),FadeOut(b),run_time=.5);self.play(t.animate.set_value(3*TAU),run_time=2.3,rate_func=linear)
        self.at('Now make the obstacle');w.clear_updaters();dot.clear_updaters();self.remove(trace,dot);self.play(FadeOut(w),FadeOut(fixed),run_time=.4);R=1.65;r=.55;t.set_value(0);base=self.coin(r);fixed=self.coin(R,'primary').move_to(c);w=always_redraw(lambda:base.copy().rotate(4*t.get_value()).move_to(c+(R+r)*np.array([np.cos(t.get_value()),np.sin(t.get_value()),0])));self.add(fixed,w);self.say('3r + r = 4r')
        self.at('One lap now');self.play(t.animate.set_value(TAU),run_time=5,rate_func=linear);self.finish()
