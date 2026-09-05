from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        self.at('A moving sound')
        clock=self.process_clock();moving=[True];start=[0.0];T=1.25;v=.12;c=.48;center=np.array([0,1.8,0])
        def wavefield():
            t=clock.value-start[0];speed=v if moving[0] else 0.;sx=-1.8+speed*t if moving[0] else 0.
            g=VGroup()
            for k in range(math.floor(t/T)-7,math.floor(t/T)+1):
                age=t-k*T
                if age<.015:continue
                r=c*age;cx=-1.8+speed*k*T if moving[0] else 0.;segments=[];current=[]
                for a in np.linspace(0,TAU,181):
                    pt=np.array([cx+r*math.cos(a),1.8+r*math.sin(a),0])
                    if -3.15<=pt[0]<=3.15 and -.6<=pt[1]<=4.2:current.append(pt)
                    else:
                        if len(current)>1:segments.append(current)
                        current=[]
                if len(current)>1:segments.append(current)
                for pts in segments:g.add(VMobject(color=self.palette['primary'],stroke_width=2.3).set_points_as_corners(pts))
            g.add(Dot([sx,1.8,0],radius=.11,color=self.palette['secondary']))
            return g
        field=always_redraw(wavefield);self.add(field)
        self.at('Watch the places');clock.pause();source_x=-1.8+v*clock.value
        origins=VGroup(*[Dot([-1.8+v*k*T,1.8,0],radius=.035,color=self.palette['accent']) for k in range(max(0,math.floor(clock.value/T)-4),math.floor(clock.value/T)+1)])
        self.play(FadeIn(origins),run_time=.5)
        self.at('Each pulse starts');clock.resume()
        self.at('The old rings');self.play(FadeOut(origins),run_time=.4)
        self.at('Let us hold');clock.pause()
        self.at('In one beat');y=-1.7;x=-1.8;scale=2.5
        wave=self.line([x,y,0],[x+c*T*scale,y,0],'primary',6);wave_label=self.label('wave travel',[0,y-.35,0],'primary','detail');self.play(Create(wave),FadeIn(wave_label),run_time=.6)
        self.at('The source travels');travel=self.line([x,y-.9,0],[x+v*T*scale,y-.9,0],'secondary',6);travel_label=self.label('source travel',[.25,y-.9,0],'secondary','detail');self.play(Create(travel),FadeIn(travel_label),run_time=.6)
        self.at('Ahead subtract');front=self.line([x+v*T*scale,y+.15,0],[x+c*T*scale,y+.15,0],'accent',7);front_label=self.label('ahead',[.7,y+.15,0],'ink','detail');self.play(Create(front),FadeIn(front_label),run_time=.5)
        self.at('Behind add');back=self.line([x,y+.85,0],[x+(c+v)*T*scale,y+.85,0],'accent',5);back_label=self.label('behind',[.7,y+.85,0],'ink','detail');self.play(Create(back),FadeIn(back_label),run_time=.5)
        self.at('That creates');self.play(FadeOut(wave),FadeOut(wave_label),FadeOut(travel),FadeOut(travel_label),FadeOut(front),FadeOut(back),FadeOut(front_label),FadeOut(back_label),run_time=.6)
        def listeners():
            t=clock.value;g=VGroup()
            for x in [-2.9,2.9]:
                distance=min(abs(abs(x-(-1.8+v*k*T))-c*(t-k*T)) for k in range(math.floor(t/T)-12,math.floor(t/T)+1))
                pulse=max(0,1-distance/.09)
                g.add(Circle(radius=.10+.07*pulse,stroke_color=self.palette['ink'],stroke_width=2.5,fill_color=self.palette['accent'],fill_opacity=.15+.85*pulse).move_to([x,1.8,0]))
            return g
        self.at('When we let');clock.resume();ears=always_redraw(listeners);self.add(ears)
        self.at('A listener ahead');right=self.label('closer gaps → higher pitch',[0,-1.6,0],'primary','label');self.play(FadeIn(right),run_time=.5)
        self.at('A listener behind');left=self.label('wider gaps → lower pitch',[0,-2.3,0],'secondary','label');self.play(FadeIn(left),run_time=.5)
        self.at('The source itself');clock.pause()
        self.at('Compare with a source');ears.clear_updaters();self.play(FadeOut(ears),FadeOut(field),FadeOut(right),FadeOut(left),run_time=.5);moving[0]=False;start[0]=clock.value;clock.resume();field=always_redraw(wavefield);self.add(field)
        self.at('This is an ideal drawing');note=self.label('sound • still air',[0,-1.8,0],'muted','detail');self.play(FadeIn(note),run_time=.5)
        self.at('The surprise is');self.play(FadeOut(note),run_time=.5);self.finish()
