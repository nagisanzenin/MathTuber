from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        pts=[VectorizedPoint(x) for x in [(-2.6,-1.7,0),(-1.9,2.7,0),(2.5,1.6,0),(1.7,-1.5,0)]]
        def v():return [p.get_center() for p in pts]
        def mid():q=v();return [(q[i]+q[(i+1)%4])/2 for i in range(4)]
        outer=always_redraw(lambda:self.poly(*v(),opacity=.06));inner=always_redraw(lambda:self.poly(*mid(),color='accent',opacity=.5));dots=always_redraw(lambda:VGroup(*[Dot(x,radius=.1,color=self.palette['ink']) for x in mid()]));self.add(outer,inner,dots);self.play(pts[2].animate.move_to([1.4,3,0]),run_time=3)
        self.at('halfway along each edge');ticks=always_redraw(lambda:VGroup(*[self.label('½',x+UP*.27,'ink','detail').scale(.65) for x in mid()]));self.add(ticks)
        self.at('Try a completely different');self.play(pts[1].animate.move_to([-2.7,1.4,0]),pts[2].animate.move_to([2.6,2.7,0]),pts[3].animate.move_to([.7,-2,0]),run_time=3)
        self.at('Draw just one diagonal');q=v();diag=self.line(q[0],q[2],'secondary',5);self.play(Create(diag),FadeOut(ticks),run_time=1)
        self.at('A half size copy');big=self.poly(q[0],q[1],q[2],color='primary',opacity=.35);self.play(FadeIn(big),run_time=.5);self.play(big.animate.scale(.5,about_point=q[1]),run_time=2)
        self.at('parallel to the diagonal');m=mid();upper=self.line(m[0],m[1],'primary',8);self.play(Create(upper),run_time=.7);self.say('Same direction. Half the length.')
        self.at('Look below');small=self.poly(q[0],q[3],q[2],color='secondary',opacity=.3);self.play(FadeIn(small),run_time=.4);self.play(small.animate.scale(.5,about_point=q[3]),run_time=2);lower=self.line(m[3],m[2],'secondary',8);self.play(Create(lower),run_time=.6)
        self.at('Now draw the other');diag2=self.line(q[1],q[3],'muted',4);self.play(FadeOut(big),FadeOut(small),FadeOut(upper),FadeOut(lower),Create(diag2),run_time=1);sides=VGroup(self.line(m[1],m[2],'primary',8),self.line(m[3],m[0],'primary',8));self.play(Create(sides),run_time=1)
        self.at('That is a parallelogram');self.say('Crooked outside. Parallel inside.')
        self.at('Try pulling one corner inward');self.play(FadeOut(diag),FadeOut(diag2),FadeOut(sides),run_time=.5);self.play(pts[2].animate.move_to([-.8,.1,0]),run_time=3);self.finish()
