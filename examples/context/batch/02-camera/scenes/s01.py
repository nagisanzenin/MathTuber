from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];PAPER=self.palette['background'];origin=np.array([0,1,0]);od=ValueTracker(2.6);sd=ValueTracker(2.6)
        def candle(x):
            wax=RoundedRectangle(width=.3,height=1.65,corner_radius=.07,fill_color='#DBC69F',fill_opacity=1,stroke_color='#A88C60',stroke_width=1.5).move_to([x,.625,0]);wick=Line([x,1.45,0],[x,1.7,0],color=INK,stroke_width=2);flame=VMobject().set_points_smoothly([[x,1.62,0],[x-.18,1.82,0],[x-.11,2,0],[x,2.2,0],[x+.15,1.86,0],[x,1.62,0]]).set_fill('#D6A14E',1).set_stroke('#C38C45',1);core=flame.copy().scale(.55,about_point=np.array([x,1.7,0])).set_fill('#F1D08B',1).set_stroke(width=0);return VGroup(wax,wick,flame,core)
        box=Rectangle(width=3.6,height=4.4,fill_color='#243944',fill_opacity=1,stroke_color='#9A8264',stroke_width=4).move_to([1.8,1,0]);self.add(box)
        # Two aperture-wall segments leave a small opening at y1.
        wall=VGroup(Line([0,-1.2,0],[0,.95,0],color='#C8A77D',stroke_width=8),Line([0,1.05,0],[0,3.2,0],color='#C8A77D',stroke_width=8));self.add(wall)
        obj=always_redraw(lambda:candle(-od.get_value()));self.add(obj)
        def display():
            d=sd.get_value();m=d/od.get_value();screen=Line([d,-1.1,0],[d,3.1,0],color=PAPER,stroke_width=9);im=candle(-od.get_value()).scale(m,about_point=origin).rotate(PI,about_point=origin).set_opacity(.85);return VGroup(screen,im)
        img=always_redraw(display);self.add(img)
        base=Line([-3.5,-.25,0],[-1.5,-.25,0],color='#A88C60',stroke_width=3);self.add(base)
        self.at('Inside a dark');self.at('A tiny opening');self.at('We are looking');view=self.label('side view • image shown schematically',[0,4.35,0],'ink','label').scale(.8);self.play(FadeIn(view),run_time=.5)
        def ray(y,color):
            d=sd.get_value();x=od.get_value();return Line([-x,y,0],[d,1-(y-1)*d/x,0],color=color,stroke_width=3)
        self.at('Light from the top');top=always_redraw(lambda:ray(2.2,'#D6A14E'));self.play(Create(top),run_time=1.2);self.at('It reaches');self.at('Light from the bottom');bottom=always_redraw(lambda:ray(-.2,'#B7CDC3'));self.play(Create(bottom),run_time=1.2)
        self.at('The crossing');hole=Circle(radius=.12,color=self.palette['secondary'],stroke_width=3).move_to(origin);self.play(Create(hole),run_time=.6);self.at('No lens');self.at('Only a narrow');self.play(FadeOut(hole),run_time=.5)
        self.at('The two triangles');axis=DashedLine([-3.4,1,0],[3.5,1,0],color='#C8C2A5',stroke_width=2);self.play(Create(axis),run_time=.7)
        def triangles():
            x=od.get_value();d=sd.get_value();return VGroup(Polygon([-x,1,0],[-x,2.2,0],origin,fill_color=self.palette['primary'],fill_opacity=.2,stroke_width=0),Polygon(origin,[d,1,0],[d,1-1.2*d/x,0],fill_color=self.palette['secondary'],fill_opacity=.22,stroke_width=0))
        tri=always_redraw(triangles);self.add(tri);self.at('Image height divided');ratio=VGroup(self.label('image height / object height',[0,-1.85,0],'ink','label'),self.label('= screen distance / object distance',[0,-2.4,0],'ink','label')).scale(.85);self.play(FadeIn(ratio),run_time=.5)
        self.at('Move the screen');self.play(sd.animate.set_value(3.25),run_time=2.5)
        self.at('Keep that screen');self.play(od.animate.set_value(3.2),run_time=2.5);self.at('Now its image');self.at('Real openings');self.play(FadeOut(tri),FadeOut(axis),FadeOut(ratio),run_time=.7);self.at('Here we are following');self.at('A little darkness');self.play(FadeOut(top),FadeOut(bottom),run_time=1.5);self.finish()
