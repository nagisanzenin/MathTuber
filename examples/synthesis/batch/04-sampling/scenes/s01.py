from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        pos=[-2,0,2];cards=VGroup(*[RoundedRectangle(width=1.5,height=1.5,corner_radius=.1,stroke_color=TEAL).move_to([x,3.6,0]) for x in pos]);vals=VGroup(*[txt(str(v),[x,3.6,0],'claim') for x,v in zip(pos,[2,4,6])]);title=txt('true total: 12',[0,5.5,0],'claim');self.add(cards,vals,title)
        self.at('A sample can');self.at('Imagine three');self.at('Choose exactly');probs=VGroup(*[txt(s,[x,2.2,0]) for x,s in zip(pos,['1/2','1/4','1/4'])]);self.play(FadeIn(probs),run_time=.5)
        self.at('The observed value alone');calc=txt('average observed value: 3.5',[0,.5,0]);self.play(FadeIn(calc),run_time=.5)
        self.at('Instead divide');self.play(FadeOut(calc),run_time=.2);rule=txt('estimate = value / inclusion chance',[0,.5,0]);self.play(FadeIn(rule),run_time=.5)
        self.at('The possible');est=VGroup(*[txt(str(v),[x,-.8,0],'claim') for x,v in zip(pos,[4,16,24])]);self.play(FadeIn(est),run_time=.5)
        self.at('Weight these');calc=txt('½ × 4 + ¼ × 16 + ¼ × 24 = 12',[0,-2.2,0]);self.play(FadeIn(calc),run_time=.5)
        self.at('Each item contributes');self.at('In expectation');calc=self.replace_label(calc,txt('chance × (value / chance) = value',[0,-2.2,0]))
        self.at('Now make');self.play(FadeOut(VGroup(rule,est,calc,probs)),run_time=.3);self.play(cards[2].animate.set_stroke(CORAL),vals[2].animate.set_opacity(.15),run_time=.5);probs=VGroup(*[txt(s,[x,2.2,0]) for x,s in zip(pos,['1/2','1/2','0'])]);self.add(probs)
        self.at('No finite');note=txt('inclusion chance 0: information missing',[0,.2,0]);self.play(FadeIn(note),run_time=.5)
        self.at('Known positive');end=txt('unbiased ≠ exact in every sample',[0,-1.5,0],'claim');self.play(FadeIn(end),run_time=.5);self.finish()
