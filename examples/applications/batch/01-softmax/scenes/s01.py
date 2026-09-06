from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        def shares(v):
         return VGroup(Rectangle(width=5*v,height=.65,fill_color=TEAL,fill_opacity=1,stroke_width=0).move_to([-2.5+2.5*v,.8,0]),Rectangle(width=5*(1-v),height=.65,fill_color=CORAL,fill_opacity=1,stroke_width=0).move_to([2.5*v,.8,0]))
        scores=txt('scores: 1     2',[0,4.3,0],'claim');bar=shares(1/(1+np.e));names=txt('first                 second',[0,1.7,0]);self.add(scores,bar,names)
        self.at('These two');self.play(Indicate(bar,color=GOLD),run_time=.7)
        self.at('A machine learning');rule=txt('softmax',[0,5.4,0],'claim');self.play(FadeIn(rule),run_time=.5)
        self.at('Exponentiate');formula=txt('share = exp(score) / total weight',[0,3,0]);self.play(FadeIn(formula),run_time=.5)
        self.at('For scores');result=txt('≈ 27%                  ≈ 73%',[0,-.25,0]);self.play(FadeIn(result),run_time=.5)
        self.at('Now add');self.remove(scores);scores=txt('scores: 1000     1001',[0,4.3,0],'claim');self.add(scores);shift=txt('+999 to both',[0,-1.6,0]);self.play(FadeIn(shift),run_time=.6)
        self.at('The new scores');self.at('Do the shares');self.play(Indicate(bar,color=GOLD),run_time=.7)
        self.at('They do not');self.at('Adding the same');self.play(FadeOut(formula),FadeOut(shift),run_time=.5);factor=txt('exp(x + c) = exp(c) × exp(x)',[0,3,0]);self.play(FadeIn(factor),run_time=.5)
        self.at('That factor');cancel=txt('same factor in top and bottom',[0,-1.6,0]);self.play(FadeIn(cancel),run_time=.6)
        self.at('But a computer');self.play(FadeOut(VGroup(factor,cancel)),run_time=.5)
        self.at('In ordinary');warning=txt('exp(1000): overflow in float64',[0,3,0]);self.play(FadeIn(warning),run_time=.5)
        self.at('We can subtract');self.play(FadeOut(warning),run_time=.4);shift=txt('subtract the maximum',[0,3,0]);self.play(FadeIn(shift),run_time=.5)
        self.at('Our scores');scores=self.replace_label(scores,txt('scores: −1     0',[0,4.3,0],'claim'))
        self.at('The weights');weights=txt('weights: ≈ 0.368     1',[0,2.2,0]);self.play(FadeIn(weights),run_time=.5)
        self.at('Divide by their total. The original');calc=txt('0.368 / 1.368     1 / 1.368',[0,-1.6,0]);self.play(FadeIn(calc),Indicate(bar,color=GOLD),run_time=.7)
        self.at('This rewrite');self.at('It avoids');self.at('Try one different');self.play(FadeOut(VGroup(shift,weights,calc)),run_time=.5);scores=self.replace_label(scores,txt('scores: 1     2',[0,4.3,0],'claim'));gap=txt('gap = 1',[0,3,0]);self.play(FadeIn(gap),run_time=.5)
        self.at('This time');self.play(FadeOut(result),FadeOut(gap),run_time=.2);scores=self.replace_label(scores,txt('scores: 1     3',[0,4.3,0],'claim'));self.play(Transform(bar,shares(1/(1+np.exp(2)))),run_time=.8)
        self.at('Now the gap');gap=txt('gap = 2',[0,3,0]);result=txt('≈ 12%                  ≈ 88%',[0,-.25,0]);self.play(FadeIn(gap),FadeIn(result),run_time=.5)
        self.at('A common shift');ending=txt('shared shift: unchanged\nchanged gap: changed shares',[0,-1.8,0]);self.play(FadeIn(ending),run_time=.7);self.finish()
