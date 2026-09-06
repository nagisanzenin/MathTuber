from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];INK=self.palette['ink']
        def txt(s,p,role='claim',color='ink'):return self.label(s,p,color,role)
        def box(title,count,p,color):
            return VGroup(RoundedRectangle(width=2.8,height=1.8,corner_radius=.15,fill_color=self.palette['surface'],fill_opacity=1,stroke_color=self.palette[color],stroke_width=3),txt(title,[0,.45,0],'label'),txt(count,[0,-.35,0],color=color)).move_to(p)
        intro=txt('9 of 10 unwanted messages caught',[0,4.3,0]);self.add(intro)
        mail=VGroup(*[VGroup(Rectangle(width=.85,height=.58,stroke_color=INK,stroke_width=2),Line([-.425,.29,0],[0,0,0],color=INK,stroke_width=2),Line([0,0,0],[.425,.29,0],color=INK,stroke_width=2)).move_to([-2.4+1.2*(i%5),2.5-1.25*(i//5),0]) for i in range(10)]);flags=VGroup(*[Square(side_length=.15,fill_color=TEAL,fill_opacity=1,stroke_width=0).move_to(mail[i].get_corner(UR)) for i in range(9)]);denom=txt('all ten are unwanted',[0,.1,0],'label')
        self.at('Your message filter');self.play(FadeIn(mail),FadeIn(denom),run_time=.6);self.play(LaggedStart(*[FadeIn(f) for f in flags],lag_ratio=.06),run_time=1)
        self.at('That sounds');self.at('But when it');question=txt('Is a flag usually right?',[0,-1.4,0]);self.play(FadeIn(question),run_time=.5)
        self.at('Consider a made');self.play(FadeOut(VGroup(intro,question,mail,flags,denom)),run_time=.4);heading=txt('hypothetical batch · 1,000 messages',[0,5.1,0],'label');self.add(heading)
        self.at('Ten are unwanted');left=box('unwanted','10',[-1.8,3.3,0],'primary');right=box('ordinary','990',[1.8,3.3,0],'secondary');self.play(FadeIn(VGroup(left,right)),run_time=.7)
        self.at('The filter catches');a=Arrow([-1.8,2.3,0],[-1.8,1.1,0],color=TEAL,buff=.05);true=txt('9 true flags',[-1.8,.65,0],'label','primary');self.play(Create(a),FadeIn(true),run_time=.6)
        self.at('Suppose it also');b=Arrow([1.8,2.3,0],[1.8,1.1,0],color=CORAL,buff=.05);rate=txt('10% of ordinary',[1.8,.65,0],'label','secondary');self.play(Create(b),FadeIn(rate),run_time=.6)
        self.at('That makes');rate=self.replace_label(rate,txt('99 false flags',[1.8,.65,0],'label','secondary'),.4)
        self.at('Now look only');self.play(FadeOut(VGroup(heading,left,right,a,b,true,rate)),run_time=.5);title=txt('flagged messages only',[0,4.7,0]);self.add(title)
        dots=VGroup()
        for i in range(108):
            point=np.array([-.18*17+.36*(i%18),2.8-.47*(i//18),0]);color=TEAL if i<9 else CORAL
            dot=Square(side_length=.18,fill_color=color,fill_opacity=1,stroke_color=color).move_to(point) if i<9 else Circle(radius=.09,fill_color=color,fill_opacity=1,stroke_color=color).move_to(point)
            dots.add(dot)
        self.play(LaggedStart(*[FadeIn(x) for x in dots],lag_ratio=.008),run_time=1.3)
        self.at('There are nine');legend=VGroup(txt('■ 9 true',[-1.6,-.5,0],'label','primary'),txt('● 99 false',[1.6,-.5,0],'label','secondary'));self.play(FadeIn(legend),run_time=.5)
        self.at('Nine out of one hundred');fraction=txt('9 / (9 + 99) ≈ 8.3%',[0,-2,0]);self.play(FadeIn(fraction),run_time=.5)
        self.at('Catching most');note=txt('different denominator · different question',[0,-3.2,0],'label');self.play(FadeIn(note),run_time=.4)
        self.at('Change the batch');self.play(FadeOut(VGroup(title,dots,legend,fraction,note)),run_time=.5);left=box('unwanted','100',[-1.8,3.3,0],'primary');right=box('ordinary','900',[1.8,3.3,0],'secondary');self.play(FadeIn(VGroup(left,right)),run_time=.6)
        self.at('The filtering rates');rates=VGroup(txt('90% caught',[-1.8,1.7,0],'label','primary'),txt('10% flagged',[1.8,1.7,0],'label','secondary'));self.play(FadeIn(rates),run_time=.4)
        self.at('We get ninety');counts=VGroup(txt('90 true',[-1.8,.3,0],color='primary'),txt('90 false',[1.8,.3,0],color='secondary'));self.play(FadeIn(counts),run_time=.4)
        self.at('This time');fraction=txt('90 / (90 + 90) = 50%',[0,-1.3,0]);self.play(FadeIn(fraction),run_time=.5)
        self.at('Recall is the share');self.play(FadeOut(VGroup(left,right,rates,counts,fraction)),run_time=.5);recall=VGroup(txt('recall',[0,3.7,0],color='primary'),txt('caught / actual unwanted',[0,2.65,0],'label'));self.play(FadeIn(recall),run_time=.5)
        self.at('Precision is the share');precision=VGroup(txt('precision',[0,.9,0],color='secondary'),txt('correct flags / all flags',[0,-.15,0],'label'));self.play(FadeIn(precision),run_time=.5)
        self.at('These are invented');self.at('When you read');end=txt('Which group is underneath?',[0,-2.6,0]);self.play(FadeIn(end),run_time=.5);self.finish()
