from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        c=np.array([0,1.6,0]);R=1.7;self.palette=dict(self.palette,ray='#A66C1C')
        drop=Circle(radius=R,stroke_color=self.palette['primary'],stroke_width=4,fill_color=self.palette['primary'],fill_opacity=.055).move_to(c);self.add(drop)
        def ray(b,n=4/3):
            P=np.array([-math.sqrt(1-b*b),b,0]);D=np.array([1.,0,0])
            def refract(d,N,eta):
                ci=-np.dot(d,N);return eta*d+(eta*ci-math.sqrt(1-eta*eta*(1-ci*ci)))*N
            T=refract(D,P,1/n);Q=P-2*np.dot(P,T)*T;U=T-2*np.dot(T,Q)*Q;S=Q-2*np.dot(Q,U)*U;V=refract(U,-S,n)
            return P,Q,S,V
        def draw_ray(b,col='ray',parts=4):
            P,Q,S,V=ray(b);points=[c+np.array([-3.3/R,b,0])*R,c+P*R,c+Q*R,c+S*R,c+(S+V*1.8)*R]
            return VGroup(*[self.line(a,b,col,4) for a,b in zip(points,points[1:])][:parts])
        path=draw_ray(.82);self.play(LaggedStart(*[Create(x) for x in path],lag_ratio=.5),run_time=2);self.add(path);self.say('Light finds a gathering angle.')
        self.at('Change where the ray enters');other=draw_ray(.6);self.play(Transform(path,other),run_time=1.8)
        self.at('Neighboring rays leave');self.play(Transform(path,draw_ray(.86)),run_time=1.5)
        self.at('Let us follow one ray');self.play(FadeOut(path),run_time=.4);P,Q,S,V=ray(.86);single=draw_ray(.86);self.play(Create(single[0]),run_time=.5)
        self.at('At the first surface');normal=DashedLine(c,c+P*R*1.25,stroke_color=self.palette['muted'],stroke_width=2);self.add(normal);self.play(Create(single[1]),run_time=1)
        self.at('reflects from the back');self.play(Create(single[2]),run_time=1)
        self.at('At the final surface');self.play(FadeOut(normal),Create(single[3]),run_time=1);self.add(single)
        self.at('Snell');self.say('Refraction + one reflection')
        self.at('These rays enter');self.play(FadeOut(single),run_time=.4);bundle=VGroup(*[draw_ray(b,'ray') for b in [.84,.855,.87,.885,.90]])
        for line in bundle:line.set_stroke(width=2,opacity=.65)
        self.play(LaggedStart(*[Create(x) for x in bundle],lag_ratio=.18),run_time=2)
        self.at('Measured from the direction');self.say('Nearly 42° from straight back');exitpoint=c+ray(.87)[2]*R;self.add(DashedLine(exitpoint,exitpoint+LEFT*2.2,stroke_color=self.palette['muted'],stroke_width=2),Arc(radius=.7,start_angle=PI,angle=42*DEGREES,arc_center=exitpoint,stroke_color=self.palette['ink'],stroke_width=2),self.label('42°',exitpoint+[-.95,-.38,0],'ink','detail'),self.label('straight back',exitpoint+[-2.55,.25,0],'ink','detail'))
        self.at('angle reaches a maximum');self.add(self.label('water index ≈ 4/3',[1.7,-1.6,0],'ink','detail'))
        self.at('It is not a claim');self.say('A concentration, not the only path.')
        self.at('Why an arc across the sky');self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.caption],run_time=.7);self.say('Equal angle → a circle in view');self.add(self.label('angular view of the sky',[0,4,0],'ink','detail'))
        origin=np.array([0,.8,0]);circle=Circle(radius=2.15,stroke_color=self.palette['accent'],stroke_width=7).move_to(origin);self.play(Create(circle),run_time=2);self.add(Dot(origin,radius=.07,color=self.palette['ink']),self.label('opposite the sun',[0,.35,0],'ink','detail'));self.add(DashedLine(origin,origin+UP*2.15,stroke_color=self.palette['muted']),self.label('42°',[.4,1.95,0],'ink','detail'))
        self.at('The horizon usually hides');horizon=self.line([-4,1.1,0],[4,1.1,0],'ink',2);mask=Rectangle(width=8,height=5.3,fill_color=self.palette['surface'],fill_opacity=1,stroke_width=0).move_to([0,-1.55,0]).set_z_index(1);self.play(FadeIn(mask),Create(horizon),run_time=.8)
        self.at('Different colors bend');bands=VGroup(*[Arc(radius=2.15-i*.06,start_angle=0,angle=PI,arc_center=origin,stroke_color=col,stroke_width=4) for i,col in enumerate(['#D85B42','#E5AA35','#187D8D','#6771A6'])]);self.play(Create(bands),run_time=1.5)
        self.at('A rainbow is not');self.say('Sunlight. Drops. Your viewpoint.')
        self.at('It is a relationship');self.finish()
