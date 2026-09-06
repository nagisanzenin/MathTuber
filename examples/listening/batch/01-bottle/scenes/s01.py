from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];WATER='#91B9B1'
        water=ValueTracker(0);clock=self.process_clock(rate=.8);rate=ValueTracker(1);phase=ValueTracker(0)
        body=RoundedRectangle(width=2.8,height=3.3,corner_radius=.45,stroke_color=INK,stroke_width=3,fill_color='#DCE4D6',fill_opacity=.4).move_to([0,1.3,0]);neck=Rectangle(width=.72,height=1,stroke_color=INK,stroke_width=3,fill_color=self.palette['background'],fill_opacity=1).move_to([0,3.35,0]);lip=Ellipse(width=.85,height=.16,stroke_color=INK,stroke_width=2).move_to([0,3.85,0]);base=Line([-2,-.42,0],[2,-.42,0],color='#BBA98C',stroke_width=3)
        liquid=always_redraw(lambda:Rectangle(width=2.5,height=max(.001,water.get_value()*2.8),fill_color=WATER,fill_opacity=.75,stroke_width=0).move_to([0,-.1+water.get_value()*1.4,0]))
        plug=always_redraw(lambda:RoundedRectangle(width=.57,height=.28,corner_radius=.05,fill_color=CORAL,fill_opacity=.65,stroke_width=0).move_to([0,3.35+.12*np.sin(TAU*clock.value),0]))
        self.add(body,liquid,neck,lip,base,plug);slow=self.label('schematic • neck motion slowed',[0,4.6,0]).scale(.75);self.add(slow)
        note=always_redraw(lambda:self.label(f'{220/np.sqrt(1-water.get_value()):.0f} Hz',[0,-1.3,0],role='claim'));self.add(note)
        self.at('An empty bottle');self.at('This gentle tone');self.at('Listen before');self.wait(self.listen('full'))
        self.at('The air near');mark=Arrow([1.9,3.35,0],[.45,3.35,0],buff=.1,color=CORAL);self.play(Create(mark),run_time=.6)
        self.at('The air in');compression=VGroup(*[Line([-.8,y,0],[.8,y,0],color=TEAL,stroke_width=2) for y in [.2,.6,1,1.4,1.8,2.2]]);self.play(FadeIn(compression),run_time=.5);self.play(compression.animate.stretch(.8,1),run_time=.7);self.play(compression.animate.stretch(1.25,1),run_time=.7)
        self.at('Together, they');self.play(FadeOut(mark),FadeOut(compression),run_time=.5)
        self.at('Keep the neck');self.play(water.animate.set_value(.75),run_time=2.3);self.at('The remaining air');volume=self.label('air volume: ¼',[0,2.45,0]).scale(.7);self.play(FadeIn(volume),run_time=.5)
        self.at('When only a quarter');self.wait(.5)
        self.at('Here, two hundred');comparison=self.label('¼ volume  →  2 × frequency',[0,-2.4,0],role='claim').scale(.85);self.play(FadeIn(comparison),run_time=.6)
        self.at('These are synthesized');self.at('Hear the larger');self.play(water.animate.set_value(0),FadeOut(volume),run_time=.6);self.wait(self.listen('return-full'));self.play(water.animate.set_value(.75),run_time=.6);self.wait(self.listen('quarter'));self.play(FadeIn(volume),run_time=.4)
        self.at('The rule is');formula=self.label('f ∝ 1 / √V',[0,-3.4,0],role='claim');self.play(FadeIn(formula),run_time=.5)
        self.at('It assumes small');self.at('Real neck shape');self.at('A little empty');self.finish()
