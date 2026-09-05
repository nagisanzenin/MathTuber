from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        w=4.6;verts=np.array([[0,w/np.sqrt(3),0],[-w/2,-w/(2*np.sqrt(3)),0],[w/2,-w/(2*np.sqrt(3)),0]])
        # Boundary goes from vertex 0 to 1 around center 2, then 1 to 2 around 0, then 2 to 0 around 1.
        raw=[]
        for c,a,b in [(2,0,1),(0,1,2),(1,2,0)]:
            start=math.atan2(*(verts[a]-verts[c])[1::-1]);raw.extend(verts[c]+w*np.array([math.cos(t),math.sin(t),0]) for t in np.linspace(start,start+PI/3,181))
        raw=np.array(raw);theta=ValueTracker(0);center=np.array([0,.7,0])
        def points():
            t=theta.get_value();rot=np.array([[math.cos(t),-math.sin(t),0],[math.sin(t),math.cos(t),0],[0,0,1]]);pts=raw@rot.T;pts[:,0]-=(pts[:,0].max()+pts[:,0].min())/2;return pts+center
        def shape():
            s=VMobject(fill_color=self.palette['primary'],fill_opacity=.75,stroke_color=self.palette['ink'],stroke_width=3);s.set_points_as_corners(list(points())+[points()[0]]);return s
        body=always_redraw(shape);rails=VGroup(*[self.line([x,-2.7,0],[x,4,0],'ink',5) for x in [-w/2,w/2]]);self.add(rails,body);self.play(theta.animate.set_value(PI/3),run_time=4,rate_func=smooth);self.say('Same gap. Every direction.')
        self.at('This is a Reuleaux');self.say('Reuleaux triangle')
        self.at('ordinary equilateral triangle');body.clear_updaters();self.play(FadeOut(body),FadeOut(rails),run_time=.6);tri=self.poly(*[v+center for v in verts],opacity=.08);self.add(tri);self.say('Begin with three equal sides')
        self.at('Put a compass');arcs=VGroup()
        for c,a,b in [(2,0,1),(0,1,2),(1,2,0)]:
            if c==0:self.at('Repeat from each corner')
            start=math.atan2(*(verts[a]-verts[c])[1::-1]);arc=Arc(radius=w,start_angle=start,angle=PI/3,arc_center=verts[c]+center,color=self.palette['primary'],stroke_width=6);radius=self.line(verts[c]+center,verts[a]+center,'secondary',3);dot=Dot(verts[c]+center,color=self.palette['secondary']);self.add(radius,dot);self.play(Create(arc),Rotate(radius,PI/3,about_point=verts[c]+center),run_time=1.4);self.remove(radius,dot);arcs.add(arc)
        self.at('Now look at these two');self.play(FadeOut(tri),FadeOut(arcs),run_time=.5);theta.set_value(PI/6);body=always_redraw(shape);self.add(rails,body)
        def contacts():
            pts=points();a=pts[np.argmin(pts[:,0])];b=pts[np.argmax(pts[:,0])];return a,b
        contact=always_redraw(lambda:VGroup(*[Dot(p,radius=.11,color=self.palette['secondary']) for p in contacts()]));radius=always_redraw(lambda:self.line(*contacts(),'secondary',5));self.add(contact,radius);self.say('Corner to its own circular arc')
        self.at('The distance between them');radius_caption=self.label('one compass radius',[0,-3.3,0],'secondary','detail');self.add(radius_caption)
        self.at('Turn a little');self.play(theta.animate.set_value(PI/6+.3),run_time=3,rate_func=smooth)
        self.at('Turn further');self.play(theta.animate.set_value(PI/6+PI/3+.3),run_time=4,rate_func=smooth);self.say('The contact changes. The width stays.')
        self.at('It does not mean');self.remove(radius,contact,radius_caption);body.clear_updaters();self.play(FadeOut(rails),run_time=.5);pts=points();ctr=Dot(np.mean(verts,axis=0)+center,radius=.08,color=self.palette['ink']);self.add(ctr);self.say('Constant width ≠ constant radius')
        self.at('A circle has that extra');self.play(FadeOut(body),FadeOut(ctr),run_time=.6);circle=Circle(radius=2,stroke_color=self.palette['primary'],stroke_width=5).move_to(center);self.play(Create(circle),run_time=1);self.add(self.line(center,center+RIGHT*2,'secondary',4))
        self.at('The rounded triangle offers');self.play(FadeOut(circle),*[FadeOut(m) for m in list(self.mobjects) if isinstance(m,Line)],run_time=.5);theta.set_value(0);body=always_redraw(shape);self.add(body);self.play(theta.animate.set_value(PI/3),run_time=5,rate_func=smooth);self.say('Familiar property. Another possibility.');self.finish()
