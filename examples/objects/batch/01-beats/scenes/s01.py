from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        clock=self.process_clock(rate=1);clock.pause();phase=ValueTracker(0)
        def fork(x,col):
         return VGroup(Line([x-.33,3.5,0],[x-.33,2.2,0],color=self.palette[col],stroke_width=6),Line([x+.33,3.5,0],[x+.33,2.2,0],color=self.palette[col],stroke_width=6),Arc(radius=.33,start_angle=PI,angle=PI,color=self.palette[col],stroke_width=6).move_to([x,2.2,0]),Line([x,1.9,0],[x,1.2,0],color=self.palette['ink'],stroke_width=5))
        f1=fork(-1.5,'primary');f2=fork(1.5,'secondary');self.add(f1,f2)
        # Audible envelope in real seconds; slow explanatory oscillations introduced separately.
        windows=json.loads((Path(__file__).resolve().parents[1]/'assets/sound-design.json').read_text())['windows'];t0=windows[0]['start']
        pulse=always_redraw(lambda:Circle(radius=.38+.35*abs(math.cos(PI*max(0,self.renderer.time-t0))),color=self.palette['primary'],fill_color=self.palette['primary'],fill_opacity=.12+.3*abs(math.cos(PI*max(0,self.renderer.time-t0)))).move_to([0,.1,0]))
        self.at('Two steady notes');self.add(pulse)
        self.at('Here are two');self.wait(.2)
        self.at('Listen for the slow');self.wait(.2)
        self.at('Neither note');self.remove(pulse)
        xs=np.linspace(-2.8,2.8,160)
        def wave(y,offset,col):return VMobject(color=self.palette[col],stroke_width=4).set_points_smoothly([[x,y+.35*math.sin(2*PI*(x/2.8-clock.value*.3)+offset),0] for x in xs])
        clock.resume();w1=always_redraw(lambda:wave(.5,0,'primary'));w2=always_redraw(lambda:wave(-.7,-phase.get_value(),'secondary'));self.play(FadeIn(w1),FadeIn(w2),run_time=.7)
        summed=always_redraw(lambda:VMobject(color=self.palette['ink'],stroke_width=4).set_points_smoothly([[x,-1.7+.35*(math.sin(2*PI*(x/2.8-clock.value*.3))+math.sin(2*PI*(x/2.8-clock.value*.3)-phase.get_value())),0] for x in xs]));self.add(summed)
        self.at('Their vibrations');self.play(phase.animate.set_value(2*PI),run_time=2.5,rate_func=linear)
        self.at('When they agree');clock.pause();phase.set_value(0);tag=self.label('pushes add',[0,-2.9,0],'ink','label');self.play(FadeIn(tag),run_time=.5)
        self.at('When they oppose');self.play(phase.animate.set_value(PI),FadeOut(tag),run_time=.8);tag=self.label('opposing pushes cancel',[0,-2.9,0],'ink','label');self.play(FadeIn(tag),run_time=.4);clock.resume()
        self.at('We have slowed');self.play(FadeOut(tag),run_time=.3);phase.add_updater(lambda m:m.set_value(clock.value*.6));self.add(phase);slow=self.label('schematic waves • slow alignment',[0,4.8,0],'muted','label');slow.scale(.75);self.play(FadeIn(slow),run_time=.5)
        self.at('The sound itself');self.wait(.2)
        self.at('One note is');a=self.label('220 Hz',[-1.5,4,0],'primary','label');self.play(FadeIn(a),run_time=.4)
        self.at('The other is');b=self.label('221 Hz',[1.5,4,0],'secondary','label');self.play(FadeIn(b),run_time=.4)
        self.at('It gains one');self.play(FadeOut(tag),run_time=.3);tag=self.label('one extra cycle per second',[0,-2.9,0],'ink','label');tag.scale(.8);self.play(FadeIn(tag),run_time=.4)
        self.at('So their alignment');self.play(FadeOut(w1),FadeOut(w2),FadeOut(summed),FadeOut(slow),FadeOut(tag),run_time=.5);clock.pause();rule=self.label('221 − 220 = 1 beat / second',[0,-1.4,0],'ink','label');rule.scale(.8);self.play(FadeIn(rule),run_time=.5)
        self.at('That difference');self.wait(.2)
        self.at('Move the second');self.play(FadeOut(b),FadeOut(rule),run_time=.4);b=self.label('220.5 Hz',[1.5,4,0],'secondary','label');self.play(FadeIn(b),run_time=.4)
        self.at('Now the swelling');t1=windows[1]['start'];pulse2=always_redraw(lambda:Circle(radius=.38+.35*abs(math.cos(PI*.5*max(0,self.renderer.time-t1))),color=self.palette['primary'],fill_color=self.palette['primary'],fill_opacity=.12+.3*abs(math.cos(PI*.5*max(0,self.renderer.time-t1)))).move_to([0,-.4,0]));self.add(pulse2)
        self.at('The beat rate');self.remove(pulse2);rule=self.label('beat rate = frequency difference',[0,-1.4,0],'ink','label');rule.scale(.75);self.play(FadeIn(rule),run_time=.4)
        self.at('This is one way');self.wait(.2)
        self.at('As the notes meet');self.play(FadeOut(b),run_time=.3);b=self.label('220 Hz',[1.5,4,0],'secondary','label');self.play(FadeIn(b),run_time=.4)
        self.at('A gentle rhythm');self.finish()
