from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        r=2.7;c=UP*.45;disk=Circle(radius=r,fill_color=self.palette['accent'],fill_opacity=.48,stroke_color=self.palette['ink'],stroke_width=3).move_to(c);self.add(disk)
        # Line represented as y=m*x+b in pizza-local coordinates.
        def ends(m,b):
         roots=np.roots([1+m*m,2*m*b,b*b-r*r]);return [c+np.array([float(x),float(m*x+b),0]) for x in sorted(roots)]
        def cut(m,b,col='ink'):return self.line(*ends(m,b),col,5)
        one=cut(0,0);two=cut(1.2,0);third=cut(-.8,0);self.play(Create(one),Create(two),Create(third),run_time=2)
        self.at('Six is easy');self.say('3 cuts → 6 pieces?')
        self.at('slide the last cut');new=cut(-.8,.8);self.play(Transform(third,new),run_time=2);tiny=self.poly(c,c+RIGHT*1,c+np.array([.4,.48,0]),color='primary',opacity=.8);self.play(FadeIn(tiny),run_time=.5);self.say('3 cuts → 7 pieces')
        self.at('Follow the last cut');e=ends(-.8,.8);walker=Dot(e[0],radius=.13,color=self.palette['secondary']);self.add(walker);self.play(walker.animate.move_to(e[1]),run_time=3,rate_func=linear)
        self.at('three regions');xs=[e[0],c+np.array([.4,.48,0]),c+np.array([1,0,0]),e[1]];sections=VGroup(*[self.line(xs[i],xs[i+1],['primary','secondary','primary'][i],10) for i in range(3)]);self.play(FadeOut(walker),Create(sections),run_time=.8);self.say('2 crossings → 3 new pieces')
        self.at('crossings merge');self.play(FadeOut(sections),FadeOut(tiny),Transform(third,cut(-.8,0)),run_time=1.2)
        self.at('Now try a fourth');self.play(Transform(third,cut(-.8,.8)),run_time=.8);four=cut(-.25,-.5,'secondary');self.play(Create(four),run_time=1.2)
        self.at('three different points');crosses=[(-2,0),(-.5/1.45,1.2*(-.5/1.45)),(1.3/.55,-.25*(1.3/.55)-.5)];marks=VGroup(*[Dot(c+np.array([x,y,0]),radius=.11,color=self.palette['ink']) for x,y in crosses]);self.play(FadeIn(marks),run_time=.7)
        self.at('new cut into four sections');ep=ends(-.25,-.5);points=[ep[0]]+[c+np.array([x,y,0]) for x,y in sorted(crosses)]+[ep[1]];parts=VGroup(*[self.line(points[i],points[i+1],['primary','secondary','primary','secondary'][i],9) for i in range(4)]);self.play(Create(parts),run_time=1);self.say('7 + 4 = 11');self.add(*[self.label(str(i+1),(points[i]+points[i+1])/2+UP*.3,'ink','detail').scale(.75) for i in range(4)])
        self.at('cannot cross each');self.play(*[Indicate(x) for x in marks],run_time=1)
        self.at('Five old region sections');self.say('Next maximum: 11 + 5 = 16');self.finish()
