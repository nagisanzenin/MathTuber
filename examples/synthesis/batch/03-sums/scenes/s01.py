from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        cells=VGroup(*[Square(side_length=.6,stroke_color=INK,stroke_width=1).move_to([-1.8+j*.6,4.1-i*.6,0]) for i in range(6) for j in range(6)]);self.add(cells)
        heads=VGroup(*[txt(str(i+1),[-1.8+i*.6,4.8,0]) for i in range(6)],*[txt(str(i+1),[-2.5,4.1-i*.6,0]) for i in range(6)]);title=txt('two independent dice',[0,5.7,0],'claim');self.add(heads,title)
        self.at('Two fair');self.at('Every ordered');calc=txt('36 equally likely pairs',[0,-.3,0]);self.play(FadeIn(calc),run_time=.4)
        self.at('To total seven');self.play(cells[5].animate.set_fill(TEAL,.7),run_time=.5)
        self.at('Or two');self.play(*[cells[i*6+5-i].animate.set_fill(TEAL,.7) for i in range(1,6)],run_time=1);calc=self.replace_label(calc,txt('P(sum = 7) = 6/36',[0,-.3,0],'claim'))
        self.at('To total two');self.play(cells[0].animate.set_fill(CORAL,.8),run_time=.5);note=txt('P(sum = 2) = 1/36',[0,-1.4,0]);self.play(FadeIn(note),run_time=.4)
        self.at('Collect the pairs');self.play(FadeOut(VGroup(calc,note)),run_time=.2);bars=VGroup(*[Rectangle(width=.32,height=.24*n,fill_color=TEAL,fill_opacity=.7,stroke_width=0).move_to([-2+i*.4,-2+.12*n,0]) for i,n in enumerate([1,2,3,4,5,6,5,4,3,2,1])]);labels=txt('totals: 2     ← 7 →     12',[0,-2.7,0]);self.play(FadeIn(bars),FadeIn(labels),run_time=.7)
        self.at('For independent');self.at('This operation')
        self.at('Now use');self.play(FadeOut(VGroup(bars,labels,title)),run_time=.3);self.play(*[c.animate.set_fill(TEAL,0) for c in cells],run_time=.3);title=txt('one roll · copied result',[0,5.7,0],'claim');self.add(title)
        self.at('Each individual');self.play(*[cells[i*6+i].animate.set_fill(CORAL,.8) for i in range(6)],run_time=.8)
        self.at('The totals are');calc=txt('2, 4, 6, 8, 10, 12: each 1/6\nP(sum = 7) = 0',[0,-1.2,0],'claim');self.play(FadeIn(calc),run_time=.5);self.finish()
