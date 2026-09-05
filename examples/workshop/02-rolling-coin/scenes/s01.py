from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        r=1.1;center=UP*.65;fixed=self.coin(r,'primary').move_to(center);fixed.remove(fixed[2]);moving=self.coin(r);base=moving.copy();theta=ValueTracker(0)
        def position(m):m.become(base.copy().rotate(2*theta.get_value()).move_to(center+2*r*np.array([np.cos(theta.get_value()),np.sin(theta.get_value()),0])))
        moving.add_updater(position);position(moving);self.add(fixed,moving,self.text('One lap. How many spins?'))
        self.at('Watch the arrow');self.play(theta.animate.set_value(PI),run_time=3,rate_func=linear)
        self.at('one full turn');self.note('HALF A LAP → 1 TURN',-2.7)
        self.at('Finish the lap');self.play(theta.animate.set_value(TAU),run_time=1.1,rate_func=linear)
        self.at('turned twice');self.rule('ONE LAP → 2 TURNS')
        self.at('moving center');dot=Dot(moving.get_center(),color=self.palette['secondary'],radius=.1);self.show(dot);self.finish()
