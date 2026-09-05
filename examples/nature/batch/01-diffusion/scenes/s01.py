from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        rng=np.random.default_rng(714);directions=np.array([[1,0],[-1,0],[0,1],[0,-1]])
        walks=np.concatenate([np.zeros((96,1,2)),np.cumsum(directions[rng.integers(0,4,(96,64))],axis=1)],axis=1)
        scale=.17;center=np.array([0,1.1,0]);dots=VGroup(*[Dot(center,radius=.055,color=self.palette['primary']) for _ in range(96)])
        start=Circle(radius=.08,stroke_color=self.palette['ink'],stroke_width=2).move_to(center);sample_label=self.label('96 simulated walks',[0,-2.5,0],'ink','detail');self.add(dots,start,sample_label)
        step=[0]
        def move_cloud(n,seconds):
            count=n-step[0]
            for k in range(step[0]+1,n+1):
                self.play(*[d.animate.move_to(center+np.r_[walks[i,k]*scale,0]) for i,d in enumerate(dots)],run_time=seconds/count,rate_func=linear)
            step[0]=n
        move_cloud(4,1.5);self.say('Wandering. Spreading.')
        self.at('Each dot takes');move_cloud(8,2)
        self.at('Some paths wander back');move_cloud(16,2)
        self.at('cloud has no preferred');move_cloud(32,2)
        self.at('To double the typical');move_cloud(64,3)
        self.at('Let us see why');self.play(dots.animate.scale(.45,about_point=center).shift(np.array([-2.2,-2.4,0])-center),start.animate.move_to([-2.2,-2.4,0]),FadeOut(sample_label),run_time=.7);self.say('Measure spread, not the edge.')
        origin=np.array([-2,1,0]);unit=.9
        grid=VGroup(*[self.line(origin+[x*unit,-unit,0],origin+[x*unit,unit,0],'surface',2) for x in range(5)],*[self.line(origin+[0,y*unit,0],origin+[4*unit,y*unit,0],'surface',2) for y in [-1,0,1]])
        self.add(grid,Dot(origin,radius=.06,color=self.palette['ink']),self.label('start',origin+DOWN*.45,'ink','detail'))
        self.at('Begin two steps');point=Dot(origin+[2*unit,0,0],radius=.12,color=self.palette['secondary']);self.add(point,self.line(origin,point.get_center(),'primary',4));value=self.label('distance² = 4',[0,3.2,0]);self.play(FadeIn(value),run_time=.5)
        self.at('next step can leave');ends=[(3,0,9),(1,0,1),(2,1,5),(2,-1,5)];branches=VGroup()
        for x,y,squared in ends:
            pos=origin+[x*unit,y*unit,0];branches.add(Arrow(point.get_center(),pos,buff=.12,stroke_width=3,color=self.palette['secondary']),Circle(radius=.2,fill_color=self.palette['background'],fill_opacity=1,stroke_color=self.palette['ink']).move_to(pos),self.label(str(squared),pos,'ink','detail').scale(.8))
        self.play(LaggedStart(*[FadeIn(m) for m in branches],lag_ratio=.04),run_time=1.2)
        self.at('Their average is five');self.say('(9 + 1 + 5 + 5) / 4 = 5')
        self.at('opposite steps cancel');self.play(Circumscribe(branches[:6],color=self.palette['secondary'],buff=.12),run_time=.8);self.play(Circumscribe(branches[6:],color=self.palette['secondary'],buff=.12),run_time=.8)
        self.at('Only one squared step');self.say('Mean distance² grows by 1.')
        self.at('After sixteen steps');self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.caption and m is not dots],run_time=.5);self.remove(dots)
        for n,y,col in [(16,2.2,'primary'),(64,-.7,'secondary')]:
            radius=.19*math.sqrt(n);circle=Circle(radius=radius,stroke_color=self.palette[col],stroke_width=4).move_to([0,y,0]);self.add(circle,Dot([0,y,0],radius=.045,color=self.palette['ink']),self.label(str(n)+' steps',[2.5,y,0],'ink','detail'),self.label('RMS '+str(int(math.sqrt(n))),[-2.25,y,0],col,'detail'))
        self.at('After sixty four steps');self.say('4 × time → 2 × spread')
        self.at('not a boundary containing');self.say('RMS is a measure, not a wall.');outside=Dot([1.1,2.9,0],radius=.07,color=self.palette['primary']);self.play(FadeIn(outside),run_time=.4)
        self.at('Flowing water');self.say('Drift can carry the cloud too.')
        self.at('Even directionless');self.say('A rhythm in the wandering.');self.finish()
