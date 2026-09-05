from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        R=2;r=.65
        def world(u,v):return np.array([(R+r*math.cos(v))*math.cos(u),(R+r*math.cos(v))*math.sin(u),r*math.sin(v)])
        def project(p):return np.array([p[0],1.4+.45*p[1]+.9*p[2],0])
        def torus():
            faces=[]
            for u in np.linspace(0,TAU,49)[:-1]:
                for v in np.linspace(0,TAU,21)[:-1]:
                    pts=[world(u,v),world(u+TAU/48,v),world(u+TAU/48,v+TAU/20),world(u,v+TAU/20)];m=world(u+PI/48,v+PI/20);n=np.array([math.cos(v)*math.cos(u),math.cos(v)*math.sin(u),math.sin(v)]);shade=.25+.5*(np.dot(n,np.array([-.3,-.4,.85]))+1)/2;color=interpolate_color(ManimColor(self.palette['primary']),ManimColor(self.palette['background']),1-shade);poly=Polygon(*[project(p) for p in pts],fill_color=color,fill_opacity=1,stroke_color=color,stroke_width=.3);faces.append((.9*m[1]-.45*m[2],u,poly))
            return sorted(faces,key=lambda f:f[0])
        faces=torus();full=VGroup(*[x[2] for x in faces]);opening=ValueTracker(0)
        for depth,u,poly in faces:
            poly.set_z_index(depth);poly.set_opacity(0);poly.add_updater(lambda mob,u=u:mob.set_opacity(1 if u<=opening.get_value() else 0))
        self.add(full);self.play(opening.animate.set_value(TAU),run_time=2,rate_func=linear)
        for _,_,poly in faces:poly.clear_updaters()
        self.at('Its answer follows');orbit=ParametricFunction(lambda t:project(np.array([R*math.cos(t),R*math.sin(t),0])),t_range=[0,TAU],color=self.palette['secondary'],stroke_width=3);self.play(Create(orbit),run_time=2)
        self.at('First look at');self.play(FadeOut(full),FadeOut(orbit),run_time=.8)
        center=np.array([.9,1.65,0]);small=1.1;axisx=-2.5
        axis=self.line([axisx,-.25,0],[axisx,4,0],'muted',2);disk=Circle(radius=small,color=self.palette['ink'],fill_color=self.palette['primary'],fill_opacity=.2,stroke_width=3).move_to(center);dot=Dot(center,radius=.06,color=self.palette['secondary']);radius=self.line(center,center+RIGHT*small,'secondary',3);rl=self.label('r',center+np.array([.55,.28,0]),'ink','detail');self.play(Create(axis),FadeIn(disk),FadeIn(dot),Create(radius),FadeIn(rl),run_time=1)
        self.at('Its area is');area=self.label('A = π r²',[.9,-.05,0],'ink','label');self.play(FadeIn(area),run_time=.6)
        self.at('Its center travels');big=self.line([axisx,1.65,0],center,'secondary',3);Rlabel=self.label('R',[-.8,2,0],'ink','label');self.play(Create(big),FadeIn(Rlabel),run_time=.7)
        self.at('That journey is');distance=self.label('journey = 2πR',[0,-1.15,0],'ink','label');self.play(FadeIn(distance),run_time=.6)
        self.at('Multiply the area');formula=self.label('V = (πr²)(2πR)',[0,-2.25,0],'ink','claim');self.play(FadeIn(formula),run_time=.8)
        self.at('But the inner side');self.play(FadeOut(radius),FadeOut(rl),FadeOut(big),FadeOut(Rlabel),FadeOut(area),FadeOut(distance),FadeOut(formula),run_time=.6)
        self.at('Take two equally');s=.5;left=center+LEFT*s;right=center+RIGHT*s;pieces=VGroup(Square(side_length=.17,color=self.palette['secondary'],fill_opacity=1).move_to(left),Square(side_length=.17,color=self.palette['accent'],fill_opacity=1).move_to(right));self.play(FadeIn(pieces),run_time=.7)
        self.at('One travels at');l=self.label('2π(R − s)',[-1.5,-.65,0],'secondary','label');self.play(FadeIn(l),run_time=.6)
        self.at('The other travels');rr=self.label('2π(R + s)',[1.5,-.65,0],'ink','label');self.play(FadeIn(rr),run_time=.6)
        self.at('Their two journey lengths');average=self.label('average = 2πR',[0,-1.8,0],'ink','label');self.play(FadeIn(average),run_time=.7)
        self.at('Pair up the little');pairs=VGroup()
        for y in [-.65,-.3,0,.3,.65]:
            for x in [.25,.55,.8]:
                if x*x+y*y<small*small*.9:
                    pairs.add(Square(side_length=.1,stroke_width=0,fill_color=self.palette['secondary'],fill_opacity=.7).move_to(center+np.array([-x,y,0])),Square(side_length=.1,stroke_width=0,fill_color=self.palette['accent'],fill_opacity=.7).move_to(center+np.array([x,y,0])))
        self.play(FadeOut(pieces),LaggedStart(*[FadeIn(x) for x in pairs],lag_ratio=.025),run_time=1.5)
        self.at('Every pair has');self.focus_outline(average,run_time=.8)
        self.at('As the pieces become');self.play(*[x.animate.scale(.4) for x in pairs],run_time=.5)
        self.at('Adding them gives');self.play(FadeOut(l),FadeOut(rr),FadeOut(average),FadeIn(formula),run_time=.8)
        self.at('This is an example');name=self.label('Pappus · centroid theorem',[0,4.4,0],'ink','detail');self.play(FadeIn(name),run_time=.7)
        self.at('The rotation axis must');self.focus_outline(axis,run_time=.8)
        self.at('If the disk crosses');note=self.label('axis outside the disk',[0,-1.3,0],'ink','detail');self.play(FadeIn(note),run_time=.6)
        self.at('For our ordinary ring');self.play(*[FadeOut(x) for x in [axis,disk,dot,pairs,formula,name,note]],run_time=.8)
        # The final sweep reveals depth-sorted surface patches and the moving cross section.
        phase=ValueTracker(.001)
        for depth,u,poly in faces:
            poly.set_z_index(depth);poly.set_opacity(1 if u<=phase.get_value() else 0);poly.add_updater(lambda mob,u=u:mob.set_opacity(1 if u<=phase.get_value() else 0))
        cut=always_redraw(lambda:Polygon(*[project(world(phase.get_value(),v)) for v in np.linspace(0,TAU,49)],fill_color=self.palette['secondary'],fill_opacity=.45,stroke_color=self.palette['secondary'],stroke_width=2).set_z_index(10));self.add(full,cut)
        self.at('One circle carried');self.play(phase.animate.set_value(TAU),run_time=4,rate_func=linear);self.remove(cut)
        for _,_,poly in faces:poly.clear_updaters()
        self.finish()
