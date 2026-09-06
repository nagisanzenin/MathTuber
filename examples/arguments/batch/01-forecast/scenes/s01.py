from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        axis=NumberLine(x_range=[0,1,.2],length=5,include_numbers=True,font_size=24,color=INK).move_to([0,3.5,0]);dot=Dot(axis.n2p(.8),color=TEAL,radius=.12);title=txt('forecast probability',[0,5,0],'claim');axis.numbers.set_color(INK);self.add(axis,dot,title)
        self.at('A forecast can');self.focus_outline(dot,run_time=.6)
        self.at('Suppose rain');truth=txt('true chance: 0.8',[0,2.5,0]);self.play(FadeIn(truth),run_time=.4)
        self.at('The outcome');out=txt('rain: 1       no rain: 0',[0,1.2,0]);self.play(FadeIn(out),run_time=.4)
        self.at('Square the distance');rule=txt('score = (forecast − outcome)²',[0,-.2,0]);self.play(FadeIn(rule),run_time=.5)
        self.at('At eighty');errors=txt('rain: 0.04       dry: 0.64',[0,-1.4,0]);self.play(FadeIn(errors),run_time=.5)
        self.at('Weight those');calc=txt('0.8 × 0.04 + 0.2 × 0.64',[0,-2.6,0]);self.play(FadeIn(calc),run_time=.5)
        self.at('The expected');calc=self.replace_label(calc,txt('expected score = 0.16',[0,-2.6,0],'claim'))
        self.at('Announcing certainty');self.play(FadeOut(errors),FadeOut(calc),dot.animate.move_to(axis.n2p(1)),run_time=.6);errors=txt('rain: 0       dry: 1',[0,-1.4,0]);calc=txt('expected score = 0.20',[0,-2.6,0],'claim');self.play(FadeIn(errors),FadeIn(calc),run_time=.5)
        self.at('Here is the whole');self.play(FadeOut(VGroup(axis,dot,title,truth,out,rule,errors,calc)),run_time=.5)
        ax=Axes(x_range=[0,1,.2],y_range=[0,1,.2],x_length=5,y_length=4,axis_config={'color':INK,'include_tip':False}).move_to([0,2,0]);curve=ax.plot(lambda p:.16+(p-.8)**2,color=TEAL);minimum=Dot(ax.c2p(.8,.16),color=CORAL);labels=VGroup(txt('forecast: 0 → 1',[0,-.6,0]),txt('expected score',[0,5,0],'claim'));self.play(Create(ax),Create(curve),FadeIn(minimum),FadeIn(labels),run_time=1)
        self.at('It equals');eq=txt('0.16 + (forecast − 0.8)²',[0,-1.9,0],'claim');self.play(FadeIn(eq),run_time=.5)
        self.at('That extra');self.focus_outline(minimum,run_time=.6)
        self.at('Now suppose');self.play(FadeOut(eq),run_time=.2);self.play(Transform(curve,ax.plot(lambda p:.25+(p-.5)**2,color=TEAL)),minimum.animate.move_to(ax.c2p(.5,.25)),run_time=.8)
        self.at('The bottom');eq=txt('0.25 + (forecast − 0.5)²',[0,-1.9,0],'claim');self.play(FadeIn(eq),run_time=.5)
        self.at('This binary');self.finish()
