from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];O=np.array([-2.8,-.6,0]);q=ValueTracker(0);rodlen=1.5
        def shape(t):return np.array([1.8+.48*np.cos(t),1.1+.3*np.sin(t)+.09*np.sin(2*t),0])
        def geometry(t):
         p=shape(t);n=np.linalg.norm(p);u=p/2+np.sqrt(rodlen**2-n*n/4)*np.array([-p[1],p[0],0])/n;v=p-u
         return O+u,O+2*u,O+p,O+2*u+v,O+2*p
        small=self.trace_curve(lambda t:O+shape(t),q.get_value,0,TAU,801,color='primary',stroke_width=4);large=self.trace_curve(lambda t:O+2*shape(t),q.get_value,0,TAU,801,color='secondary',stroke_width=4);self.add(small,large)
        def machine():
         a,d,p,c,z=geometry(q.get_value());rods=VGroup(*[Line(x,y,color='#AD8F63',stroke_width=8) for x,y in [(O,d),(a,p),(p,c),(d,z)]]);joints=VGroup(*[Dot(x,radius=.065,color=INK) for x in [a,d,c]]);return VGroup(rods,joints)
        self.add(always_redraw(machine),self.bead(.14,'ink').move_to(O));self.add(always_redraw(lambda:self.bead(.11,'primary').move_to(geometry(q.get_value())[2])),always_redraw(lambda:self.bead(.11,'secondary').move_to(geometry(q.get_value())[4])))
        self.add(self.label('O · fixed pivot',[-2.25,-1.15,0]).scale(.75));claim=self.label('one motion · two scales',[0,4.55,0],role='claim');self.add(claim)
        self.at('One point follows');self.play(q.animate.set_value(.8),run_time=2,rate_func=smooth);self.at('Another point draws');self.play(q.animate.set_value(1.6),run_time=2.8,rate_func=smooth);self.at('The rods between');self.play(q.animate.set_value(2.2),run_time=2.1,rate_func=smooth)
        self.at('Pause and look');a,d,p,c,z=geometry(q.get_value());ray=DashedLine(O,z,color=INK,stroke_width=2);self.play(Create(ray),run_time=.4)
        self.at('Two sides form');tri1=Polygon(O,a,p,stroke_color=TEAL,stroke_width=5,fill_opacity=0);tri2=Polygon(O,d,z,stroke_color=CORAL,stroke_width=3,fill_opacity=0);self.play(Create(tri2),Create(tri1),run_time=.8)
        self.at('Their directions match');self.focus_outline(Line(a,p),run_time=.7)
        self.at('The long side');measure=self.label('long side = 2 × short side',[0,-2.3,0],role='claim');letters=VGroup();self.play(FadeIn(measure),run_time=.5)
        self.at('The triangles therefore');copy=tri1.copy();self.add(copy);self.play(copy.animate.scale(2,about_point=O),run_time=1.2);self.play(FadeOut(copy),run_time=.3);measure=self.replace_label(measure,self.label('matching triangles · scale 2',[0,-2.3,0],role='claim'),.5)
        self.at('The copying point');relation=self.label('copy distance = 2 × tracing distance',[0,-3.2,0]).scale(.9);self.play(FadeIn(relation),run_time=.4)
        self.at('Let the points');self.play(FadeOut(VGroup(tri1,tri2,ray,letters,measure)),run_time=.4);self.play(q.animate.set_value(3.1),run_time=1.4,rate_func=smooth)
        self.at('Every part');self.play(q.animate.set_value(4.5),run_time=2.8,rate_func=smooth);self.at('Lengths double');self.play(q.animate.set_value(TAU),run_time=2.3,rate_func=smooth)
        self.at('This drawing tool');claim=self.replace_label(claim,self.label('pantograph',[0,4.55,0],role='claim'),.5);self.at('Its ideal rods')
        self.at('Swap which point');small.clear_updaters();large.clear_updaters();small.set_stroke(opacity=.25);large.set_stroke(opacity=.25);q.set_value(0);relation=self.replace_label(relation,self.label('large outline → half-size copy',[0,-3.2,0]),.4);newsmall=self.trace_curve(lambda t:O+shape(t),q.get_value,0,TAU,801,color='primary',stroke_width=5);self.add(newsmall);self.play(q.animate.set_value(PI),run_time=2.2,rate_func=smooth)
        self.at('The same arrangement');self.play(q.animate.set_value(TAU),run_time=3,rate_func=smooth);self.finish()
