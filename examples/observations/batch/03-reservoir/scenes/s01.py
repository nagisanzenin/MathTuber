from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary']
        def card(letter,point,color='primary'):
            box=RoundedRectangle(width=1.05,height=1.3,corner_radius=.12,stroke_color=self.palette[color],stroke_width=4,fill_color=self.palette['surface'],fill_opacity=1)
            return VGroup(box,self.label(letter,ORIGIN,color,'claim')).move_to(point)
        slot=RoundedRectangle(width=1.5,height=1.8,corner_radius=.15,stroke_color=INK,stroke_width=3).move_to([0,1,0]);slotlabel=self.label('one stored message',[0,-.3,0]);incoming=card('A',[-2.7,3.3,0]);self.add(slot,slotlabel,incoming)
        self.at('Suppose messages');self.play(incoming.animate.move_to([0,1,0]),run_time=1.6);self.at('You want every')
        self.at('Keep the first');label=self.label('A is kept',[0,4.6,0],role='claim');self.play(FadeIn(label),run_time=.35)
        self.at('When the second');second=card('B',[-2.7,3.3,0]);self.play(FadeIn(second),run_time=.35);label=self.replace_label(label,self.label('replace with chance 1/2',[0,4.6,0],role='claim'),.4);self.play(incoming.animate.shift(RIGHT*2.7).set_opacity(.25),second.animate.move_to([0,1,0]),run_time=1.2)
        self.at('When the third arrives');third=card('C',[-2.7,3.3,0],'secondary');self.play(FadeIn(third),run_time=.35);label=self.replace_label(label,self.label('replace with chance 1/3',[0,4.6,0],role='claim'),.4)
        sample=self.label('one possible run',[0,-1.25,0]);self.play(FadeIn(sample),third.animate.move_to([-2.7,1,0]).set_opacity(.3),run_time=1)
        self.at('A smaller chance');self.at('But an earlier');self.play(FadeOut(VGroup(slot,slotlabel,incoming,second,third,label,sample)),run_time=.5)
        head=self.label('all possible stored messages',[0,4.7,0],role='claim');self.play(FadeIn(head),run_time=.3)
        cards=VGroup(card('A',[-2,2.8,0]),card('B',[0,2.8,0]),card('C',[2,2.8,0],'secondary'));self.add(cards)
        probA=self.label('1/2',[-2,1.5,0],role='claim');probB=self.label('1/2',[0,1.5,0],role='claim');new=self.label('new',[2,1.5,0],'secondary');self.at('After two messages');self.play(FadeIn(VGroup(probA,probB,new)),run_time=.5)
        self.at('Either stays');survive=self.label('A or B survives: 2/3',[0,4,0]);arrows=VGroup(*[Arrow([x,1,0],[x,-1,0],buff=.1,color=TEAL,stroke_width=4) for x in [-2,0]]);self.play(FadeIn(survive),Create(arrows),run_time=.8)
        self.at('One half times');eq=self.label('1/2 × 2/3 = 1/3',[0,-2.8,0],role='claim');outA=self.label('1/3',[-2,-1.55,0],role='claim');outB=self.label('1/3',[0,-1.55,0],role='claim');self.play(FadeIn(VGroup(eq,outA,outB)),run_time=.7)
        self.at('The new message');outC=self.label('1/3',[2,-1.55,0],'secondary','claim');arrowC=Arrow([2,1,0],[2,-1,0],buff=.1,color=CORAL,stroke_width=4);self.play(Create(arrowC),FadeIn(outC),run_time=.7)
        self.at('With four messages');self.play(FadeOut(VGroup(head,cards,probA,probB,new,survive,arrows,eq,outA,outB,outC,arrowC)),run_time=.5)
        cards4=VGroup(*[card(x,[-2.4+1.6*i,2.5,0],'secondary' if x=='D' else 'primary') for i,x in enumerate('ABCD')]);self.play(FadeIn(cards4),run_time=.7)
        fourhead=self.label('new message D: chance 1/4',[0,4.7,0],role='claim');self.play(FadeIn(fourhead),run_time=.3)
        self.at('Each earlier chance');equation=self.label('1/3 × 3/4 = 1/4',[0,.3,0],role='claim');chances=VGroup(*[self.label('1/4',[-2.4+1.6*i,1.2,0],'secondary' if i==3 else 'primary','claim') for i in range(4)]);self.play(FadeIn(equation),FadeIn(chances),run_time=.6)
        self.at('At step n');general=self.label('at step n: replace with chance 1/n',[0,-1.5,0]);self.play(FadeIn(general),run_time=.5)
        self.at('The same cancellation');formula=self.label('n ≥ 2: 1/(n−1) × (n−1)/n = 1/n',[0,-2.7,0],role='claim');self.play(FadeIn(formula),run_time=.5)
        self.at('This is reservoir');self.play(FadeOut(VGroup(fourhead,equation,general,formula)),run_time=.5);name=self.label('reservoir sampling · one item',[0,4.7,0],role='claim');self.play(FadeIn(name),run_time=.4)
        self.at('The letters here');foot=self.label('diagram: possibilities · memory: one item',[0,-1.2,0]);self.play(FadeIn(foot),run_time=.4)
        self.at('It can sample');self.play(FadeOut(VGroup(cards4[0],cards4[2],cards4[3],chances,foot)),cards4[1].animate.move_to([0,1.5,0]),run_time=.8);memory=self.label('one possible stored item · counter = 4',[0,-.3,0]);self.play(FadeIn(memory),run_time=.4);self.at('Equal chances');self.finish()
