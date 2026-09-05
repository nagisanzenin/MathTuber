from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        def sticker(i,pos,filled=True):
            shapes=[Circle(radius=.27),Square(side_length=.49),Triangle().scale(.32),RegularPolygon(n=5,radius=.3),RegularPolygon(n=6,radius=.3),Star(n=5,outer_radius=.31,inner_radius=.14)];s=shapes[i].set_stroke(self.palette['ink'],2).set_fill(self.palette['primary'] if filled else self.palette['surface'],1);return VGroup(RoundedRectangle(width=1.15,height=1.25,corner_radius=.12,fill_color=self.palette['surface'],fill_opacity=.3,stroke_color=self.palette['muted'],stroke_width=2),s,self.label(str(i+1),DOWN*.43,'ink','detail')).move_to(pos)
        positions=[[(i%3-1)*1.65,2.8-(i//3)*1.7,0] for i in range(6)];album=VGroup(*[sticker(i,positions[i],i<5) for i in range(6)]);self.add(album);self.say('One space left')
        def packet(i):
            pack=sticker(i,[0,-1.9,0]);self.play(FadeIn(pack,shift=UP*.3),run_time=.5);self.play(pack.animate.move_to([-2.4,-2.7,0]).scale(.7),run_time=.7);return pack
        self.at('Another packet opens');dup=packet(0)
        self.at('Then another duplicate');dup2=packet(3)
        self.at('six equally likely stickers');self.play(FadeOut(dup),FadeOut(dup2),run_time=.4);self.say('6 types • equally likely • independent')
        self.at('Our first sticker');self.play(*[Transform(album[i],sticker(i,positions[i],False)) for i in range(6)],run_time=.5);self.play(Transform(album[0],sticker(0,positions[0])),run_time=.6)
        self.at('With three spaces');self.play(*[Transform(album[i],sticker(i,positions[i],i<3)) for i in range(6)],run_time=.7);mark=VGroup(*[SurroundingRectangle(album[i],color=self.palette['secondary'],buff=.07) for i in range(3,6)]);self.play(Create(mark),run_time=.6)
        self.at('average wait is two');wait=self.label('3 of 6 help → average wait 2',[0,-1.4,0],'primary');self.add(wait)
        self.at('With just one space');self.play(FadeOut(mark),FadeOut(wait),*[Transform(album[i],sticker(i,positions[i],i<5)) for i in range(6)],run_time=.7);mark=SurroundingRectangle(album[5],color=self.palette['secondary'],buff=.07);self.add(mark)
        self.at('average wait is six');wait=self.label('1 of 6 helps → average wait 6',[0,-1.4,0],'secondary');self.add(wait)
        self.at('not mean the sixth');self.say('An average, not a deadline')
        self.at('call the remaining wait E');self.play(FadeOut(wait),FadeOut(mark),album.animate.scale(.36).move_to([2.0,-2.8,0]),run_time=.6);self.say('Let E be the average remaining wait');formula=self.label('E = 1 + ⅚ E',[0,1.4,0],'primary','claim').scale(1.7);self.add(formula)
        self.at('We always open one packet');box=SurroundingRectangle(formula,color=self.palette['secondary'],buff=.18);self.play(Create(box),run_time=.7)
        self.at('Five times out of six');self.add(self.label('duplicate → same situation',[0,.1,0],'ink','detail'))
        self.at('Subtract those five sixths');self.play(FadeOut(box),run_time=.4);formula=self.replace_label(formula,self.label('⅙ E = 1',[0,1.4,0],'primary','claim').scale(1.7))
        self.at('and E is six');formula=self.replace_label(formula,self.label('E = 6 packets',[0,1.4,0],'primary','claim').scale(1.7))
        self.at('Adding the average waits');self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.caption],run_time=.5);self.say('Every new sticker has its own wait');rows=VGroup(*[self.label(t,[0,3-j*.85,0],'primary','label') for j,t in enumerate(['6/6 + 6/5 + 6/4','+ 6/3 + 6/2 + 6/1','= 14.7 packets on average'])]);self.play(LaggedStart(*[FadeIn(t) for t in rows],lag_ratio=.4),run_time=1.5)
        self.at('Near the finish');self.say('Fewer new possibilities. A longer wait.');self.finish()
