from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        s=.073;origin=np.array([-3.066,-.9,0])
        def rect(x,y,w,h,col='surface'):
         return Rectangle(width=w*s,height=h*s,fill_color=self.palette[col],fill_opacity=.7,stroke_color=self.palette['ink'],stroke_width=2).move_to(origin+np.array([(x+w/2)*s,(y+h/2)*s,0]))
        board=rect(0,0,84,30);dims=VGroup(self.label('84',UP*2.0),self.label('30',LEFT*3.4+UP*.2));self.add(board,dims);self.play(Create(SurroundingRectangle(board,buff=.05,color=self.palette['primary'])),run_time=1)
        self.at('Guess ten');trial=VGroup(*[rect(x,y,10,10,'accent') for y in range(0,30,10) for x in range(0,80,10)]);self.play(LaggedStart(*[FadeIn(t) for t in trial],lag_ratio=.03),run_time=2);self.say('10 leaves a strip.')
        self.at('Cut off the biggest');self.play(FadeOut(trial),FadeOut(dims),board.animate.set_fill(opacity=0),run_time=.5);one=rect(0,0,30,30,'primary');self.play(FadeIn(one),run_time=1)
        self.at('Then another');two=rect(30,0,30,30,'primary');self.play(FadeIn(two),run_time=.8)
        self.at('twenty four by thirty rectangle');left=rect(60,0,24,30,'secondary');self.play(FadeIn(left),run_time=.7);self.say('84 = 2 × 30 + 24')
        self.at('removing whole thirty unit squares');self.play(one.animate.shift(UP*2.8),two.animate.shift(DOWN*2.8),run_time=2)
        self.at('common tile sizes have not changed');self.say('Same common tile sizes.')
        self.at('Remove a twenty four');sq=rect(60,6,24,24,'accent');strip=rect(60,0,24,6,'secondary');self.play(FadeOut(left),FadeIn(sq),FadeIn(strip),run_time=.8);self.play(sq.animate.shift(UP*2.3),run_time=1.3);self.say('30 = 24 + 6')
        self.at('six unit squares fill');tiles=VGroup(*[rect(x,0,6,6,'accent') for x in range(60,84,6)]);self.play(LaggedStart(*[FadeIn(t) for t in tiles],lag_ratio=.2),run_time=1.5);self.say('24 = 4 × 6')
        self.at('Six is the answer');self.say('Largest tile: 6 × 6')
        self.at('Work backward');self.play(one.animate.shift(DOWN*2.8),two.animate.shift(UP*2.8),sq.animate.shift(DOWN*2.3),run_time=2)
        self.at('Reveal the grid');grid=VGroup(*[self.line(origin+RIGHT*x*s,origin+RIGHT*x*s+UP*30*s,'ink',1.5) for x in range(0,85,6)],*[self.line(origin+UP*y*s,origin+UP*y*s+RIGHT*84*s,'ink',1.5) for y in range(0,31,6)]);self.play(Create(grid),run_time=2);self.finish()
