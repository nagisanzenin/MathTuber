from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        q=ValueTracker(6.);half=3.;screen_y=.8;slit_y=3.4
        anchor=VGroup(VectorizedPoint([-half,screen_y,0]),VectorizedPoint([half,screen_y,0]),VectorizedPoint([0,slit_y,0]))
        def pattern(half_width,y,ratio,band_height=1.15):
            blocks=VGroup()
            for u in np.linspace(-.49,.49,121):
                intensity=float(np.sinc(ratio*u)**2)
                blocks.add(Rectangle(width=half_width*2/120+.003,height=band_height,stroke_width=0,fill_color=self.palette['accent'],fill_opacity=intensity**.35).move_to([2*half_width*u,y,0]))
            return blocks
        bar=pattern(half,screen_y,6)
        slit=VGroup(self.line([-2.4,slit_y,0],[-.36,slit_y,0],'ink',8),self.line([.36,slit_y,0],[2.4,slit_y,0],'ink',8))
        subject=VGroup(anchor,bar,slit).scale(.78).shift(UP*.7);self.add(subject)
        self.at('A narrow opening');self.play(FadeIn(bar),run_time=1)
        self.at('Here, the bright');self.at('Come closer');self.stage_focus(subject,UP*1.8,width=6.4,height=4.2,run_time=1.6)
        left,right,aperture=[a.get_center().copy() for a in anchor];half=(right[0]-left[0])/2;screen_y=left[1];slit_y=aperture[1]
        self.remove(subject);self.add(anchor,bar,slit)
        view=self.label('screen pattern • brightness compressed',[0,screen_y-.9,0],'muted','label').scale(.8);self.add(view)
        self.at('The light has');scope=self.label('one wavelength • far field',[0,5.3,0],'muted','label').scale(.85);self.add(scope)
        self.at('We are looking');self.at('Light from different');self.at('In the center');middle=self.label('center',[0,screen_y+1.1,0],'accent','label');self.play(FadeIn(middle),run_time=.5)
        self.at('At certain angles');mins=VGroup(*[Line([s*2*half/6,screen_y-.75,0],[s*2*half/6,screen_y+.75,0],color=self.palette['primary'],stroke_width=2) for s in [-1,1]]);self.play(Create(mins),run_time=.7)
        self.at('The first dark line obeys');mark=self.label('first dark lines',[0,-.8,0],'primary','label');self.play(FadeIn(mark),run_time=.5)
        self.at('Slit width times');eq=self.label('width × sin(angle) = wavelength',[0,-2,0],'ink','claim').scale(.78);self.play(FadeIn(eq),run_time=.6)
        axis=self.label('horizontal position represents sin(angle)',[0,-3,0],'muted','label').scale(.78);self.play(FadeIn(axis),run_time=.5)
        self.at('Keep the wavelength');band_height=bar[0].height;original_gap=slit[1].get_start()[0];outer=slit[1].get_end()[0];self.remove(bar,mins,slit)
        def active():
         ratio=q.get_value();gap=original_gap*(ratio/6)
         stripe=pattern(half,screen_y,ratio,band_height)
         jaws=VGroup(self.line([-outer,slit_y,0],[-gap,slit_y,0],'ink',8),self.line([gap,slit_y,0],[outer,slit_y,0],'ink',8))
         boundaries=VGroup(*[Line([s*2*half/ratio,screen_y-.75,0],[s*2*half/ratio,screen_y+.75,0],color=self.palette['primary'],stroke_width=2) for s in [-1,1]])
         return VGroup(stripe,jaws,boundaries)
        live=always_redraw(active);self.add(live);self.play(q.animate.set_value(3),run_time=2.2)
        self.at('The sine of the first dark');notice=self.label('½ opening → wider central band',[0,-3.9,0],'ink','label');self.play(FadeIn(notice),run_time=.5)
        self.at('Both dark');self.at('The central band');self.at('This display');self.at('Open the slit');self.play(q.animate.set_value(6),FadeOut(notice),run_time=2)
        self.at('An opening does');self.finish()
