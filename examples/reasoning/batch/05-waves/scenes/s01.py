from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        lam=3.;amp=.43;speed=.75;clock=self.process_clock();base1=3.4;base2=1.2;sum_y=ValueTracker(1.2)
        def val(x,sign):return amp*np.sin(TAU/lam*(x+3)+sign*TAU/lam*speed*clock.value)
        def curve(which):
            base=base1 if which==-1 else base2 if which==1 else sum_y.get_value()
            pts=[[x,base+(val(x,which) if which else val(x,-1)+val(x,1)),0] for x in np.linspace(-3,3,161)]
            return VMobject(color=self.palette['primary'] if which==-1 else self.palette['secondary'] if which==1 else self.palette['ink'],stroke_width=4).set_points_smoothly(pts)
        sumline=always_redraw(lambda:curve(0));openingnodes=always_redraw(lambda:VGroup(*[Dot([z,sum_y.get_value(),0],radius=.065,color=self.palette['secondary']) for z in np.arange(-3,3.001,lam/2)]));self.add(sumline,openingnodes);self.at('Some places');self.at('That stillness');self.at('Separate their');self.play(sum_y.animate.set_value(-1.3),run_time=1.2);one=always_redraw(lambda:curve(-1));two=always_redraw(lambda:curve(1));self.add(one,two);labels=VGroup(self.label('contribution →',[0,4.4,0],'primary','label'),self.label('← contribution',[0,2.2,0],'secondary','label'),self.label('their sum',[0,.15,0],'ink','label'));baselines=VGroup(*[self.line([-3,y,0],[3,y,0],'muted',1) for y in [base1,base2,-1.3]]);self.add(baselines,labels)
        self.at('The upper wave');self.at('They have equal');self.at('The actual displacement')
        self.at('At this marked');self.remove(openingnodes);clock.pause();clock=self.process_clock(initial=lam/(4*speed));clock.pause();x=-1.5
        mark=VGroup(*[Dot([x,y,0],radius=.065,color=self.palette['ink']) for y in [base1,base2,-1.3]]);arrows=VGroup(Arrow([x,base1,0],[x,base1+val(x,-1),0],buff=0,color=self.palette['primary'],stroke_width=4),Arrow([x,base2,0],[x,base2+val(x,1),0],buff=0,color=self.palette['secondary'],stroke_width=4));self.play(FadeIn(mark),GrowArrow(arrows[0]),GrowArrow(arrows[1]),run_time=.8)
        self.at('They cancel');cancel=self.label('equal + opposite → zero',[0,-2.8,0],'ink','claim').scale(.85);self.play(FadeIn(cancel),run_time=.6)
        self.at('As time passes');self.play(FadeOut(arrows),run_time=.3);clock.resume();self.at('It is called');nodes=always_redraw(lambda:VGroup(*[Dot([z,-1.3,0],radius=.065,color=self.palette['secondary']) for z in np.arange(-3,3.001,lam/2)]));self.add(nodes)
        self.at('Between the nodes');clock.pause();clock=self.process_clock(initial=0);clock.pause();self.play(FadeOut(mark),FadeOut(cancel),run_time=.4);xx=-2.25;reinforce=VGroup(Arrow([xx,base1,0],[xx,base1+amp,0],buff=0,color=self.palette['primary']),Arrow([xx,base2,0],[xx,base2+amp,0],buff=0,color=self.palette['secondary']),Arrow([xx,-1.3,0],[xx,-1.3+2*amp,0],buff=0,color=self.palette['ink']));self.play(*[GrowArrow(a) for a in reinforce],run_time=.8)
        self.at('The string moves');self.play(FadeOut(reinforce),run_time=.4);clock.resume();self.at('The distance');spacing=self.label('node spacing = ½ wavelength',[0,-2.9,0],'ink','claim').scale(.8);self.play(FadeIn(spacing),run_time=.6)
        self.at('Use waves');clock.pause();self.remove(one,two,sumline,nodes);lam=1.5;clock=self.process_clock(initial=0);one=always_redraw(lambda:curve(-1));two=always_redraw(lambda:curve(1));sumline=always_redraw(lambda:curve(0));nodes=always_redraw(lambda:VGroup(*[Dot([z,-1.3,0],radius=.065,color=self.palette['secondary']) for z in np.arange(-3,3.001,lam/2)]));self.add(one,two,sumline,nodes)
        self.at('More still points');self.at('This is an ideal');self.at('A quiet point');self.finish()
