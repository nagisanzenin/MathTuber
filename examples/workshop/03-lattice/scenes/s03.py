from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        shape,grid,inside,boundary=lattice(self,[(0,0),(4,0),(4,4),(0,4)]);self.add(shape,grid,self.text('The count survives gluing.'))
        a=Polygon(point(0,0),point(4,0),point(4,4),fill_color=self.palette['primary'],fill_opacity=.25,stroke_color=self.palette['primary']);b=Polygon(point(0,0),point(4,4),point(0,4),fill_color=self.palette['secondary'],fill_opacity=.25,stroke_color=self.palette['secondary'])
        self.at('Split a square');self.play(FadeOut(shape),FadeIn(a),FadeIn(b),run_time=.7);self.play(a.animate.shift(DR*.22),b.animate.shift(UL*.22),run_time=1)
        self.at('two triangles meet');self.play(a.animate.shift(UL*.22),b.animate.shift(DR*.22),run_time=1)
        self.at('shared edge disappears');diagonal=Line(point(0,0),point(4,4),color=self.palette['accent'],stroke_width=7);self.show(diagonal);self.play(FadeOut(diagonal),run_time=.7)
        self.at('endpoints stay');ends=VGroup(*[Circle(radius=.15,color=self.palette['secondary']).move_to(point(*q)) for q in [(0,0),(4,4)]]);self.show(ends)
        self.at('points strictly between');middle=VGroup(*[Dot(point(i,i),radius=.12,color=self.palette['primary']) for i in [1,2,3]]);self.show(middle);self.note('Shared edge points become INSIDE.',-2.2)
        self.at('values add just like areas');self.rule('F(whole) = F(left) + F(right)',-3.1)
        self.at('not the whole proof');self.note('PROOF IDEA — full derivation in description',-4,'muted')
        self.finish()
