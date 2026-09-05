from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        s=ValueTracker(0);y0=-.3;h=3.;b=4.
        def outline():
            q=s.get_value();return self.poly([-2,y0,0],[2,y0,0],[2+q,y0+h,0],[-2+q,y0+h,0],opacity=.55)
        live=always_redraw(outline);self.add(live);self.at('A patch');self.play(s.animate.set_value(1.2),run_time=2);self.at('Its outline')
        self.at('Keep its base');base=self.line([-2,y0-.25,0],[2,y0-.25,0],'ink',2);height=self.line([-3.3,y0,0],[-3.3,y0+h,0],'secondary',3);labels=VGroup(self.label('base',[0,-1.05,0]),self.label('height',[-2.7,3.2,0],'secondary'));self.play(Create(base),Create(height),FadeIn(labels),run_time=.8)
        self.at('Now cut');self.remove(live);body=self.poly([-2,y0,0],[2,y0,0],[2,y0+h,0],[-.8,y0+h,0],opacity=.55);piece=self.poly([2,y0,0],[3.2,y0+h,0],[2,y0+h,0],color='secondary',opacity=.75);self.add(body,piece);cut=DashedLine([2,y0,0],[2,y0+h,0],color=self.palette['ink'],stroke_width=3);self.play(Create(cut),run_time=.8)
        self.at('Slide the same');self.remove(cut);self.play(piece.animate.shift(LEFT*4),run_time=2.5)
        self.at('It fits');self.focus_outline(VGroup(body,piece),run_time=.8)
        self.at('Nothing was');self.at('The leaning');self.at('So its area');eq=self.label('area = base × height',[0,-2.1,0],'ink','claim');self.play(FadeIn(eq),run_time=.7)
        self.at('The height');self.focus_outline(height,run_time=.8);self.at('It is not');self.play(piece.animate.shift(RIGHT*4),FadeOut(height),FadeOut(labels),FadeOut(base),run_time=1.2);
        self.at('Let the shape');self.remove(piece,body);self.add(live);self.play(s.animate.set_value(-1.2),run_time=2)
        self.at('Each horizontal');
        def layers():
            q=s.get_value();return VGroup(*[self.line([-2+q*f,y0+h*f,0],[2+q*f,y0+h*f,0],'secondary',2) for f in np.linspace(.12,.88,7)])
        strips=always_redraw(layers);self.add(strips);self.at('The layers');self.play(s.animate.set_value(.9),run_time=3);self.at('Sometimes a new');self.play(s.animate.set_value(0),run_time=2);self.finish()
