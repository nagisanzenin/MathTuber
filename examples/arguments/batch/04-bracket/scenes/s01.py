from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        ax=Axes(x_range=[1,2,.25],y_range=[-1,6,1],x_length=5,y_length=4,axis_config={'color':INK,'include_tip':False}).move_to([0,2,0]);curve=ax.plot(lambda x:x**3-2,color=TEAL);title=txt('x³ − 2',[0,5.4,0],'claim');self.add(ax,curve,title)
        def bracket(a,b):return VGroup(Line(ax.c2p(a,0),ax.c2p(b,0),stroke_width=8,color=GOLD),Dot(ax.c2p(a,0),color=CORAL),Dot(ax.c2p(b,0),color=CORAL))
        band=bracket(1,2);info=txt('bracket: 1 to 2',[0,-.8,0],'claim');self.add(band,info)
        self.at('We want');self.at('At one');self.at('Keep a bracket');self.focus_outline(band,run_time=.6)
        self.at('Because the curve');self.at('Test the middle');dot=Dot(ax.c2p(1.5,1.5**3-2),color=CORAL);self.play(FadeIn(dot),run_time=.4);self.play(Transform(band,bracket(1,1.5)),run_time=.7);info=self.replace_label(info,txt('bracket: 1 to 1.5',[0,-.8,0],'claim'))
        self.at('The next middle');self.play(dot.animate.move_to(ax.c2p(1.25,1.25**3-2)),Transform(band,bracket(1.25,1.5)),run_time=.8);info=self.replace_label(info,txt('bracket: 1.25 to 1.5',[0,-.8,0],'claim'))
        self.at('Two more tests');self.play(FadeOut(info),run_time=.2)
        for m in [1.375,1.3125]:
         self.play(dot.animate.move_to(ax.c2p(m,m**3-2)),Transform(band,bracket(1.25,m)),run_time=.7)
        self.at('Each test');rule=txt('keep opposite signs · halve width',[0,-2,0]);self.play(FadeIn(rule),run_time=.5)
        self.at('After four');info=txt('1.25 < root < 1.3125',[0,-.8,0],'claim');self.play(FadeIn(info),run_time=.5)
        self.at('The interval is one sixteenth');width=txt('width: 1/16',[0,-3.2,0]);self.play(FadeIn(width),run_time=.5)
        self.at('Choosing its midpoint');width=self.replace_label(width,txt('midpoint error ≤ 1/32',[0,-3.2,0]))
        self.at('Now replace');self.play(FadeOut(VGroup(curve,band,dot,info,rule,width)),run_time=.4);jump=VGroup(Line(ax.c2p(1,-1),ax.c2p(1.3,-1),color=TEAL),Line(ax.c2p(1.3,1),ax.c2p(2,1),color=TEAL));self.play(Create(jump),run_time=.7);title=self.replace_label(title,txt('a discontinuous jump',[0,5.4,0],'claim'))
        self.at('The signs still');note=txt('opposite signs · no zero',[0,-1.3,0],'claim');self.play(FadeIn(note),run_time=.5)
        self.at('Continuity was');self.finish()
