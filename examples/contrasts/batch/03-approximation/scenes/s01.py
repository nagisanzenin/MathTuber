from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent']
        def txt(s,p,role='label',color='ink'):return self.label(s,p,color,role)
        title=txt('7/5 ≈ √2',[0,5,0],'claim')
        row1=VGroup(*[Square(side_length=.17,fill_color=TEAL,fill_opacity=.7,stroke_width=.5,stroke_color=INK).move_to([-2.6+(i%10)*.27,3.4-(i//10)*.27,0]) for i in range(49)]);row2=VGroup(*[Square(side_length=.17,fill_color=CORAL,fill_opacity=.7,stroke_width=.5,stroke_color=INK).move_to([-2.6+(i%10)*.27,.6-(i//10)*.27,0]) for i in range(50)]);counts=VGroup(txt('7² = 49',[2,2.8,0]),txt('2 × 5² = 50',[1.7,0,0]));self.add(title,row1,row2);self.at('Seven fifths is not');self.play(Indicate(row2[-1],color=GOLD),run_time=.8);self.at('Seven squared');self.play(FadeIn(counts),run_time=.6)
        self.at('Those whole');self.play(Indicate(row2[-1],color=GOLD),run_time=.8)
        self.at('Here is a way');self.play(FadeOut(VGroup(title,row1,row2,counts)),run_time=.6)
        self.at('Start with');pair=txt('p = 1      q = 1',[0,4.6,0],'claim');self.play(FadeIn(pair),run_time=.4)
        self.at('For the next numerator');r1=txt('new p = p + 2q',[0,3.1,0],'claim');self.play(FadeIn(r1),run_time=.5)
        self.at('For the next denominator');r2=txt('new q = p + q',[0,1.8,0],'claim');self.play(FadeIn(r2),run_time=.5)
        self.at('Both calculations');old=txt('use the same old p and q',[0,.4,0]);self.play(FadeIn(old),run_time=.4)
        self.at('One over one becomes');seq=txt('1/1 → 3/2',[0,-1.1,0],'claim');self.play(FadeIn(seq),run_time=.5)
        self.at('Then three');pair=self.replace_label(pair,txt('p = 3      q = 2',[0,4.6,0],'claim'));seq=self.replace_label(seq,txt('1/1 → 3/2 → 7/5',[0,-1.1,0],'claim'))
        self.at('The next pair');pair=self.replace_label(pair,txt('p = 7      q = 5',[0,4.6,0],'claim'));seq=self.replace_label(seq,txt('1/1 → 3/2 → 7/5 → 17/12',[0,-1.1,0],'claim'))
        self.at('Their squares keep missing');certificate=txt('p² − 2q²:  −1, +1, −1, +1',[0,-2.4,0]);self.play(FadeIn(certificate),run_time=.5)
        self.at('Why does');self.play(FadeOut(VGroup(pair,r1,r2,old,seq,certificate)),run_time=.6);head=txt('the difference flips sign',[0,5,0],'claim');self.play(FadeIn(head),run_time=.5)
        self.at('The new squared');expr=txt('(p + 2q)² − 2(p + q)²',[0,3.5,0],'claim');self.play(FadeIn(expr),run_time=.6)
        self.at('Expand and cancel');expanded=VGroup(txt('p² + 4pq + 4q²',[0,2,0]),txt('− 2p² − 4pq − 2q²',[0,1,0]));self.play(FadeIn(expanded),run_time=.6)
        self.at('What remains');result=txt('−p² + 2q² = −(p² − 2q²)',[0,-.6,0]);self.play(FadeIn(result),run_time=.6)
        self.at('So minus');alternating=txt('−1 → +1 → −1 → +1',[0,-2,0],'claim');self.play(FadeIn(alternating),run_time=.5)
        self.at('Now divide');self.play(FadeOut(VGroup(head,expr,expanded,result,alternating)),run_time=.6);rule=txt('(p/q)² − 2 = ±1/q²',[0,4.7,0],'claim');self.play(FadeIn(rule),run_time=.5)
        self.at('For seven fifths');first=txt('(7/5)² = 2 − 1/25',[0,3.1,0],'claim');self.play(FadeIn(first),run_time=.5)
        self.at('For seventeen');second=txt('(17/12)² = 2 + 1/144',[0,1.7,0],'claim');self.play(FadeIn(second),run_time=.5)
        self.at('The growing');self.at('Because these');self.play(FadeOut(VGroup(rule,first,second)),run_time=.6);numberline=Line([-3,2,0],[3,2,0],color=INK);target=Line([1.05,1.65,0],[1.05,2.35,0],color=INK);rootlabel=txt('√2',[1.05,2.9,0],'claim');self.play(Create(numberline),Create(target),FadeIn(rootlabel),run_time=.7)
        # This final number line spans1.35 to1.445, so7/5 and17/12 are separated honestly.
        def xp(v):return -3+(v-1.35)/(.095)*6
        # Place the target using exactly the same mapping.
        target.move_to([xp(np.sqrt(2)),2,0]);rootlabel.move_to([xp(np.sqrt(2)),2.9,0])
        a=Dot([xp(7/5),2,0],color=TEAL,radius=.13);b=Dot([xp(17/12),2,0],color=CORAL,radius=.13);labs=VGroup(txt('7/5',[xp(7/5)-.2,1.2,0]),txt('17/12',[xp(17/12)+.4,.4,0]));self.play(FadeIn(a),FadeIn(b),FadeIn(labs),run_time=.6)
        self.at('They approach');self.at('An exact whole');self.finish()
