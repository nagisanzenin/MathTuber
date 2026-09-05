from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        length=4.4;k=.24;grid=np.linspace(0,length,881);phi=k*grid*grid/(2*length);ds=grid[1]-grid[0];xx=np.r_[0,np.cumsum((np.cos(phi[:-1])+np.cos(phi[1:]))*ds/2)];yy=np.r_[0,np.cumsum((np.sin(phi[:-1])+np.sin(phi[1:]))*ds/2)]
        def data(kind,s):
            origin=np.array([-1.6,2.2 if kind==0 else -1.3,0])
            if s<=0:return origin+RIGHT*s,0,0
            if kind==0:return origin+np.array([math.sin(k*s)/k,(1-math.cos(k*s))/k,0]),k*s,k
            return origin+np.array([np.interp(s,grid,xx),np.interp(s,grid,yy),0]),k*s*s/(2*length),k*s/length
        def path(kind):
            points=[data(kind,s)[0] for s in np.linspace(-1.2,length,281)];return VMobject().set_points_as_corners(points).set_stroke(self.palette['primary'],width=5)
        p0=path(0);p1=path(1);self.add(p0.copy().set_stroke(width=25,opacity=.08));self.play(Create(p0),run_time=1.8)
        label0=self.label('straight → circle',[-1.1,5.05,0],'ink','label');self.add(label0)
        self.at('Their directions match');join0=Dot(data(0,0)[0],radius=.08,color=self.palette['secondary']);tangent=self.line(data(0,0)[0]+LEFT*.7,data(0,0)[0]+RIGHT*.7,'secondary',3);self.play(FadeIn(join0),Create(tangent),run_time=.8)
        self.at('But the amount of turning');self.play(FadeOut(tangent),run_time=.4);turnlabel=self.label('turning per metre',[-.4,.85,0],'ink','detail');self.play(FadeIn(turnlabel),run_time=.4)
        t=ValueTracker(-1.1)
        def traveler(kind):
            pos,a,c=data(kind,t.get_value());normal=np.array([-math.sin(a),math.cos(a),0]);direction=np.array([math.cos(a),math.sin(a),0]);items=VGroup(Dot(pos,radius=.105,color=self.palette['ink']),Arrow(pos,pos+direction*.6,buff=0,stroke_width=3,color=self.palette['primary']))
            if c>1e-5:items.add(Arrow(pos,pos+normal*c*5,buff=0,color=self.palette['secondary'],stroke_width=5,max_tip_length_to_length_ratio=.18))
            return items
        trav0=always_redraw(lambda:traveler(0));self.add(trav0)
        self.at('On the straight');self.play(t.animate.set_value(-.05),run_time=1.2,rate_func=linear)
        self.at('On the circle');self.play(t.animate.set_value(1.3),run_time=1.5,rate_func=linear)
        self.at('At constant speed');acc=self.label('sideways acceleration',[.9,.25,0],'secondary','detail');self.play(FadeIn(acc),run_time=.5)
        self.at('We can let the turn');self.play(FadeOut(turnlabel),FadeOut(acc),run_time=.4);self.add(p1.copy().set_stroke(width=25,opacity=.08));self.play(Create(p1),run_time=1.5);self.add(self.label('straight → Euler spiral',[-.6,.1,0],'ink','label'))
        self.at('This lower path starts');join1=Dot(data(1,0)[0],radius=.08,color=self.palette['secondary']);self.play(FadeIn(join1),run_time=.4)
        self.at('Each equal step');ticks=VGroup()
        for s in [0,1.1,2.2,3.3,4.4]:
            pos,a,c=data(1,s);normal=np.array([-math.sin(a),math.cos(a),0]);ticks.add(self.line(pos-normal*.12,pos+normal*.12,'ink',2))
        self.play(Create(ticks),run_time=1)
        self.at('The direction changes');tangents=VGroup(*[Arrow(data(1,s)[0],data(1,s)[0]+.55*np.array([math.cos(data(1,s)[1]),math.sin(data(1,s)[1]),0]),buff=0,color=self.palette['primary'],stroke_width=3) for s in [0,1.1,2.2,3.3,4.4]]);self.play(FadeIn(tangents),run_time=.8)
        self.at('Watch both travelers');self.play(FadeOut(tangents),FadeOut(ticks),FadeOut(join0),FadeOut(join1),run_time=.5);t.set_value(-1.1);trav1=always_redraw(lambda:traveler(1));self.add(trav1);self.play(t.animate.set_value(4.4),run_time=5,rate_func=linear)
        self.at('The upper arrow appears');t.set_value(-.1);self.play(t.animate.set_value(.8),run_time=2,rate_func=linear)
        self.at('The lower arrow grows');self.play(t.animate.set_value(4.4),run_time=2.5,rate_func=linear)
        self.at('At the end, both paths');endlabel=self.label('same final curvature',[0,-3,0],'ink','label');self.play(FadeIn(endlabel),run_time=.5)
        self.at('They do not reach');self.focus_outline(VGroup(trav0,trav1),run_time=.9)
        self.at('A transition spiral');pos,a,c=data(1,length);extension=ParametricFunction(lambda u:pos+np.array([(math.sin(a+k*u)-math.sin(a))/k,(-math.cos(a+k*u)+math.cos(a))/k,0]),t_range=[0,.5,.02],color=self.palette['secondary'],stroke_width=5);self.play(Create(extension),run_time=1)
        self.at('Real road design');self.play(FadeOut(endlabel),run_time=.5);note=self.label('one part of a real design',[0,-3,0],'muted','detail');self.play(FadeIn(note),run_time=.5)
        self.at('A quiet piece of mathematics');self.play(FadeOut(note),run_time=.5);self.finish()
