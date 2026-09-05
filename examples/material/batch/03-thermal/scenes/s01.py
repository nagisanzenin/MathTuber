from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        center=np.array([0,1.65,0]);R=2;hole=1;scale=ValueTracker(1)
        def ring():
            s=scale.get_value();outer=Circle(radius=R*s,fill_color=self.palette['secondary'],fill_opacity=.7,stroke_color=self.palette['ink'],stroke_width=2).move_to(center)
            inner=Circle(radius=hole*s,fill_color=self.palette['background'],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=2).move_to(center)
            rim=Circle(radius=(R-.08)*s,stroke_color=self.palette['background'],stroke_width=2).move_to(center)
            return VGroup(outer,rim,inner)
        live=always_redraw(ring);self.add(live);self.at('Warm a metal');self.play(scale.animate.set_value(1.18),run_time=2);self.at('The empty');scope=self.label('uniform free expansion • exaggerated',[0,5.2,0],'muted','label').scale(.85);self.add(scope)
        self.at('Imagine the hole');self.play(scale.animate.set_value(1),run_time=.7);plug=Circle(radius=hole,fill_color=self.palette['primary'],fill_opacity=.35,stroke_color=self.palette['primary'],stroke_width=3).move_to(center);self.play(FadeIn(plug),run_time=.5)
        self.at('If the whole');self.play(scale.animate.set_value(1.18),plug.animate.scale(1.18),run_time=2)
        self.at('The imaginary');self.at('Take that disk');self.play(FadeOut(plug),run_time=.7)
        self.at('The boundary');inner=self.label('inner boundary',[0,-1.5,0],'primary','label');self.play(FadeIn(inner),run_time=.4)
        self.at('Adding a hole');self.at('For a small');eq=self.label('fractional growth = α × ΔT',[0,-2.65,0],'ink','claim').scale(.82);self.play(FadeIn(eq),run_time=.6)
        self.at('The inner');self.at('Our animation');self.at('Now compare');self.play(FadeOut(inner),scale.animate.set_value(1),run_time=.7)
        ball=self.bead(1.025,'primary').move_to(center);self.play(FadeIn(ball),run_time=.6)
        self.at('A small clearance');self.play(scale.animate.set_value(1.18),run_time=2);gap=self.label('ring grows • ball stays cool',[0,-1.55,0],'primary','label').scale(.85);self.play(FadeIn(gap),run_time=.4)
        self.at('This assumes');self.at('Sometimes understanding');self.finish()
