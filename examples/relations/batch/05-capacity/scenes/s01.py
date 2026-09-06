from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent']
        def txt(s,p,role='label',color='ink'):return self.label(s,p,color,role)
        loc={'S':np.array([0,4.4,0]),'A':np.array([-2.25,1.65,0]),'B':np.array([2.25,1.65,0]),'T':np.array([0,-1.1,0])};caps={('S','A'):4,('S','B'):3,('A','T'):2,('A','B'):1,('B','T'):5};labelspos={('S','A'):[-1.75,3.35,0],('S','B'):[1.75,3.35,0],('A','T'):[-1.8,-.05,0],('A','B'):[0,2.2,0],('B','T'):[1.8,-.05,0]}
        nodes=VGroup(*[VGroup(Circle(radius=.42,color=INK,fill_color=self.palette['background'],fill_opacity=1,stroke_width=2),txt(k,[0,0,0])).move_to(v) for k,v in loc.items()]);edges={e:Arrow(loc[e[0]],loc[e[1]],buff=.47,color=INK,stroke_width=3,max_tip_length_to_length_ratio=.09) for e in caps};labs={e:txt(str(c),labelspos[e]) for e,c in caps.items()};self.add(*edges.values(),nodes,*labs.values())
        self.at('Seven units');ends=VGroup(txt('out: 4+3 = 7',[0,5.6,0]),txt('in: 2+5 = 7',[0,-2.05,0]));self.play(FadeIn(ends),run_time=.5)
        self.at('Yet this network');question=txt('maximum flow = 6?',[0,-3.2,0],'claim');self.play(FadeIn(question),run_time=.5)
        self.at('The limit is');self.at('Each arrow');self.play(FadeOut(ends),run_time=.4);legend=txt('units per time step · capacities',[0,5.6,0]);self.play(FadeIn(legend),run_time=.4)
        self.at('Flow cannot');self.at('Separate the source');cut=DashedLine([-3.1,-.25,0],[3.1,3.55,0],color=CORAL,stroke_width=4);self.play(Create(cut),run_time=.8)
        self.at('Every route');self.at('Only three arrows');cross=[('S','B'),('A','B'),('A','T')];self.play(*[edges[e].animate.set_color(CORAL) for e in cross],run_time=.6);self.play(*[Circumscribe(labs[e],color=CORAL) for e in cross],run_time=1)
        self.at('Their total');question=self.replace_label(question,txt('cut capacity: 3 + 1 + 2 = 6',[0,-3.2,0],'claim'))
        self.at('No routing');self.at('Can we actually');self.play(FadeOut(cut),*[edges[e].animate.set_color(INK) for e in cross],run_time=.5);question=self.replace_label(question,txt('construct a flow of 6',[0,-3.2,0],'claim'))
        flows={e:0 for e in caps}
        def show_flow():
            fresh={e:txt(f'{flows[e]}/{caps[e]}',labelspos[e]) for e in caps}
            self.play(*[FadeOut(labs[e]) for e in caps],run_time=.15)
            self.play(*[FadeIn(fresh[e]) for e in caps],run_time=.15)
            labs.update(fresh)
        def send(route,count,color):
            points=[loc[k] for k in route];path=VMobject().set_points_as_corners(points);packets=VGroup(*[Square(side_length=.14,fill_color=color,fill_opacity=1,stroke_width=0).move_to(points[0]) for _ in range(count)]);self.add(packets);self.play(LaggedStart(*[MoveAlongPath(x,path,rate_func=linear) for x in packets],lag_ratio=.18),run_time=1.0);self.remove(packets,*packets)
            for u,v in zip(route,route[1:]):flows[(u,v)]+=count
            show_flow()
        self.play(FadeOut(legend),run_time=.15);show_flow();legend=txt('flow / capacity · same time unit',[0,5.6,0]);self.play(FadeIn(legend),run_time=.15)
        self.at('Send two along');send(['S','A','T'],2,TEAL)
        self.at('Send three');send(['S','B','T'],3,GOLD)
        self.at('Send one more');send(['S','A','B','T'],1,CORAL)
        self.at('Every capacity');balance=txt('A: 3 = 2+1     B: 3+1 = 4',[0,-2.05,0]);self.play(FadeIn(balance),run_time=.5)
        self.at('We have both');self.play(Create(cut),run_time=.5);question=self.replace_label(question,txt('achieved 6 = cut limit 6',[0,-3.2,0],'claim'))
        self.at('That proves');self.at('This is the idea');self.at('Now increase');self.play(FadeOut(cut),FadeOut(balance),FadeOut(question),run_time=.4);caps[('A','B')]=2;labs[('A','B')]=self.replace_label(labs[('A','B')],txt('1/2',labelspos[('A','B')]));self.play(Circumscribe(labs[('A','B')],color=CORAL),run_time=.6)
        self.at('The cut can');send(['S','A','B','T'],1,CORAL);self.play(Create(cut),run_time=.5);question=txt('new cut: 3 + 2 + 2 = 7',[0,-3.2,0],'claim');self.play(FadeIn(question),run_time=.4)
        self.at('The network now');balance=txt('source sends 7 · destination receives 7',[0,-2.05,0]);self.play(FadeIn(balance),run_time=.4)
        self.at('A useful improvement');self.finish()
