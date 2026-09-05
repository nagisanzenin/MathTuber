from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        a=np.array([-2.5,-1.8,0]);b=np.array([2.5,-1.8,0]);c=np.array([0,-1.8+2.5*math.sqrt(3),0]);vs=[a,b,c];p=VectorizedPoint([-.6,-.1,0]);colors=['primary','secondary','accent']
        def foot(x,a,b):v=b-a;return a+np.dot(x-a,v)/np.dot(v,v)*v
        def distances():return [np.linalg.norm(p.get_center()-foot(p.get_center(),vs[i],vs[(i+1)%3])) for i in range(3)]
        tri=self.poly(a,b,c,opacity=.05);dot=always_redraw(lambda:Dot(p.get_center(),radius=.12,color=self.palette['ink']));lines=always_redraw(lambda:VGroup(*[self.line(p.get_center(),foot(p.get_center(),vs[i],vs[(i+1)%3]),colors[i],6) for i in range(3)]))
        def bars():
         ds=distances();start=np.array([-2.165,-3.15,0]);g=VGroup()
         for length,col in zip(ds,colors):g.add(self.line(start,start+RIGHT*length,col,12));start=start+RIGHT*length
         return g
        bar=always_redraw(bars);barname=self.label('sum of the 3 distances',DOWN*3.65,'ink','detail').scale(.85);self.add(tri,lines,dot,bar,barname);self.play(p.animate.move_to([1.2,-.8,0]),run_time=3)
        self.at('three equal sides');self.say('Three distances. One fixed total.')
        self.at('Try pushing');self.play(p.animate.move_to([-.05,1.8,0]),run_time=3)
        self.at('Join the dot');self.play(p.animate.move_to([-.6,-.1,0]),run_time=1);pieces=VGroup(*[self.poly(vs[i],vs[(i+1)%3],p.get_center(),color=colors[i],opacity=.65) for i in range(3)]);self.play(LaggedStart(*[FadeIn(x) for x in pieces],lag_ratio=.25),run_time=1.5)
        self.at('Now rotate the pieces');self.say('Same base. Different heights.',5.8);dot.clear_updaters();lines.clear_updaters();bar.clear_updaters();self.play(FadeOut(tri),FadeOut(dot),FadeOut(lines),FadeOut(bar),FadeOut(barname),run_time=.5)
        # Rigid rotation and translation only: no scaling or area-changing morph.
        angles=[-np.arctan2((vs[(i+1)%3]-vs[i])[1],(vs[(i+1)%3]-vs[i])[0]) for i in range(3)]
        for i,piece in enumerate(pieces):
            self.play(piece.animate.move_to(UP*.4),run_time=.45)
            self.play(Rotate(piece,angle=angles[i],about_point=piece.get_center()),run_time=.6)
            self.play(piece.animate.shift(np.array([-2.5,3.0-i*2.25,0])-piece.get_vertices()[0]),run_time=.6)
        heights=VGroup()
        for i,piece in enumerate(pieces):
         v=piece.get_vertices();f=np.array([v[2][0],v[0][1],0]);heights.add(self.line(v[2],f,colors[i],7))
        self.play(Create(heights),run_time=.8)
        self.at('half its base');self.say('Area = ½ × base × height',5.8)
        self.at('adding the heights');self.play(*[Indicate(h,color=self.palette['ink']) for h in heights],run_time=1)
        self.at('Watch the dot move again');self.play(FadeOut(pieces),FadeOut(heights),run_time=.5);p.move_to([-.6,-.1,0]);dot=always_redraw(lambda:Dot(p.get_center(),radius=.12,color=self.palette['ink']));lines=always_redraw(lambda:VGroup(*[self.line(p.get_center(),foot(p.get_center(),vs[i],vs[(i+1)%3]),colors[i],6) for i in range(3)]));bar=always_redraw(bars);self.add(tri,dot,lines,bar,barname);self.say('Their sum = the triangle’s height');self.play(p.animate.move_to([1.2,-.9,0]),run_time=3)
        self.at('At the very top');self.play(p.animate.move_to(c),run_time=3);self.finish()
