from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        head=ValueTracker(1);clock=self.process_clock(rate=.45);surface=2.35;INK=self.palette['ink'];WATER='#79A9A6'
        # Cutaway reservoir, supported on a wooden plinth.
        stand=Rectangle(width=2.6,height=2.8,fill_color='#B99A71',fill_opacity=1,stroke_color='#947955',stroke_width=2).move_to([-2,-.25,0]);grain=VGroup(*[Line([-3.2,y,0],[-.8,y+.05,0],color='#A68A63',stroke_width=1) for y in [-1.2,-.6,0,.6]])
        jar=VMobject().set_points_as_corners([[-3.2,3,0],[-3.15,1.15,0],[-.85,1.15,0],[-.8,3,0]]).set_stroke('#B68F78',9);water=Rectangle(width=2.26,height=1.15,fill_color=WATER,fill_opacity=.85,stroke_width=0).move_to([-2,1.775,0]);self.add(stand,grain,water,jar)
        def path():
            end=surface-head.get_value();p=VMobject().start_new_path(np.array([-1.65,1.6,0]));p.add_line_to(np.array([-1.65,3.35,0]));p.add_cubic_bezier_curve_to(np.array([-1.65,3.65,0]),np.array([-1.45,3.7,0]),np.array([-1.2,3.7,0]));p.add_line_to(np.array([.3,3.7,0]));p.add_cubic_bezier_curve_to(np.array([.6,3.7,0]),np.array([.8,3.65,0]),np.array([.8,3.35,0]));p.add_line_to(np.array([2,end,0]));return p
        def tube():
            p=path();return VGroup(p.copy().set_stroke('#546F6B',13),p.copy().set_stroke('#B6D3C4',8),p.copy().set_stroke(WATER,5))
        tub=always_redraw(tube);self.add(tub)
        # Arc-length samples keep equal-diameter flow markers at uniform speed.
        arc_cache={}
        def particles():
            value=head.get_value()
            if arc_cache.get("head")!=value:
                p=path();pts=np.array([p.point_from_proportion(t) for t in np.linspace(0,1,220)]);dist=np.r_[0,np.cumsum(np.linalg.norm(np.diff(pts,axis=0),axis=1))];arc_cache.update(head=value,pts=pts,dist=dist)
            pts=arc_cache["pts"];dist=arc_cache["dist"];length=dist[-1];out=VGroup()
            for i in range(10):
                s=(i*length/10+clock.value*np.sqrt(head.get_value()))%length;pos=np.array([np.interp(s,dist,pts[:,k]) for k in range(3)]);out.add(Dot(pos,radius=.035,color='#F3EBD7'))
            return out
        flow=always_redraw(particles);self.add(flow)
        def bowl():
            y=surface-head.get_value();shape=VMobject().set_points_smoothly([[1.15,y-.35,0],[1.4,y-1,0],[2.3,y-1.15,0],[3.15,y-.35,0]]).set_stroke('#B68F78',8);rim=Ellipse(width=2,height=.2,color='#B68F78',stroke_width=3).move_to([2.15,y-.35,0]);velocity=np.array([1.2,y-3.35,0]);velocity=velocity/np.linalg.norm(velocity)*np.sqrt(2*9.81*head.get_value());flight=(velocity[1]+np.sqrt(velocity[1]**2+2*9.81*.62))/9.81;stream=ParametricFunction(lambda t:np.array([2+velocity[0]*t,y+velocity[1]*t-.5*9.81*t*t,0]),t_range=[0,flight],color=WATER,stroke_width=4);return VGroup(shape,rim,stream)
        b=always_redraw(bowl);self.add(b);self.at('Water rises');self.at('A siphon can do this');self.at('The useful height');self.at('It is the drop')
        def measure():
            y=surface-head.get_value();return VGroup(DashedLine([-3.2,surface,0],[3.4,surface,0],color=INK,stroke_width=1.7),DoubleArrow([3.35,surface,0],[3.35,y,0],buff=0,color=INK,stroke_width=3),DashedLine([2,y,0],[3.5,y,0],color=INK,stroke_width=1.7))
        h=always_redraw(measure);self.play(FadeIn(h),run_time=.8);self.at('Gravity releases');self.at('For an ideal');label=self.label('ideal steady flow',[0,4.6,0],'ink','label');self.play(FadeIn(label),run_time=.5);self.at('The large upper');self.at('Then gravitational');eq=self.label('g × drop = ½ × speed²',[0,-3.3,0],'ink','claim').scale(.9);self.play(FadeIn(eq),run_time=.7);self.at('Speed squared');self.at('Compare two');clock.pause();self.play(head.animate.set_value(4),run_time=2.3);clock.resume();self.at('Four times the drop');ratio=self.label('4 × drop → 2 × speed',[0,-3.85,0],'primary','label').scale(.8);self.play(FadeIn(ratio),run_time=.6);self.at('Real tubes');self.play(FadeOut(eq),FadeOut(ratio),run_time=.7);self.at('The pressure');self.at('Our picture');self.at('The water climbs');self.play(FadeOut(h),FadeOut(label),run_time=1);self.finish()
