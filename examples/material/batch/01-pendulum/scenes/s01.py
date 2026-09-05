from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        pivot=np.array([0,3.6,0]);L=3.4;theta0=.20
        rail=self.line([-2.8,3.6,0],[2.8,3.6,0],'muted',3);self.add(rail)
        clock=self.process_clock(rate=1)
        def pend(x,length,period,t,r=.23,color='primary'):
            top=np.array([x,3.6,0]);a=theta0*math.cos(TAU*t/period);pos=top+length*np.array([math.sin(a),-math.cos(a),0])
            return VGroup(self.line(top,pos,'ink',3),self.bead(r,color).move_to(pos),Dot(top,radius=.055,color=self.palette['ink']))
        live=always_redraw(lambda:pend(0,L,2*math.sqrt(L),clock.value));self.add(live)
        self.at('A small weight');self.at('Its rhythm');self.at('Imagine a tiny');scope=self.label('small swings • ideal light string',[0,5.25,0],'muted','label').scale(.85);self.add(scope)
        self.at('We keep');self.at('The distance');measure=self.line([.9,3.6,0],[.9,.2,0],'secondary',2);label=self.label('length',[1.55,1.9,0],'secondary','label');self.play(Create(measure),FadeIn(label),run_time=.7)
        self.at('Gravity pulls');self.at('A longer');self.at('The time');eq=self.label('cycle time ∝ √length',[0,-2.6,0],'ink','claim');self.play(FadeIn(eq),run_time=.7)
        self.at('Here are two');self.play(FadeOut(measure),FadeOut(label),run_time=.5);self.remove(live);clock.pause();clock=self.process_clock();clock.pause()
        lengths=[1.1,4.4];periods=[2*math.sqrt(x) for x in lengths]
        live=always_redraw(lambda:VGroup(pend(-1.65,lengths[0],periods[0],clock.value),pend(1.1,lengths[1],periods[1],clock.value,color='secondary')));self.add(live)
        names=VGroup(self.label('1 length',[-1.8,-1.7,0],'primary','label'),self.label('4 lengths',[1.2,-1.7,0],'secondary','label'));self.add(names)
        self.at('Release them');clock.resume();self.at('While the long');ratio=self.label('2 cycles      :      1 cycle',[0,-3.55,0],'ink','label');self.play(FadeIn(ratio),run_time=.5)
        self.at('Their masses');self.at('Now compare');clock.pause();self.remove(live);self.play(FadeOut(names),FadeOut(ratio),run_time=.4);clock=self.process_clock();clock.pause();lengths=[.52,4.68];periods=[2*math.sqrt(x) for x in lengths]
        live=always_redraw(lambda:VGroup(pend(-1.65,lengths[0],periods[0],clock.value,r=.12),pend(1.1,lengths[1],periods[1],clock.value,r=.12,color='secondary')));self.add(live);clock.resume()
        names=VGroup(self.label('1 length',[-1.8,-1.8,0],'primary','label'),self.label('9 lengths',[1.2,-1.8,0],'secondary','label'));self.add(names)
        self.at('The longer');ratio=self.label('3 cycles      :      1 cycle',[0,-3.55,0],'ink','label');self.play(FadeIn(ratio),run_time=.5)
        self.at('These are');self.at('A quiet clock');self.finish()
