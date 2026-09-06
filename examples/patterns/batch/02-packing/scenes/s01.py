from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];INK=self.palette['ink'];CORAL=self.palette['secondary'];r=.47;q=ValueTracker(0);O=np.array([-3.055,-1.9,0])
        def center(c,row,t):return O+np.array([2*r*c+(row%2)*r*t,r*row*np.sqrt(4-t*t),0])
        stones=always_redraw(lambda:VGroup(*[self.bead(r,'surface',layers=5).move_to(center(c,row,q.get_value())) for row in range(6) for c in range(7)]));self.add(stones)
        self.at('Round stones');self.at('First, place');self.at('Now let each');self.play(q.animate.set_value(1),run_time=3,rate_func=smooth)
        self.at('The stones have');self.at('Their neighbors');self.at('But the rows');label=self.label('same circles · smaller row spacing',[0,-3.2,0],role='claim');self.play(FadeIn(label),run_time=.4)
        self.at('Look at three');stones.clear_updaters();self.play(stones.animate.set_opacity(.16),FadeOut(label),run_time=.5)
        # Lift an exact triangle of three circles; scale uniformly for the explanation.
        R=1.35;A=np.array([-R,-.1,0]);B=np.array([R,-.1,0]);C=np.array([0,np.sqrt(3)*R-.1,0]);large=VGroup(*[Circle(radius=R,fill_color='#E2D6BE',fill_opacity=1,stroke_color='#AC987A',stroke_width=2).move_to(p) for p in (A,B,C)]);self.play(FadeIn(large),run_time=.6)
        triangle=Polygon(A,B,C,stroke_color=TEAL,stroke_width=5,fill_opacity=0);dots=VGroup(*[Dot(p,radius=.075,color=INK) for p in (A,B,C)])
        self.at('Each pair is');self.play(Create(triangle),FadeIn(dots),run_time=.7);label=self.label('each side = 2 radii',[0,4.55,0],role='claim');self.play(FadeIn(label),run_time=.4)
        self.at('They form');self.at('Split it');foot=np.array([0,-.1,0]);height=Line(C,foot,color=CORAL,stroke_width=5);self.play(Create(height),run_time=.8);half=Line(A,foot,color=INK,stroke_width=5);self.play(Create(half),run_time=.4)
        self.at('Its height is');equation=self.label('h² + 1² = 2²',[0,-2.75,0],role='claim');self.play(FadeIn(equation),run_time=.4);label=self.replace_label(label,self.label('height: √3 radii',[0,4.55,0],role='claim'),.4);base=self.label('1 radius',[-.7,-.65,0]).scale(.75);self.play(FadeIn(base),run_time=.3)
        self.at('A repeating cell');self.play(FadeOut(VGroup(large,triangle,dots,height,half,base,label,equation)),run_time=.5);self.play(stones.animate.set_opacity(1),run_time=.4)
        # Two exact lattice vectors bound a fundamental cell. One circle's area per cell.
        v1=np.array([2*r,0,0]);v2=np.array([r,np.sqrt(3)*r,0]);P=center(2,2,1);cell=Polygon(P,P+v1,P+v1+v2,P+v2,stroke_color=CORAL,stroke_width=5,fill_color=CORAL,fill_opacity=.16);self.play(Create(cell),run_time=.6)
        self.at('Its height falls');label=self.label('same width · 86.6% of the height',[0,-3.2,0],role='claim');self.play(FadeIn(label),run_time=.4)
        self.at('The same circle');self.at('Across a large');label=self.replace_label(label,self.label('coverage: 78.5% → 90.7%',[0,-3.2,0],role='claim'),.5)
        self.at('Those numbers');self.at('A small tray');self.play(FadeOut(cell),run_time=.4);label=self.replace_label(label,self.label('repeating pattern · edges excluded',[0,-3.2,0]),.4)
        self.at('Look again');self.at('The quieter gaps');self.finish()
