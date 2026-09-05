from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        center=np.array([0,1.1,0]);r=2.35;angles=np.array([90,210,330])*DEGREES;pins=[center+r*np.array([math.cos(a),math.sin(a),0]) for a in angles]
        junction=VectorizedPoint(center+[.7,-.4,0]);lines=always_redraw(lambda:VGroup(*[self.line(junction.get_center(),p,'primary',7) for p in pins]));pinmarks=VGroup(*[Circle(radius=.14,fill_color=self.palette['surface'],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=2).move_to(p) for p in pins]);self.add(lines,pinmarks);self.play(junction.animate.move_to(center),run_time=2);self.say('A quiet balance.')
        self.at('Imagine three pins');labels=VGroup(*[self.label(chr(65+i),p+UP*.35,'ink','detail') for i,p in enumerate(pins)]);self.add(labels)
        self.at('Each one pulls');arrows=VGroup(*[Arrow(center,center+1.1*(p-center)/r,buff=0,stroke_width=5,color=self.palette['secondary']) for p in pins]);self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.2),run_time=1)
        self.at('If the pulls do not cancel');self.play(junction.animate.shift(RIGHT*.45),FadeOut(arrows),run_time=.7);self.play(junction.animate.move_to(center),run_time=1)
        self.at('Watch what happens');self.play(FadeOut(lines),FadeOut(pinmarks),FadeOut(labels),run_time=.5);vectors=[3.0*(p-center)/r for p in pins];q=np.array([.52,-.2,0]);triangle=VGroup()
        for v in vectors:
            arrow=Arrow(q,q+v,buff=0,stroke_width=5,color=self.palette['secondary']);triangle.add(arrow);q=q+v
        self.play(LaggedStart(*[GrowArrow(a) for a in triangle],lag_ratio=.4),run_time=2);self.add(triangle)
        self.at('Each corner of that triangle');self.say('Equal arrows close a triangle.');corner=triangle[1].get_start();arc=Arc(radius=.4,start_angle=-PI/2,angle=-PI/3,arc_center=corner,color=self.palette['ink']);angle_label=self.label('60°',corner+[-.6,-.45,0],'ink','detail');self.add(arc,angle_label)
        self.at('But the pulls at the junction');self.play(FadeOut(arc),FadeOut(angle_label),run_time=.3);self.play(*[a.animate.shift(center-a.get_start()) for a in triangle],run_time=1.5)
        self.at('Their separation');self.say('120° between equal pulls.');self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.caption and m is not triangle],run_time=.4)
        anglemarks=VGroup(*[Arc(radius=.55,start_angle=a,angle=TAU/3,arc_center=center,stroke_color=self.palette['ink'],stroke_width=2) for a in angles]);self.add(anglemarks)
        self.at('Now bring the arrows back');self.add(lines,pinmarks);self.play(FadeOut(triangle),run_time=.7)
        self.at('No direction wins');self.say('Three pulls. No winner.')
        self.at('Between parallel plates, film area');self.say('Less length → less film area')
        self.at('For three pins forming');sides=VGroup(self.line(pins[0],pins[1],'secondary',4),self.line(pins[1],pins[2],'secondary',4));self.play(Create(sides),run_time=1);lengthlabels=VGroup(self.label('r = branch length',[0,-1.8,0],'ink','detail'),self.label('two sides: 2√3 r',[0,-2.4,0],'secondary','detail'),self.label('three branches: 3r',[0,-3,0],'primary','detail'));self.add(lengthlabels)
        self.at('shorter than connecting');self.play(FadeOut(sides),run_time=.6);self.say('3r < 2√3 r')
        self.at('not a promise');self.say('An ideal equilibrium model.')
        self.at('Change a film');self.play(FadeOut(anglemarks),FadeOut(lengthlabels),run_time=.3);self.say('Unequal tension → unequal angles');self.play(junction.animate.shift(UP*.4),run_time=1)
        self.at('A small meeting');self.play(junction.animate.move_to(center),run_time=1);self.say('Geometry in a meeting of films.');self.finish()
