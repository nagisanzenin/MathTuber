from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        angle=.20;direction=np.array([math.cos(angle),-math.sin(angle),0]);normal=np.array([math.sin(angle),math.cos(angle),0]);r=.58;length=5.1
        starts=[np.array([-2.6,2.5,0]),np.array([-2.6,.1,0])]
        for start in starts:self.add(self.line(start-.6*direction,start+direction*length,'ink',4))
        clock=self.process_clock(rate=.65);g=2.8
        base1=VGroup(self.bead(r,'primary'),Circle(radius=r*.83,fill_color=self.palette['primary'],fill_opacity=1,stroke_width=0));base2=VGroup(Circle(radius=r,stroke_color=self.palette['secondary'],stroke_width=12),Circle(radius=r-.09,stroke_color=self.palette['ink'],stroke_width=1))
        def body(i,t,dist=4.3):
            acceleration=g*math.sin(angle)/(1+(.5 if i==0 else 1));s=min(dist,.5*acceleration*t*t);center=starts[i]+r*normal+s*direction
            face=(base1 if i==0 else base2).copy().move_to(center);phi=-s/r;mark=Dot(center+r*.75*np.array([-math.sin(phi),math.cos(phi),0]),radius=.045,color=self.palette['ink'])
            return VGroup(face,mark)
        live=always_redraw(lambda:VGroup(body(0,clock.value),body(1,clock.value)));self.add(live)
        self.at('Two round');self.at('Their insides');clock.pause();scope=self.label('side view • ideal rolling • slowed',[0,5.2,0],'muted','label').scale(.85);self.add(scope)
        self.at('One is');labels=VGroup(self.label('solid cylinder',[0,4.2,0],'primary','label'),self.label('thin hoop',[0,1.3,0],'secondary','label'));self.play(FadeIn(labels),run_time=.5)
        self.at('The other');self.at('We compare');self.at('Falling gives');energy=self.label('height → travel + spin',[0,-2.2,0],'ink','claim').scale(.9);self.play(FadeIn(energy),run_time=.6)
        self.at('Mass far');self.at('The hoop stores');self.at('From the same');self.remove(live);clock=self.process_clock(rate=.65);live=always_redraw(lambda:VGroup(body(0,clock.value),body(1,clock.value)));self.add(live)
        self.at('Here its');fraction=self.label('cylinder: ⅔     hoop: ½',[0,-3.25,0],'ink','label');self.play(FadeIn(fraction),run_time=.5)
        self.at('The hoop gets');self.at('The difference');self.at('Try releasing');self.remove(live);starts=[s-.6*direction for s in starts];clock=self.process_clock(rate=.65);live=always_redraw(lambda:VGroup(body(0,clock.value,4.9),body(1,clock.value,4.9)));self.add(live)
        self.at('Both gain');self.at('Enough static');self.at('Inside a familiar');self.finish()
