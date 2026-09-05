from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        r=.65;line=Line(LEFT*2.8+UP*.3,RIGHT*2.8+UP*.3,color=self.palette['ink']);wheel=self.coin(r).move_to(LEFT*2.5+UP*(.3+r));base=wheel.copy();v=ValueTracker(0)
        wheel.add_updater(lambda m:m.become(base.copy().rotate(-v.get_value()).shift(RIGHT*r*v.get_value())))
        self.add(line,wheel,self.text('Follow the CENTER.'))
        self.at('One complete turn');self.play(v.animate.set_value(TAU),run_time=3.5,rate_func=linear)
        self.at('bend the road');wheel.clear_updaters();self.play(FadeOut(wheel),FadeOut(line),run_time=.5);fixed=self.coin(1,'primary').move_to(UP*.6);fixed.remove(fixed[2]);path=DashedVMobject(Circle(radius=2,color=self.palette['secondary']).move_to(UP*.6),num_dashes=55);self.show(fixed,path)
        self.at('one extra radius away');rad=Line(UP*.6,RIGHT*2+UP*.6,color=self.palette['secondary'],stroke_width=5);self.show(rad);self.note('RADIUS: r + r = 2r',-2.5)
        self.at('twice as long');self.rule('CENTER PATH: 2 × CIRCUMFERENCE');dot=Dot(RIGHT*2+UP*.6,radius=.11,color=self.palette['secondary']);self.add(dot);self.play(MoveAlongPath(dot,Circle(radius=2).move_to(UP*.6)),run_time=3,rate_func=linear)
        self.finish()
