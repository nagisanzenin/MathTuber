from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        phase=ValueTracker(.55);C=np.array([0,2.65,0]);r=1.55
        panel=RoundedRectangle(width=6.7,height=4.65,corner_radius=.25,stroke_width=0,fill_color=self.palette['ink'],fill_opacity=1).move_to([0,2.65,0]);self.add(panel)
        base=Circle(radius=r,stroke_color=self.palette['muted'],stroke_width=1.5,fill_color=interpolate_color(ManimColor(self.palette['ink']),ManimColor(self.palette['muted']),.22),fill_opacity=1).move_to(C)
        def illuminated(alpha):
            if (1-math.cos(alpha))/2<.00001:return VGroup()
            side=1 if math.sin(alpha)>=0 else -1;ys=np.linspace(-1,1,101);outer=[C+r*np.array([side*math.sqrt(max(0,1-y*y)),y,0]) for y in ys];inner=[C+r*np.array([side*math.cos(alpha)*math.sqrt(max(0,1-y*y)),y,0]) for y in ys[::-1]];return Polygon(*(outer+inner),stroke_width=0,fill_color=self.palette['background'],fill_opacity=1)
        lit=always_redraw(lambda:illuminated(phase.get_value()));self.add(base,lit)
        self.at('It is a meeting');self.play(phase.animate.set_value(.9),run_time=2.2)
        self.at('The whole sphere is still');outline=Circle(radius=r,stroke_color=self.palette['background'],stroke_width=2).move_to(C);self.play(Create(outline),run_time=1)
        E=np.array([0,-1.25,0]);orbitR=1.05
        self.at('In this simple model');orbit=Circle(radius=orbitR,color=self.palette['muted'],stroke_width=1.5).move_to(E);earth=Dot(E,radius=.14,color=self.palette['primary']);el=self.label('Earth',E+DOWN*.45,'ink','detail');self.play(Create(orbit),FadeIn(earth),FadeIn(el),run_time=1)
        def moonpos():return E+orbitR*np.array([-math.cos(phase.get_value()),math.sin(phase.get_value()),0])
        def moonmodel():
            p=moonpos();dark=Circle(radius=.16,stroke_width=0,fill_color=self.palette['ink'],fill_opacity=1).move_to(p);bright=Sector(radius=.16,start_angle=PI/2,angle=PI,fill_color=self.palette['accent'],fill_opacity=1,stroke_width=0).move_arc_center_to(p);return VGroup(dark,bright)
        moon=always_redraw(moonmodel);view=always_redraw(lambda:DashedLine(E,moonpos(),dash_length=.07,color=self.palette['primary'],stroke_width=2));sun=VGroup(*[Arrow([-3,-1.25+y,0],[-1.5,-1.25+y,0],buff=0,color=self.palette['accent'],stroke_width=2) for y in [-.65,0,.65]],self.label('sunlight',[-2.25,-2.25,0],'ink','detail'));self.add(moon,sun)
        self.at('We see another half');self.add(view);observer=self.label('view from Earth',[0,5.4,0],'ink','detail');self.play(FadeIn(observer),run_time=.5)
        self.at('The visible phase');self.play(phase.animate.set_value(PI/2),run_time=2)
        self.at('As the Moon travels');self.play(phase.animate.set_value(PI*.85),run_time=2.5)
        self.at('Near the direction');self.play(phase.animate.set_value(.08),run_time=2.2)
        self.at('A little farther');self.play(phase.animate.set_value(.65),run_time=2)
        self.at('At a quarter');self.play(phase.animate.set_value(PI/2),run_time=2)
        self.at('The visible disk');half=self.label('1/2 of the visible disk',[0,-2.9,0],'ink','label');self.play(FadeIn(half),run_time=.5)
        self.at('Yet sunlight still');self.focus_outline(moon,run_time=.8)
        self.at('On the opposite side');self.play(FadeOut(half),phase.animate.set_value(PI),run_time=2.4)
        self.at('The disk looks full');full=self.label('the sunlit half faces us',[0,-2.9,0],'ink','label');self.play(FadeIn(full),run_time=.5)
        self.at('The Moon has not');self.focus_outline(sun,run_time=.8)
        self.at('We are seeing more');self.play(FadeOut(full),run_time=.5)
        self.at('Ordinary phases are not');note=self.label('phases ≠ eclipses',[0,-2.9,0],'ink','label');self.play(FadeIn(note),run_time=.5)
        self.at('Earth shadow causes');self.play(phase.animate.set_value(PI*.8),run_time=2)
        self.at('The boundary between');self.play(FadeOut(note),run_time=.5);self.play(phase.animate.set_value(.9),run_time=1.6)
        def terminator(alpha):
            side=1 if math.sin(alpha)>=0 else -1
            return ParametricFunction(lambda t:C+r*np.array([side*math.cos(alpha)*math.cos(t),math.sin(t),0]),t_range=[-PI/2,PI/2],color=self.palette['accent'],stroke_width=3)
        edge=always_redraw(lambda:terminator(phase.get_value()));self.add(edge)
        self.at('Seen at an angle');self.play(phase.animate.set_value(1.2),run_time=2)
        self.at('Seen edge on');self.play(phase.animate.set_value(PI/2),run_time=2)
        self.at('This drawing shows');self.play(FadeOut(edge),run_time=.5);caveat=self.label('geometry of illuminated area',[0,-2.9,0],'muted','detail');self.play(FadeIn(caveat),run_time=.5)
        self.at('The familiar shapes');self.play(phase.animate.set_value(2*PI+PI/2),run_time=4.4,rate_func=linear)
        self.at('One unchanged sphere');self.play(FadeOut(caveat),phase.animate.set_value(2*PI+.65),run_time=2.5);self.finish()
