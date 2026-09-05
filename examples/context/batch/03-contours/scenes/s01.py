from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        angle=ValueTracker(1.05);center=np.array([0,1,0]);levels=np.arange(0,3,.3)
        def project(x,y,z):
            a=angle.get_value();return center+np.array([x,y*np.cos(a)+z*np.sin(a)-1.1*np.sin(a),0])
        def hill():
            g=VGroup()
            for z in levels:
                t=np.linspace(0,TAU,121);x=np.sqrt((3-z)/.3)*np.cos(t);y=np.sqrt((3-z)/.6)*np.sin(t)
                col=interpolate_color(ManimColor('#647D66'),ManimColor('#D5CF9B'),z/3)
                ring=Polygon(*[project(a,b,z) for a,b in zip(x,y)],fill_color=col,fill_opacity=1,stroke_color='#51664F',stroke_width=1.8);g.add(ring)
            return g
        terrain=always_redraw(hill);self.add(terrain);self.at('A hill');self.at('Each of these');self.at('Imagine slicing');note=self.label('equal height intervals',[0,4.5,0],'ink','label');self.play(FadeIn(note),run_time=.7);self.at('Now look straight');self.play(angle.animate.set_value(0),run_time=1.5);self.at('Those slices')
        theta=ValueTracker(.65);r=np.sqrt(1.5)
        def point():
            t=theta.get_value();return np.array([np.sqrt(1.5/.3)*np.cos(t),np.sqrt(1.5/.6)*np.sin(t),0])
        def dot():return self.bead(radius=.075,color=self.palette['primary']).move_to(center+point())
        walker=always_redraw(dot);self.at('Walk along');self.add(walker);self.play(theta.animate.set_value(1.15),run_time=2.5);self.at('At this point')
        def dirs():
            p=point();g=np.array([-.6*p[0],-1.2*p[1],0]);g=g/np.linalg.norm(g);t=np.array([-g[1],g[0],0]);return p,g,t
        def tangent():
            p,g,t=dirs();return Line(center+p-t*.65,center+p+t*.65,color=self.palette['ink'],stroke_width=3)
        tan=always_redraw(tangent);self.play(Create(tan),run_time=.7);self.at('The steepest uphill')
        def gradient():
            p,g,t=dirs();return Arrow(center+p,center+p+g*1.05,buff=0,color=self.palette['primary'],stroke_width=5,max_tip_length_to_length_ratio=.18)
        arrow=always_redraw(gradient);self.play(FadeIn(arrow),run_time=.7)
        def square():
            p,g,t=dirs();return VMobject().set_points_as_corners([center+p+t*.19,center+p+(t+g)*.19,center+p+g*.19]).set_stroke(self.palette['ink'],2)
        mark=always_redraw(square);self.add(mark);self.at('This arrow');word=self.label('gradient',[0,-2.25,0],'primary','claim');self.play(FadeIn(word),run_time=.6);self.at('It describes');self.at('Closer contours');self.at('Move to another');self.play(theta.animate.set_value(2.5),run_time=2);self.at('The uphill');self.at('This is a local');self.play(FadeOut(word),FadeOut(note),run_time=.6);self.at('A quiet set');self.finish()
