from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        a=3.3;e=.6;b=a*math.sqrt(1-e*e);center=np.array([0,1,0]);sun=center+UP*a*e;phase=ValueTracker(0)
        def position(M):
            E=M
            for _ in range(10):E-=(E-e*math.sin(E)-M)/(1-e*math.cos(E))
            return center+np.array([b*math.sin(E),a*math.cos(E),0])
        def sector(start,end,color='primary',opacity=.2):
            points=[sun]+[position(m) for m in np.linspace(start,max(start+1e-5,end),81)];return Polygon(*points,fill_color=self.palette[color],fill_opacity=opacity,stroke_width=0)
        orbit=Ellipse(width=2*b,height=2*a,color=self.palette['muted'],stroke_width=3).move_to(center);star=VGroup(Circle(radius=.14,fill_color=self.palette['accent'],fill_opacity=1,stroke_width=0).move_to(sun),Circle(radius=.23,color=self.palette['accent'],stroke_width=1).move_to(sun));planet=always_redraw(lambda:Dot(position(phase.get_value()),radius=.095,color=self.palette['primary']));self.add(star,planet);self.play(Create(orbit),run_time=2)
        self.at('The Sun sits');sunlabel=self.label('Sun',sun+LEFT*.55,'ink','detail');self.play(FadeIn(sunlabel),run_time=.5)
        self.at('Near the Sun');self.play(phase.animate.set_value(TAU),run_time=6,rate_func=linear)
        self.at('Draw a line');phase.set_value(0);radius=always_redraw(lambda:self.line(sun,position(phase.get_value()),'primary',2));self.add(radius)
        self.at('Watch the area');sweep=always_redraw(lambda:sector(0,min(phase.get_value(),PI/4)));self.add(sweep);self.bring_to_front(star,planet,radius);self.play(phase.animate.set_value(PI/4),run_time=2.5,rate_func=linear);sweep.clear_updaters()
        self.at('This small interval');nearlabel=self.label('1/8 orbit time',[-1.1,4.8,0],'primary','detail');self.play(FadeIn(nearlabel),run_time=.5)
        self.at('Now take the same amount');phase.set_value(PI);far=always_redraw(lambda:sector(PI,min(phase.get_value(),PI+PI/4),'secondary'));self.add(far);self.bring_to_front(star,planet,radius);self.play(phase.animate.set_value(PI+PI/4),run_time=2.5,rate_func=linear);far.clear_updaters();farlabel=self.label('same time',[1,-2.8,0],'secondary','detail');self.add(farlabel)
        self.at('But the swept area');same=self.label('equal areas',[0,-3.65,0],'ink','label');self.play(FadeIn(same),run_time=.5)
        self.at('A short radius');self.focus_outline(sweep,run_time=1)
        self.at('A long radius');self.focus_outline(far,run_time=1)
        self.at('Why should gravity');self.play(*[FadeOut(x) for x in [sweep,far,nearlabel,farlabel,same]],run_time=.7)
        self.at('For a tiny time interval');M=PI/2-e;phase.set_value(M);pos=position(M);dt=.22;vel=np.array([0,-a,0]);tip=pos+vel*dt;triangle=Polygon(sun,pos,tip,fill_color=self.palette['secondary'],fill_opacity=.28,stroke_color=self.palette['secondary'],stroke_width=2);self.play(FadeIn(triangle),run_time=.8)
        self.at('Its area is half');rvec=pos-sun;projection=tip-np.dot(tip-pos,rvec)/np.dot(rvec,rvec)*rvec;side=DashedLine(tip,projection,color=self.palette['muted'],stroke_width=2,dash_length=.07);base=self.line(pos,projection,'secondary',5);self.play(Create(side),Create(base),run_time=.8)
        self.at('So area per second');formula=self.label('area rate = ½ r v sideways',[0,-3.5,0],'ink','label');self.play(FadeIn(formula),run_time=.7)
        self.at('Gravity pulls along');force=Arrow(pos,pos+(sun-pos)*.4,buff=0,color=self.palette['accent'],stroke_width=5);self.play(GrowArrow(force),run_time=.8)
        self.at('That pull has no turning');self.focus_outline(force,run_time=.9)
        self.at("The planet's angular momentum");moment=self.label('central pull · no torque',[0,-2.75,0],'ink','detail');self.play(FadeIn(moment),run_time=.6)
        self.at('This ideal orbit assumes');self.play(*[FadeOut(x) for x in [triangle,side,base,force,formula,moment]],run_time=.7);note=self.label('ideal two-body orbit',[0,-3.5,0],'muted','detail');self.play(FadeIn(note),run_time=.5)
        self.at('In the ideal picture');self.play(FadeOut(note),run_time=.3);phase.set_value(0)
        def all_areas():
            value=phase.get_value();g=VGroup()
            for j in range(8):
                start=j*PI/4
                if value>start:g.add(sector(start,min(value,start+PI/4),'primary' if j%2==0 else 'secondary',.16))
            return g
        areas=always_redraw(all_areas);self.add(areas);self.bring_to_front(star,planet,radius);self.play(phase.animate.set_value(TAU),run_time=5.5,rate_func=linear);self.finish()
