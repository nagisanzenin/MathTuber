from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];PAPER=self.palette['background'];WATER='#76A6A4';CORAL=self.palette['secondary']
        def boat():
            hull=Polygon([-.23,-.35,0],[-.25,.17,0],[0,.48,0],[.25,.17,0],[.23,-.35,0],fill_color='#A77755',fill_opacity=1,stroke_color=INK,stroke_width=1.7);inset=hull.copy().scale(.77).set_fill('#D9B989',1).set_stroke('#775D48',1);ribs=VGroup(*[Line([-.17,y,0],[.17,y,0],color='#775D48',stroke_width=2) for y in [-.2,.03,.22]]);return VGroup(hull,inset,ribs)
        def shore(y,upper):
            pts=[np.array([x,y+.04*np.sin(x*1.6),0]) for x in np.linspace(-4.2,4.2,80)];far=7.3 if upper else -7.3;fill=Polygon(*pts,[4.2,far,0],[-4.2,far,0],fill_color=PAPER,fill_opacity=1,stroke_width=0);edge=VMobject().set_points_smoothly(pts).set_stroke('#B4A98E',2);return VGroup(fill,edge)
        water=Rectangle(width=8.4,height=4.4,fill_color=WATER,fill_opacity=1,stroke_width=0).move_to([0,1.2,0]);self.add(water)
        clock=self.process_clock(rate=.5);q=ValueTracker(0);heading=ValueTracker(0);start=np.array([-1.8,-1,0]);direction=np.array([.55,1.1,0])
        def ripples():
            g=VGroup()
            for j in range(8):
                for i in range(4):
                    x=(-4+i*2.2+(j%2)*.7+.55*clock.value+4.4)%8.8-4.4;y=-.72+j*.54;g.add(Line([x-.17,y,0],[x+.17,y,0],color='#C2D4C8',stroke_width=1.3).set_opacity(.35))
            return g
        flow=always_redraw(ripples);self.add(flow,shore(3.4,True),shore(-1,False));dock=VGroup(*[Rectangle(width=.64,height=.12,fill_color='#C8A77D',fill_opacity=1,stroke_color='#9A8264',stroke_width=1).move_to([-1.8,-1.35+.13*i,0]) for i in range(4)]);goal=Circle(radius=.1,stroke_color=INK,stroke_width=2).move_to([-1.8,3.4,0]);self.add(dock,goal)
        vessel=always_redraw(lambda:boat().rotate(heading.get_value()).move_to(start+min(4,clock.value)*direction));path=always_redraw(lambda:Line(start,start+max(min(4,clock.value),.0001)*direction,color=PAPER,stroke_width=2));self.add(path,vessel)
        self.at('The boat points');self.at('Yet its journey');self.at('The river adds')
        self.at('Imagine a steady');self.at('Freeze the scene');clock.pause();self.play(vessel.animate.set_opacity(.5),run_time=.4)
        pos=np.array([-.8,-.1,0]);boatv=Arrow(pos,pos+UP*2,buff=0,color=INK,stroke_width=5);curr=Arrow(pos+UP*2,pos+UP*2+RIGHT,buff=0,color=CORAL,stroke_width=5);result=Arrow(pos,pos+UP*2+RIGHT,buff=0,color=PAPER,stroke_width=5)
        self.at('In one second');self.play(Create(boatv),run_time=.7);bl=self.label('boat: 1',[-1.8,1,0],'ink','label');self.play(FadeIn(bl),run_time=.4);self.at('The water carries');self.play(Create(curr),run_time=.7);cl=self.label('current: ½',[.1,2.6,0],'ink','label');self.play(FadeIn(cl),run_time=.4)
        self.at('Put the arrows');self.at('The diagonal joins');self.play(Create(result),run_time=.8);self.at('This is vector');eq=self.label('boat + current = movement from shore',[0,-2.1,0],'ink','claim').scale(.73);self.play(FadeIn(eq),run_time=.5)
        self.at('To arrive directly');self.play(FadeOut(VGroup(boatv,curr,result,bl,cl,eq)),FadeOut(path),run_time=.5);self.remove(vessel,path);clock=self.process_clock(rate=.5);clock.pause();direction=np.array([0,1.1*np.sqrt(.75),0]);heading.set_value(PI/6);vessel=always_redraw(lambda:boat().rotate(heading.get_value()).move_to(start+min(4/np.sqrt(.75),clock.value)*direction));self.add(vessel)
        origin=np.array([.3,.2,0]);u=Arrow(origin,origin+np.array([-1,np.sqrt(3),0]),buff=0,color=INK,stroke_width=5);w=Arrow(origin+np.array([-1,np.sqrt(3),0]),origin+UP*np.sqrt(3),buff=0,color=CORAL,stroke_width=5);v=Arrow(origin,origin+UP*np.sqrt(3),buff=0,color=PAPER,stroke_width=5)
        self.at('Its leftward');self.play(Create(u),Create(w),run_time=1);self.at('Here the current');note=self.label('30° upstream',[0,4.4,0],'ink','claim');self.play(FadeIn(note),run_time=.5)
        self.at('The remaining');self.play(Create(v),run_time=.6);self.at('It is a little');self.play(FadeOut(VGroup(u,w,v)),run_time=.5);clock.resume();path=always_redraw(lambda:Line(start,start+max(min(4/np.sqrt(.75),clock.value),.0001)*direction,color=PAPER,stroke_width=2));self.add(path)
        self.at('This ideal model');self.at('Sometimes reaching');self.finish()
