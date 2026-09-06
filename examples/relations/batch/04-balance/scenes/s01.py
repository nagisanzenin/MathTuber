from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary']
        def txt(s,p,role='label',color='ink'):return self.label(s,p,color,role)
        A=np.array([-2.1,3.1,0]);B=np.array([2.1,3.1,0]);nodes=VGroup(*[VGroup(Circle(radius=.65,color=INK,stroke_width=2),txt(n,[0,0,0],'claim')).move_to(p) for n,p in [('A',A),('B',B)]]);dot=Dot(A+DOWN*.32,radius=.09,color=CORAL);pathlabel=txt('one possible path',[0,1.8,0]);self.add(nodes,dot,pathlabel)
        self.at('This dot');self.play(dot.animate.move_to(B+DOWN*.32),run_time=.8);self.play(dot.animate.move_to(A+DOWN*.32),run_time=.8)
        self.at('At each step');self.at('From A');ab=CurvedArrow(A+UP*.55,B+UP*.55,angle=-PI/3,color=TEAL,stroke_width=3);abl=txt('1/4',[0,4.75,0]);self.play(Create(ab),FadeIn(abl),run_time=.7)
        self.at('From B');ba=CurvedArrow(B+DOWN*.55,A+DOWN*.55,angle=-PI/3,color=CORAL,stroke_width=3);bal=txt('1/2',[0,1.4,0]);self.play(FadeOut(pathlabel),Create(ba),FadeIn(bal),run_time=.7)
        self.at('Otherwise');stay=VGroup(txt('stay: 3/4',[-2.1,5.2,0]),txt('stay: 1/2',[2.1,5.2,0]));self.play(FadeIn(stay),run_time=.5)
        self.at('Now follow');self.play(FadeOut(dot),run_time=.4);probhead=txt('probability mass · total = 1',[0,.1,0],'claim');self.play(FadeIn(probhead),run_time=.5)
        self.at('Suppose the chance');# Four sixths in A, two sixths in B; split into stayed and exchanged portions.
        parts=VGroup(Rectangle(width=3,height=.8,fill_color=TEAL,fill_opacity=.45,stroke_color=INK,stroke_width=1.5).move_to([-1.5,-1.3,0]),Rectangle(width=1,height=.8,fill_color=TEAL,fill_opacity=.75,stroke_color=INK,stroke_width=1.5).move_to([.5,-1.3,0]),Rectangle(width=1,height=.8,fill_color=CORAL,fill_opacity=.75,stroke_color=INK,stroke_width=1.5).move_to([1.5,-1.3,0]),Rectangle(width=1,height=.8,fill_color=CORAL,fill_opacity=.45,stroke_color=INK,stroke_width=1.5).move_to([2.5,-1.3,0]));plabels=VGroup(txt('A: 2/3',[-1,-2.55,0],'claim'),txt('B: 1/3',[2,-2.55,0],'claim'));self.play(FadeIn(parts),FadeIn(plabels),run_time=.7)
        self.at('One quarter of the probability');one=txt('(2/3) × (1/4) = 1/6',[0,-3.3,0]);self.play(Circumscribe(parts[1],color=TEAL),FadeIn(one),run_time=.8)
        self.at('Half of the B');one=self.replace_label(one,txt('(1/3) × (1/2) = 1/6',[0,-3.3,0]));self.play(Circumscribe(parts[2],color=CORAL),run_time=.8)
        self.at('Equal probability');self.play(FadeOut(one),run_time=.3);self.play(parts[1].animate(path_arc=PI).move_to([1.5,-1.3,0]),parts[2].animate(path_arc=PI).move_to([.5,-1.3,0]),run_time=1.5);self.play(parts[1].animate.set_fill(CORAL),parts[2].animate.set_fill(TEAL),run_time=.3)
        self.at('That is a stationary');stationary=txt('same totals after one step',[0,-3.3,0]);self.play(FadeIn(stationary),run_time=.4)
        self.at('It does not mean');self.add(dot);self.play(dot.animate.move_to(B+DOWN*.32),run_time=.7)
        self.at('It means');self.at('Will a different');self.play(FadeOut(VGroup(parts,plabels,stationary,dot)),run_time=.5)
        tracker=ValueTracker(1);bar=always_redraw(lambda: VGroup(Rectangle(width=max(.0001,6*tracker.get_value()),height=.8,fill_color=TEAL,fill_opacity=.55,stroke_width=0).move_to([-3+3*tracker.get_value(),-1.3,0]),Rectangle(width=max(.0001,6*(1-tracker.get_value())),height=.8,fill_color=CORAL,fill_opacity=.55,stroke_width=0).move_to([3*tracker.get_value(),-1.3,0])));outline=Rectangle(width=6,height=.8,stroke_color=INK,stroke_width=2).move_to([0,-1.3,0]);target=DashedLine([1,-.6,0],[1,-2,0],color=INK,stroke_width=2);targetlabel=txt('target P(A) = 2/3',[.6,-2.7,0]);state_labels=VGroup(txt('A',[-2.7,-2.05,0]),txt('B',[2.7,-2.05,0]));self.add(bar,outline,target,targetlabel,state_labels)
        self.at('Start in state A');step=txt('step 0 · P(A) = 1',[0,-3.5,0]);self.play(FadeIn(step),run_time=.4)
        self.at('After one step');self.play(FadeOut(step),run_time=.15);self.play(tracker.animate.set_value(.75),run_time=.55);step=txt('step 1 · P(A) = 3/4',[0,-3.5,0]);self.play(FadeIn(step),run_time=.4)
        self.at('After two steps');self.play(FadeOut(step),run_time=.15);self.play(tracker.animate.set_value(11/16),run_time=.55);step=txt('step 2 · P(A) = 11/16',[0,-3.5,0]);self.play(FadeIn(step),run_time=.4)
        self.at('Call the current');self.play(FadeOut(VGroup(nodes,ab,ba,abl,bal,stay)),run_time=.5);pdef=txt('p = current probability of A',[0,4.7,0],'claim');self.play(FadeIn(pdef),run_time=.4)
        self.at('Next time');eq=txt('p′ = (3/4)p + (1/2)(1−p)',[0,3.3,0],'claim');self.play(FadeIn(eq),run_time=.6)
        self.at('That is one half');simple=txt('p′ = 1/2 + p/4',[0,2.1,0],'claim');self.play(FadeIn(simple),run_time=.4)
        self.at('Subtract two thirds');gap=txt('p′ − 2/3 = (p − 2/3)/4',[0,.95,0],'claim');self.play(FadeIn(gap),run_time=.5)
        self.at('So this chain');self.play(FadeOut(step),run_time=.3);self.play(tracker.animate.set_value(2/3),run_time=1.4);limit=txt('approaches 2/3',[0,-3.5,0]);self.play(FadeIn(limit),run_time=.4)
        self.at('This conclusion');self.play(FadeOut(VGroup(pdef,eq,simple,gap)),run_time=.4);self.play(FadeIn(VGroup(nodes,ab,ba,abl,bal,stay)),run_time=.5);self.at('The motion can');path_scope=txt('one possible path',[0,.8,0]);self.add(dot,path_scope);self.play(dot.animate.move_to(A+DOWN*.32),run_time=.7);self.play(dot.animate.move_to(B+DOWN*.32),run_time=.7);self.finish()
