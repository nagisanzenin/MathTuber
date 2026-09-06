from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];INK=self.palette['ink']
        def text(s,p,role='claim',color='ink'):return self.label(s,p,color,role)
        opening=VGroup(*[text(t,[-1.65,4-i*1.2,0]) for i,t in enumerate(['1/2','+ 1/6','+ 1/12','+ 1/20','+ …'])])
        self.at('Here is a sum');self.play(LaggedStart(*[FadeIn(x) for x in opening],lag_ratio=.45),run_time=2.5)
        self.at('The denominators');products=VGroup(*[text(t,[1.2,4-i*1.2,0],'label') for i,t in enumerate(['2 = 1×2','6 = 2×3','12 = 3×4','20 = 4×5'])]);self.play(FadeIn(products),run_time=.6)
        self.at('How can we');self.at('Try writing');self.play(FadeOut(VGroup(opening,products)),run_time=.4);identity=text('1/6 = 1/2 − 1/3',[0,2.7,0]);self.play(FadeIn(identity),run_time=.6)
        self.at('Use a common denominator');sixths=text('3/6 − 2/6 = 1/6',[0,.9,0]);self.play(FadeIn(sixths),run_time=.6)
        self.at('The same idea');self.play(FadeOut(VGroup(identity,sixths)),run_time=.4)
        general=text('1/n − 1/(n+1)',[0,3.2,0]);common=text('= ((n+1) − n) / (n(n+1))',[0,1.8,0]);result=text('= 1 / (n(n+1))',[0,.4,0]);self.play(FadeIn(general),run_time=.4)
        self.at('One divided by n, minus');self.play(FadeIn(common),run_time=.6);self.play(FadeIn(result),run_time=.6)
        self.at('Write the first');self.play(FadeOut(VGroup(general,common,result)),run_time=.5)
        title=text('four terms',[0,4.9,0]);self.add(title)
        plus=[];minus=[];ys=[3.6,2.1,.6,-.9]
        for k,y in enumerate(ys,1):
            a=text('1' if k==1 else f'+ 1/{k}',[-1.4,y,0],color='primary');b=text(f'− 1/{k+1}',[1.25,y,0],color='secondary');plus.append(a);minus.append(b)
            self.play(FadeIn(VGroup(a,b)),run_time=.35)
        self.at('The negative half');links=[]
        for idx,cue in enumerate(['The negative half','The thirds cancel','The thirds cancel']):
            if idx==1:self.at('The thirds cancel')
            pair=VGroup(minus[idx],plus[idx+1]);outline=VGroup(*[SurroundingRectangle(term,color=TEAL,buff=.12) for term in pair]);self.play(Create(outline),run_time=.35);self.play(FadeOut(pair),FadeOut(outline),run_time=.55)
        self.at('Only the first');self.play(plus[0].animate.move_to([-1.2,1.5,0]),minus[-1].animate.move_to([1.2,1.5,0]),run_time=.8)
        self.at('The sum is four fifths');total=text('= 4/5',[0,-.3,0]);self.play(FadeIn(total),run_time=.4)
        self.at('Add another term');title=self.replace_label(title,text('add a fifth term',[0,4.9,0]),.3);extraA=text('+ 1/5',[-1.2,-1.5,0],color='primary');extraB=text('− 1/6',[1.2,-1.5,0],color='secondary');self.play(FadeIn(VGroup(extraA,extraB)),FadeOut(total),run_time=.6)
        self.at('The old loose');outline=VGroup(*[SurroundingRectangle(term,color=TEAL,buff=.12) for term in [minus[-1],extraA]]);self.play(Create(outline),run_time=.35);self.play(FadeOut(VGroup(minus[-1],extraA,outline)),extraB.animate.move_to([1.2,1.5,0]),run_time=.8)
        self.at('After N terms');self.play(FadeOut(VGroup(title,plus[0],extraB)),run_time=.4);finite=text('S(N) = 1 − 1/(N+1)',[0,3.6,0]);self.play(FadeIn(finite),run_time=.5)
        self.at('That is an exact');note=text('N terms · exact finite sum',[0,2.1,0],'label');self.play(FadeIn(note),run_time=.4)
        self.at('As N grows');rows=VGroup(*[text(t,[0,.5-i*1.05,0],'label') for i,t in enumerate(['N = 4       gap = 1/5','N = 9       gap = 1/10','N = 99     gap = 1/100'])]);self.play(LaggedStart(*[FadeIn(x) for x in rows],lag_ratio=.4),run_time=1.6)
        self.at('The infinite sum');limit=text('limit: 1',[0,-3.4,0],color='primary');self.play(FadeIn(limit),run_time=.5)
        self.at('This is called');name=text('telescoping',[0,5.1,0]);self.play(FadeIn(name),run_time=.4)
        self.at('We first simplify');self.at('A long calculation');self.finish()
