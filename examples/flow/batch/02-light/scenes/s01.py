from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        o=np.array([-2.8,3.0,0]);r=ValueTracker(1.0)
        def pos(d,u,w):return o+np.array([1.35*d+.90*u*d,-.60*d+1.05*w*d,0])
        def patch(d,grid=True):
            g=VGroup(self.poly(*[pos(d,u,w) for u,w in [(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)]],color='primary',opacity=.28))
            n=int(round(d))
            if grid and n>1:
                for j in range(1,n):
                    z=-.5+j/n;g.add(self.line(pos(d,z,-.5),pos(d,z,.5),'ink',1.5),self.line(pos(d,-.5,z),pos(d,.5,z),'ink',1.5))
            return g
        self.at('A small lamp');lamp=VGroup(*[Circle(radius=z,fill_color=self.palette['accent'],fill_opacity=.06,stroke_opacity=0).move_to(o) for z in [.32,.24,.16]],Dot(o,radius=.08,color=self.palette['accent']))
        rays=VGroup(*[self.line(o,pos(3,u,w),'muted',2.5) for u,w in [(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)]])
        face=always_redraw(lambda:patch(r.get_value(),False));self.add(lamp,rays,face);self.play(r.animate.set_value(3),run_time=2.5,rate_func=linear)
        self.at('The light has more');self.play(r.animate.set_value(1),run_time=1.5)
        self.at('Watch one small');pulse=self.line(o,pos(1,0,0),'accent',4);self.play(ShowPassingFlash(pulse,time_width=.4),run_time=1)
        self.at('These rays mark');self.focus_outline(face,run_time=.6)
        self.at('A square patch');near=patch(1);self.add(near)
        self.at('Move the patch twice');self.play(r.animate.set_value(2),FadeOut(near),run_time=1.5,rate_func=linear)
        self.at('Its width doubles');edges=VGroup(self.line(pos(2,-.5,-.5),pos(2,.5,-.5),'secondary',5),self.line(pos(2,.5,-.5),pos(2,.5,.5),'secondary',5));self.play(Create(edges),run_time=.7)
        self.at('One square becomes');two=patch(2);self.add(two);self.play(FadeOut(edges),run_time=.4)
        self.at('The bundle carries');label=self.label('same bundle · 4 equal areas',[0,-1.5,0],'ink','detail');self.play(FadeIn(label),run_time=.5)
        self.at('Each small square');cell=self.poly(*[pos(2,u,w) for u,w in [(-.5,-.5),(0,-.5),(0,0),(-.5,0)]],color='accent',opacity=.6);self.play(FadeIn(cell),run_time=.5)
        self.at('Three times the distance');self.play(r.animate.set_value(3),FadeOut(two),FadeOut(cell),FadeOut(label),run_time=1.5,rate_func=linear)
        self.at('That makes nine');three=patch(3);self.add(three)
        self.at('Each receives one ninth');label=self.label('same bundle · 9 equal areas',[0,-1.5,0],'ink','detail');self.play(FadeIn(label),run_time=.5)
        self.at('The square in');self.focus_outline(three,run_time=.7)
        self.at('This model assumes');self.play(FadeOut(label),run_time=.6);note=self.label('point source · clear space',[0,-1.6,0],'muted','detail');self.play(FadeIn(note),run_time=.5)
        self.at('For freely spreading');self.play(FadeOut(note),run_time=.4)
        self.at('A little farther');self.finish()
