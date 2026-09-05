from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        u=ValueTracker(0);yl=1.8;floor=-1.4;xl=-2.4;xr=1.;wl=1.;wr=3.
        def fluid():
            a=yl-u.get_value();b=yl+u.get_value()/3
            return VGroup(Rectangle(width=wl,height=a-floor,fill_color=self.palette['primary'],fill_opacity=.2,stroke_width=0).move_to([xl,(a+floor)/2,0]),Rectangle(width=wr,height=b-floor,fill_color=self.palette['primary'],fill_opacity=.2,stroke_width=0).move_to([xr,(b+floor)/2,0]),Rectangle(width=1.4,height=.5,fill_color=self.palette['primary'],fill_opacity=.2,stroke_width=0).move_to([-1.2,-1.15,0]))
        def pistons():
            a=yl-u.get_value();b=yl+u.get_value()/3
            return VGroup(self.line([xl-.5,a,0],[xl+.5,a,0],'ink',8),self.line([xr-1.5,b,0],[xr+1.5,b,0],'ink',8))
        wall1=VMobject(color=self.palette['ink'],stroke_width=3).set_points_as_corners([[-2.9,3.7,0],[-2.9,floor,0],[2.5,floor,0],[2.5,3.7,0]]);wall2=VMobject(color=self.palette['ink'],stroke_width=3).set_points_as_corners([[-1.9,3.7,0],[-1.9,-.9,0],[-.5,-.9,0],[-.5,3.7,0]]);water=always_redraw(fluid);caps=always_redraw(pistons);self.add(water,wall1,wall2,caps)
        self.at('A small piston');self.play(u.animate.set_value(1.2),run_time=2.5);self.at('The liquid');self.at('Imagine an ideal');scope=self.label('ideal incompressible liquid',[0,4.8,0],'muted','label');self.play(FadeIn(scope),run_time=.5)
        self.at('Both chambers');self.at('The wider');areas=VGroup(self.label('area 1',[-2.4,-2,0],'primary','label').scale(.85),self.label('area 3',[1,-2,0],'secondary','label').scale(.85));self.play(FadeIn(areas),run_time=.6)
        self.at('Watch the space');parts=VGroup(*[Rectangle(width=1,height=.4,fill_color=self.palette['secondary'],fill_opacity=.75,stroke_color=self.palette['ink'],stroke_width=2).move_to([xl,yl-.2-.4*i,0]) for i in range(3)]);target=Rectangle(width=3,height=.4,stroke_color=self.palette['secondary'],stroke_width=3).move_to([xr,2.,0]);self.play(FadeIn(parts),Create(target),run_time=.8)
        self.at('The narrow');ratio=self.label('distance 3 : 1',[0,-2.9,0],'ink','claim');self.play(FadeIn(ratio),run_time=.5)
        self.at('Cut its colored');self.focus_outline(parts,run_time=.8);self.at('Placed side');self.play(*[part.animate.move_to([0+i,2.,0]) for i,part in enumerate(parts)],run_time=2.5)
        self.at('These regions');self.at('The same pressure');self.play(FadeOut(parts),FadeOut(target),run_time=.7)
        self.at('Across three');arrows=VGroup(Arrow([xl,yl-1.2+.75,0],[xl,yl-1.2+.15,0],buff=0,color=self.palette['primary']),Arrow([xr,2.35,0],[xr,4.15,0],buff=0,color=self.palette['secondary']));self.play(GrowArrow(arrows[0]),GrowArrow(arrows[1]),run_time=.7);force=self.label('force 1 : 3',[0,-3.65,0],'ink','label');self.play(FadeIn(force),run_time=.5)
        self.at('But the larger');self.at('The ideal work');self.play(FadeOut(ratio),FadeOut(force),run_time=.4);eq=self.label('force × distance stays equal',[0,-2.9,0],'ink','claim').scale(.85);self.play(FadeIn(eq),run_time=.6)
        self.at('We are ignoring');self.at('Another gentle');self.play(FadeOut(arrows),u.animate.set_value(1.8),run_time=3);self.finish()
