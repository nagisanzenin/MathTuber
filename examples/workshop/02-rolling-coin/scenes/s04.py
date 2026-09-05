from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        r=.65;R=3*r;center=UP*.8;fixed=self.coin(R,'primary').move_to(center);fixed.remove(fixed[2]);moving=self.coin(r);base=moving.copy();theta=ValueTracker(0)
        def position(m):m.become(base.copy().rotate(4*theta.get_value()).move_to(center+(R+r)*np.array([np.cos(theta.get_value()),np.sin(theta.get_value()),0])))
        moving.add_updater(position);position(moving);self.add(fixed,moving,self.text('Bigger obstacle. Extra turn.'))
        self.at('radius three times');self.show(self.text('R = 3r',.8,'background','label'))
        self.at('circle of radius four');path=DashedVMobject(Circle(radius=R+r,color=self.palette['secondary']).move_to(center),num_dashes=55);self.show(path);self.note('CENTER PATH RADIUS = 4r',-2.3)
        self.at('turns four times');self.play(theta.animate.set_value(TAU),run_time=4.5,rate_func=linear)
        self.at('then add one');self.rule('TURNS = R / r + 1')
        self.at('stationary screen');self.note('OUTSIDE • NO SLIP • FIXED VIEW',-4,'muted')
        self.finish()
