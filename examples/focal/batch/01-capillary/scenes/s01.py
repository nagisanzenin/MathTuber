from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        base=-1.;top=3.3;xs=[-1.3,1.3];rs=[.23,.46];hs=[2.4,1.2]
        reservoir=VGroup(self.line([-2.7,base-1,0],[-2.7,base+.6,0],'ink',3),self.line([-2.7,base-1,0],[2.7,base-1,0],'ink',3),self.line([2.7,base-1,0],[2.7,base+.6,0],'ink',3),Rectangle(width=5.4,height=1,fill_color=self.palette['primary'],fill_opacity=.15,stroke_width=0).move_to([0,base-.5,0]),self.line([-2.7,base,0],[2.7,base,0],'primary',2))
        tubes=VGroup(*[VGroup(*[self.line([x+s*r,base-.7,0],[x+s*r,top,0],'ink',3) for s in [-1,1]]) for x,r in zip(xs,rs)])
        water=VGroup(*[Rectangle(width=2*r,height=.7,fill_color=self.palette['primary'],fill_opacity=.3,stroke_width=0).move_to([x,base-.35,0]) for x,r in zip(xs,rs)])
        subject=VGroup(reservoir,tubes,water).scale(.76).shift(UP*.7);self.add(subject)
        self.at('Water can climb')
        for i,h in enumerate(hs):
         target=water[i].copy().stretch_to_fit_height((h+.7)*.76);target.align_to(water[i],DOWN);self.play(Transform(water[i],target),run_time=1.1)
        self.at('In the thinner');self.focus_outline(water[0],run_time=.7)
        self.at('Come closer');self.stage_focus(subject,UP*1,width=6.4,height=6.5,run_time=1.8)
        level=reservoir[-1].get_y();scope=self.label('widths exaggerated • equilibrium rise',[0,5.3,0],'muted','label').scale(.85);self.add(scope)
        self.at('Water meets');ring=Circle(radius=.45,color=self.palette['primary'],stroke_width=5).move_to([-1.6,-3.3,0]);self.play(Create(ring),run_time=.7)
        self.at('Surface tension');up=Arrow(water[0].get_top()+LEFT*.45,water[0].get_top()+LEFT*.45+UP*.8,buff=0,color=self.palette['primary']);self.play(GrowArrow(up),run_time=.6)
        self.at('The raised water');down=Arrow(water[0].get_center()+RIGHT*.4,water[0].get_center()+RIGHT*.4+DOWN*.8,buff=0,color=self.palette['secondary']);self.play(GrowArrow(down),run_time=.6)
        self.at('Double the radius');ring2=Circle(radius=.9,color=self.palette['secondary'],stroke_width=5).move_to([1.3,-3.3,0]);self.play(Create(ring2),FadeOut(up),FadeOut(down),run_time=.8)
        self.at('But the cross');self.play(ring.animate.set_fill(self.palette['primary'],opacity=.25),ring2.animate.set_fill(self.palette['secondary'],opacity=.25),run_time=.7)
        area=VGroup(self.label('1',ring.get_center(),'primary','label').scale(.8),self.label('4',ring2.get_center(),'secondary','label'));self.play(FadeIn(area),run_time=.5)
        self.at('At the same');self.focus_outline(ring2,run_time=.7)
        self.at('The wider column');self.focus_outline(water[1],run_time=.7)
        self.at('For the same');self.play(FadeOut(ring),FadeOut(ring2),FadeOut(area),run_time=.5);eq=self.label('radius × rise = constant',[0,-2.9,0],'ink','claim').scale(.9);self.play(FadeIn(eq),run_time=.5)
        self.at('Twice the radius');marks=VGroup(*[self.label(t,[w.get_x(),level-.9,0],c,'label') for w,t,c in zip(water,['1 radius','2 radii'],['primary','secondary'])]);self.play(FadeIn(marks),run_time=.5)
        self.at('This is an equilibrium');self.at('It does not explain')
        self.at('Now compare');self.play(FadeOut(marks),run_time=.25)
        x=tubes[1].get_center()[0];oldr=(tubes[1][1].get_x()-tubes[1][0].get_x())/2;newr=oldr*1.5
        newtube=VGroup(*[self.line([x+s*newr,tubes[1][0].get_bottom()[1],0],[x+s*newr,tubes[1][0].get_top()[1],0],'ink',3) for s in [-1,1]])
        bottom=water[1].get_bottom()[1];rise=(water[0].get_top()[1]-level)/3
        newwater=Rectangle(width=2*newr,height=level+rise-bottom,fill_color=self.palette['primary'],fill_opacity=.3,stroke_width=0).move_to([x,(level+rise+bottom)/2,0]);self.play(Transform(tubes[1],newtube),Transform(water[1],newwater),run_time=1.8)
        self.at('Its rise');last=VGroup(self.label('1 rise',[water[0].get_x()-.8,water[0].get_top()[1]+.15,0],'primary','label'),self.label('⅓ rise',[x,water[1].get_top()[1]+.4,0],'secondary','label'));self.play(FadeIn(last),run_time=.5)
        self.at('A small boundary');self.finish()
