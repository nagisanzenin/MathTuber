from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        scale=6;left=np.array([-3,2.8,0]);parts=[.3,.35,.35];cols=['primary','secondary','accent'];segments=VGroup();x=left.copy()
        for length,col in zip(parts,cols):segments.add(self.line(x,x+RIGHT*scale*length,col,12));x=x+RIGHT*scale*length
        self.add(segments)
        self.at('This one can');A=np.array([-1.05,.6,0]);B=A+RIGHT*2.1;C=(A+B)/2+UP*math.sqrt(1.8**2-1.05**2);targets=[self.line(A,C,'primary',12),self.line(C,B,'secondary',12),self.line(B,A,'accent',12)]
        # Sides must preserve lengths .30,.35,.35; corrected apex is obtained from two-circle intersection below.
        d=2.1;u=(1.8**2-2.1**2+d*d)/(2*d);C=A+RIGHT*u+UP*math.sqrt(1.8**2-u*u);targets=[self.line(A,C,'primary',12),self.line(C,B,'secondary',12),self.line(B,A,'accent',12)];self.play(*[Transform(s,t) for s,t in zip(segments,targets)],run_time=1.5)
        self.at('move a cut too far');fail=VGroup(self.line([-1.8,0,0],[-1.8,1.2,0],'primary',12),self.line([1.8,0,0],[1.8,1.2,0],'secondary',12),self.line([-1.8,0,0],[1.8,0,0],'accent',12));self.play(Transform(segments,fail),run_time=2);self.say('Longest piece < ½ the stick')
        self.at('one point in a square');self.play(FadeOut(segments),run_time=.5);o=np.array([-2.6,-2.1,0]);L=5.2
        xy=lambda a,b:o+np.array([L*a,L*b,0]);square=self.poly(xy(0,0),xy(1,0),xy(1,1),xy(0,1),opacity=.04);self.play(Create(square),run_time=1);self.add(self.label('first cut →',DOWN*2.6,'ink','detail'),self.label('second cut ↑',UP*3.65,'ink','detail'))
        self.at('Every equal area');point=Dot(xy(.3,.65),color=self.palette['ink']);guides=VGroup(DashedLine(xy(.3,0),xy(.3,.65),color=self.palette['muted']),DashedLine(xy(0,.65),xy(.3,.65),color=self.palette['muted']));self.play(FadeIn(point),Create(guides),run_time=1)
        self.at('both cuts land in the left half');self.play(FadeOut(point),FadeOut(guides),run_time=.3);q1=self.poly(xy(0,0),xy(.5,0),xy(.5,.5),xy(0,.5),color='secondary',opacity=.7);self.play(FadeIn(q1),run_time=.8)
        self.at('Both in the right half');q2=self.poly(xy(.5,.5),xy(1,.5),xy(1,1),xy(.5,1),color='secondary',opacity=.7);self.play(FadeIn(q2),run_time=.8)
        self.at('a diagonal slices away');f1=self.poly(xy(0,.5),xy(0,1),xy(.5,1),color='secondary',opacity=.7);f2=self.poly(xy(.5,0),xy(1,0),xy(1,.5),color='secondary',opacity=.7);self.play(FadeIn(f1),FadeIn(f2),run_time=1.2)
        self.at('two little triangles');ok1=self.poly(xy(0,.5),xy(.5,.5),xy(.5,1),color='primary',opacity=.8);ok2=self.poly(xy(.5,0),xy(.5,.5),xy(1,.5),color='primary',opacity=.8);self.play(FadeIn(ok1),FadeIn(ok2),run_time=1);self.say('Each surviving triangle = ⅛');self.add(self.label('⅛',xy(1/3,2/3),'background'),self.label('⅛',xy(2/3,1/3),'background'))
        self.at('one quarter of the whole');self.say('⅛ + ⅛ = ¼');self.play(Indicate(ok1),Indicate(ok2),run_time=1)
        self.at('Different ways');self.say('Independent + uniform cuts',5);self.finish()
