from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        def water(v):return Rectangle(width=2.5,height=4*v/100,fill_color=TEAL,fill_opacity=.65,stroke_width=0).move_to([0,2*v/100,0])
        vessel=VGroup(Line([-1.3,4.3,0],[-1.3,0,0]),Line([-1.3,0,0],[1.3,0,0]),Line([1.3,0,0],[1.3,4.3,0])).set_color(INK)
        level=water(100);label=txt('100 units',[0,5,0],'claim');self.add(vessel,level,label)
        self.at('Take away');self.play(Indicate(level,color=GOLD),run_time=.7)
        self.at('Begin with');self.at('Removing twenty');self.remove(label);self.play(Transform(level,water(80)),run_time=.8);label=txt('80 units',[0,5,0],'claim');self.add(label);op=txt('−20% of 100 = −20',[0,-1.2,0]);self.play(FadeIn(op),run_time=.5)
        self.at('Now add');op=self.replace_label(op,txt('+20% of 80 = +16',[0,-1.2,0]));self.remove(label);self.play(Transform(level,water(96)),run_time=.8);label=txt('96 units',[0,5,0],'claim');self.add(label)
        self.at('Twenty percent of eighty');self.at('The percentages');reference=DashedLine([-1.7,4,0],[1.7,4,0],color=CORAL);self.play(Create(reference),run_time=.6)
        self.at('We can see');self.play(FadeOut(op),run_time=.4)
        self.at('The first operation');factor=txt('× 0.8',[0,-1.2,0],'claim');self.play(FadeIn(factor),run_time=.5)
        self.at('The second multiplies');factor=self.replace_label(factor,txt('× 0.8 × 1.2',[0,-1.2,0],'claim'))
        self.at('Their product');factor=self.replace_label(factor,txt('0.8 × 1.2 = 0.96',[0,-1.2,0],'claim'))
        self.at('To restore');self.remove(label);self.play(Transform(level,water(80)),FadeOut(factor),run_time=.7);label=txt('80 units',[0,5,0],'claim');self.add(label);restore=txt('need +20 units',[0,-1.2,0],'claim');self.play(FadeIn(restore),run_time=.5)
        self.at('Twenty is one quarter');restore=self.replace_label(restore,txt('20 / 80 = 1/4 = 25%',[0,-1.2,0],'claim'))
        self.at('So reversing');self.remove(label);self.play(Transform(level,water(100)),run_time=.8);label=txt('100 units restored',[0,5,0],'claim');self.add(label)
        self.at('In general');self.at('This assumes');self.at('Try a larger');self.play(FadeOut(label),FadeOut(restore),run_time=.2);self.play(Transform(level,water(50)),run_time=.8);label=txt('50 units',[0,5,0],'claim');self.add(label)
        self.at('Fifty units remain');question=txt('what increase restores 100?',[0,-1.2,0]);self.play(FadeIn(question),run_time=.5)
        self.at('We need another');self.remove(label,question);self.play(Transform(level,water(100)),run_time=.8);label=txt('100 units restored',[0,5,0],'claim');self.add(label);answer=txt('50 / 50 = 100% increase',[0,-1.2,0],'claim');self.play(FadeIn(answer),run_time=.5)
        self.at('Before comparing');self.finish()
