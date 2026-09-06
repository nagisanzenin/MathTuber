from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent']
        def txt(s,p,role='label',color='ink'):return self.label(s,p,color,role)
        def dot(p):return Circle(radius=.19,fill_color=TEAL,fill_opacity=1,stroke_color=INK,stroke_width=2).move_to(p)
        xs=[-2.3,0,2.3]
        jars=VGroup(*[VGroup(Line([x-.7,3.4,0],[x-.7,1.6,0]),Arc(radius=.7,start_angle=PI,angle=PI).move_to([x,1.6,0]),Line([x+.7,1.6,0],[x+.7,3.4,0])).set_color(INK) for x in xs])
        names=VGroup(*[txt(n,[x,4.1,0],'claim') for x,n in zip(xs,['A','B','C'])])
        beads=VGroup(*[dot(p) for p in [[-2.55,2,0],[-2.05,2,0],[0,2,0],[2.3,2,0]]])
        self.add(jars,names,beads)
        self.at('Four identical');self.play(LaggedStart(*[Indicate(b,color=GOLD) for b in beads],lag_ratio=.2),run_time=1)
        self.at('Two here');counts=txt('(2, 1, 1)',[0,.3,0],'claim');self.play(FadeIn(counts),run_time=.5)
        self.at('Moving a counter');self.play(beads[1].animate.move_to([.5,2,0]),run_time=.7);counts=self.replace_label(counts,txt('(1, 2, 1)',[0,.3,0],'claim'));self.wait(.4);self.play(beads[1].animate.move_to([-2.05,2,0]),run_time=.7);counts=self.replace_label(counts,txt('(2, 1, 1)',[0,.3,0],'claim'))
        self.at('We care');self.at('Let us turn');slots=[np.array([-2.5+i,2.3,0]) for i in range(6)];self.play(*[beads[k].animate.move_to(slots[i]) for k,i in enumerate([0,1,3,5])],jars.animate.set_stroke(opacity=.2),run_time=1)
        self.at('Keep the counters');bars=VGroup(*[Line(slots[i]+UP*.45,slots[i]+DOWN*.45,color=CORAL,stroke_width=6) for i in [2,4]]);self.play(Create(bars),run_time=.8)
        self.at('Two counters');self.play(Indicate(beads[:2],color=GOLD),run_time=.8)
        self.at('Now the jars');self.play(FadeOut(jars),FadeOut(names),run_time=.6);heading=txt('one row remembers one share',[0,4.5,0],'claim');self.play(FadeIn(heading),run_time=.5)
        def row(positions,values):
         free=[i for i in range(6) if i not in positions]
         self.play(*[bars[k].animate.move_to(slots[i]) for k,i in enumerate(positions)],*[beads[k].animate.move_to(slots[i]) for k,i in enumerate(free)],run_time=.9)
         return self.replace_label(counts,txt(values,[0,.3,0],'claim'))
        self.at('Slide a divider');counts=row([0,4],'(0, 3, 1)')
        self.at('Put the dividers');counts=row([2,3],'(2, 0, 2)')
        self.at('Every arrangement');self.at('There are six');frames=VGroup(*[RoundedRectangle(width=.86,height=1.15,corner_radius=.1,stroke_color=INK,stroke_width=1.3).move_to(p) for p in slots]);self.play(Create(frames),run_time=.7)
        self.at('Choose two');self.play(Indicate(bars,color=GOLD),run_time=.8)
        self.at('Six choices');formula=txt('6 × 5 = 30',[0,-1.2,0],'claim');self.play(FadeIn(formula),run_time=.5)
        self.at('But choosing');arrows=VGroup(CurvedArrow(slots[2]+UP*.8,slots[3]+UP*.8,color=CORAL),CurvedArrow(slots[3]+DOWN*.8,slots[2]+DOWN*.8,color=CORAL));self.play(Create(arrows),run_time=.8)
        self.at('Divide by two');formula=self.replace_label(formula,txt('30 ÷ 2 = 15 shares',[0,-1.2,0],'claim'));self.play(FadeOut(arrows),run_time=.4)
        self.at('Each row');self.play(FadeOut(VGroup(beads,bars,frames,counts,heading)),run_time=.5)
        allrows=[]
        from itertools import combinations
        for n,(a,b) in enumerate(combinations(range(6),2)):
         symbols=VGroup(*[Line(UP*.15,DOWN*.15,color=CORAL,stroke_width=3) if i in (a,b) else Circle(radius=.06,fill_color=TEAL,fill_opacity=1,stroke_width=0) for i in range(6)]).arrange(RIGHT,buff=.1).move_to([-2.15+(n%3)*2.15,4.1-(n//3)*.85,0]);allrows.append(symbols)
        gallery=VGroup(*allrows);self.play(LaggedStart(*[FadeIn(x) for x in gallery],lag_ratio=.05),run_time=1.2)
        self.at('That is why');self.at('The trick');label=txt('stars and bars',[0,-2.4,0],'claim');self.play(FadeIn(label),run_time=.5)
        self.at('What if every');self.play(FadeOut(VGroup(gallery,formula,label)),run_time=.5);self.add(jars.set_stroke(opacity=1),names);condition=txt('at least one in every jar',[0,5,0],'claim');self.play(FadeIn(condition),run_time=.5)
        self.at('Give each jar');fixed=VGroup(*[dot([x,2,0]) for x in xs]);extra=dot([0,.1,0]);self.play(FadeIn(fixed),FadeIn(extra),run_time=.7)
        self.at('It can go');self.play(extra.animate.move_to([-1.85,2,0]),run_time=.6);self.wait(.3);self.play(extra.animate.move_to([.45,2,0]),run_time=.6);self.wait(.3);self.play(extra.animate.move_to([2.75,2,0]),run_time=.6);answer=txt('(2,1,1)   (1,2,1)   (1,1,2)',[0,-1.1,0]);self.play(FadeIn(answer),run_time=.5)
        self.at('A small change in the rules');self.finish()
