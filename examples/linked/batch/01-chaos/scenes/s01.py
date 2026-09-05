from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        vs=[np.array([-2.65,-.9,0]),np.array([2.65,-.9,0]),np.array([0,3.69,0])];rng=np.random.default_rng(71);pos=np.array([0,1,0]);points=[]
        for i in range(5000):pos=(pos+vs[int(rng.integers(3))])/2;points.append(pos.copy())
        panel=RoundedRectangle(width=6.4,height=6.2,corner_radius=.2,fill_color=self.palette['ink'],fill_opacity=1,stroke_width=0).move_to(UP*1.2);self.add(panel)
        cloud=lambda a,b:VGroup(*[Dot(x,radius=.018,color=self.palette['accent']) for x in points[a:b]])
        preview=cloud(30,2500);self.add(preview);self.wait(2);self.play(FadeOut(preview),run_time=.5)
        anchors=VGroup(*[Dot(x,radius=.1,color=self.palette['background']) for x in vs]);self.add(anchors)
        dot=Dot([0,1,0],radius=.095,color=self.palette['accent']);self.add(dot)
        self.at('Pick one of three');target=vs[2];aim=DashedLine(dot.get_center(),target,color=self.palette['background']);self.play(Create(aim),run_time=.5)
        self.at('Move halfway');self.play(dot.animate.move_to((dot.get_center()+target)/2),run_time=1.5);stepmark=Dot(dot.get_center(),radius=.04,color=self.palette['accent']);self.add(stepmark);self.remove(aim)
        self.at('Pick again');aim=DashedLine(dot.get_center(),vs[0],color=self.palette['background']);self.play(Create(aim),run_time=.4);self.play(dot.animate.move_to((dot.get_center()+vs[0])/2),run_time=1.2);self.remove(aim)
        self.at('Now speed it up');self.remove(dot,stepmark);c1=cloud(30,350);c2=cloud(350,1600);c3=cloud(1600,5000);self.play(FadeIn(c1),run_time=1);self.play(FadeIn(c2),run_time=1);self.play(FadeIn(c3),run_time=1.5);self.say('Random choices. Structured holes.')
        self.at('Slow down and watch');self.play(FadeOut(c1),FadeOut(c2),FadeOut(c3),FadeOut(panel),run_time=.6);anchors.set_color(self.palette['ink']);outer=self.poly(*vs,opacity=.08);self.add(outer)
        self.at('Start anywhere');sample=VectorizedPoint([-.9,.3,0]);sd=always_redraw(lambda:Dot(sample.get_center(),radius=.09,color=self.palette['ink']));land=always_redraw(lambda:VGroup(Dot((sample.get_center()+vs[2])/2,radius=.09,color=self.palette['secondary']),self.label('½',(sample.get_center()+vs[2])/2+RIGHT*.32,'secondary','detail')));link=always_redraw(lambda:DashedLine(sample.get_center(),vs[2],color=self.palette['muted']));self.add(link,sd,land);self.play(sample.animate.move_to([1.1,.1,0]),run_time=2)
        self.at('smaller triangle');top=self.poly(*[(x+vs[2])/2 for x in vs],color='secondary',opacity=.6);self.play(FadeIn(top),run_time=.7)
        self.at('other two choices');self.remove(sd,land,link);regions=VGroup(top,*[self.poly(*[(x+v)/2 for x in vs],color='primary',opacity=.6) for v in vs[:2]]);self.play(FadeIn(regions[1:]),run_time=1);self.say('Every next point lands in a corner.')
        self.at('same halfway rule');small=VGroup(*[self.poly(*[((x+v)/2+w)/2 for x in vs],color='primary',opacity=.7) for w in vs for v in vs]);self.play(FadeOut(regions),FadeIn(small),run_time=1.4)
        self.at('finite dot picture');self.say('Finite dots ≠ the infinite set')
        self.at('four corners of a square');self.play(FadeOut(outer),FadeOut(small),FadeOut(anchors),run_time=.6);sqvs=[np.array([x,y,0]) for x,y in [(-2.3,-1.4),(2.3,-1.4),(2.3,3.2),(-2.3,3.2)]];whole=self.poly(*sqvs,opacity=.05);self.add(whole);squares=VGroup(*[self.poly(*[(x+v)/2 for x in sqvs],color=['primary','accent','secondary','surface'][i],opacity=.8) for i,v in enumerate(sqvs)]);self.play(LaggedStart(*[FadeIn(s) for s in squares],lag_ratio=.3),run_time=2);self.say('Four half-size copies. No gap.');self.finish()
