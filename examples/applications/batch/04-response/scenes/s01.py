from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        def cards(words,y):return VGroup(*[VGroup(RoundedRectangle(width=1.25,height=.8,corner_radius=.1,fill_color=(TEAL if w=='yes' else CORAL),fill_opacity=.25,stroke_color=INK,stroke_width=1),self.lettering(w,'label','ink')).move_to([-2.25+i*1.5,y,0]) for i,w in enumerate(words)])
        rule=cards(['keep','keep','keep','flip'],3.2);self.add(rule)
        self.at('A noisy answer');self.play(Indicate(rule[-1],color=GOLD),run_time=.7)
        self.at('Imagine a yes');self.at('Three times');heading=txt('private random choice',[0,4.8,0],'claim');self.play(FadeIn(heading),run_time=.5)
        self.at('A true yes');self.play(FadeOut(rule),run_time=.4);a=cards(['yes','yes','yes','no'],3.2);al=txt('true yes → reports',[0,4.3,0]);self.play(FadeIn(a),FadeIn(al),FadeOut(heading),run_time=.5)
        self.at('A true no');b=cards(['no','no','no','yes'],.7);bl=txt('true no → reports',[0,1.8,0]);self.play(FadeIn(b),FadeIn(bl),run_time=.5)
        self.at('So a reported');self.play(Indicate(a[0],color=GOLD),Indicate(b[-1],color=GOLD),run_time=.8)
        self.at('Suppose the true');self.play(FadeOut(VGroup(a,b,al,bl)),run_time=.5);title=txt('100 responses: expected counts',[0,5,0],'claim');self.play(FadeIn(title),run_time=.5)
        self.at('Out of one hundred');r1=txt('80 true yes × 3/4 = 60 yes',[0,3.3,0],'claim');self.play(FadeIn(r1),run_time=.5)
        self.at('The twenty');r2=txt('20 true no × 1/4 = 5 yes',[0,1.8,0],'claim');self.play(FadeIn(r2),run_time=.5)
        self.at('Together');total=txt('60 + 5 = 65 expected yes',[0,.2,0],'claim');self.play(FadeIn(total),run_time=.5)
        self.at('We can undo');self.play(FadeOut(VGroup(r1,r2,total)),run_time=.5);title=self.replace_label(title,txt('a group estimate',[0,5,0],'claim'))
        self.at('The expected');eq=txt('expected report = 1/4 + true / 2',[0,3.3,0]);self.play(FadeIn(eq),run_time=.5)
        self.at('Subtract one quarter');calc=txt('2 × (0.65 − 0.25) = 0.80',[0,1.6,0],'claim');self.play(FadeIn(calc),run_time=.5)
        self.at('A finite sample');caution=txt('estimate: random error remains',[0,.1,0]);self.play(FadeIn(caution),run_time=.5)
        self.at('Try a group');self.play(FadeOut(VGroup(eq,calc,caution)),run_time=.5);title=self.replace_label(title,txt('all true answers: no',[0,5,0],'claim'));b=cards(['no','no','no','yes'],2.8);self.play(FadeIn(b),run_time=.6)
        self.at('Would every');self.at('No. One quarter');baseline=txt('expected yes reports: 25%',[0,1.2,0],'claim');self.play(FadeIn(baseline),Indicate(b[-1],color=GOLD),run_time=.7)
        self.at('That baseline');self.at('The method');name=txt('randomized response',[0,-.2,0],'claim');self.play(FadeIn(name),run_time=.5)
        self.at('Repeated reports');self.at('Sometimes we learn');self.finish()
