from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];removed=ValueTracker(0)
        xs=[-2.4,-.8,.8,2.4]
        def bars():
            group=VGroup()
            for j,x in enumerate(xs):
                strength=1-removed.get_value() if j==0 else 1;group.add(Rectangle(width=.5,height=max(.002,strength),fill_color=CORAL if j==0 else TEAL,fill_opacity=.8,stroke_width=0).move_to([x,2.2+strength/2,0]));group.add(self.label(str(220*(j+1)),[x,1.75,0]).scale(.8))
            return group
        self.add(always_redraw(bars));hz=self.label('frequency components • Hz',[0,4.2,0]).scale(.8);self.add(hz)
        def value(x):
            phase=(x+3)/3;return .38*np.sqrt(4/(4-removed.get_value()))*((1-removed.get_value())*np.sin(TAU*phase)+sum(np.sin(TAU*n*phase) for n in [2,3,4]))-.4
        curve=always_redraw(lambda:VMobject().set_points_as_corners([[x,value(x),0] for x in np.linspace(-3,3,401)]).set_stroke(INK,3));self.add(Line([-3.2,-.4,0],[3.2,-.4,0],color='#B6B39E',stroke_width=1),curve)
        status=always_redraw(lambda:self.label('all four present' if removed.get_value()<.01 else 'no 220 Hz component' if removed.get_value()>.99 else 'removing 220 Hz',[0,-3.4,0]).scale(.85));self.add(status)
        def compare(a,b):
            removed.set_value(0);self.wait(self.listen(a));self.play(removed.animate.set_value(1),run_time=.4);self.wait(self.listen(b))
        self.at('This sound contains');self.at('We will remove');self.at('The sound changes');compare('all','missing')
        self.at('The first mixture');self.play(removed.animate.set_value(0),run_time=.4);self.at('The second contains');self.play(removed.animate.set_value(1),run_time=.4);self.at('There is no');self.wait(.5)
        self.at('Yet its whole pattern');guides=VGroup(*[DashedLine([x,-1.8,0],[x,1.1,0],color=CORAL,stroke_width=2) for x in [-3,0,3]]);self.play(FadeIn(guides),run_time=.6)
        self.at('Two, three, and four');span=DoubleArrow([-3,-2.2,0],[0,-2.2,0],buff=0,color=TEAL);period=self.label('1 / 220 second',[-1.5,-2.7,0]).scale(.8);self.play(Create(span),FadeIn(period),run_time=.6)
        self.at('Our sense of pitch');self.at('This is called');self.at('It separates');self.at('Compare the two');self.play(FadeOut(status),run_time=.3);compare('all-again','missing-again')
        self.at('The shapes differ');note=self.label('same repeating interval',[0,-3.5,0]).scale(.85);self.play(FadeIn(note),run_time=.5)
        self.at('Listeners and playback');self.at('You do not have');self.at('Sometimes a relationship');self.finish()
