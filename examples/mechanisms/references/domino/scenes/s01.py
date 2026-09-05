from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        g=VGroup(*[Square(side_length=.61,fill_color=self.palette['primary' if (x+y)%2==0 else 'surface'],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=.5).move_to([(x-3.5)*.65,(y-3.5)*.65+.5,0]) for y in range(8) for x in range(8)]);self.add(g)
        self.at('Remove two opposite');self.play(FadeOut(g[0],shift=DL*.5),FadeOut(g[63],shift=UR*.5),run_time=1)
        self.at('one dark and one light');box=SurroundingRectangle(VGroup(g[1],g[2]),buff=.035,color=self.palette['secondary']);self.play(Create(box),run_time=.8)
        self.at('Keep every remaining square');self.play(FadeOut(box),run_time=.4)
        dark=[g[i] for i in range(64) if i not in (0,63) and (i%8+i//8)%2==0];light=[g[i] for i in range(64) if (i%8+i//8)%2==1]
        self.at('Move each dark square');pairs=[]
        for j,(a,b) in enumerate(zip(dark,light)):
         pos=np.array([-2.7+(j%5)*1.2,3.0-(j//5)*.83,0]);pairs.append((a,b,pos))
        self.play(LaggedStart(*[AnimationGroup(a.animate.scale(.68).move_to(pos),b.animate.scale(.68).move_to(pos+RIGHT*.43)) for a,b,pos in pairs],lag_ratio=.04),light[-2].animate.scale(.68).move_to(LEFT*.45+DOWN*2.8),light[-1].animate.scale(.68).move_to(RIGHT*.45+DOWN*2.8),run_time=4)
        self.at('these two light squares');self.play(Circumscribe(VGroup(*light[-2:]),color=self.palette['secondary']),run_time=1);self.say('30 pairs. 2 without partners.')
        self.at('not to make a legal tiling');self.say('Counting arrangement ≠ tiling',-3.7)
        self.at('rules out every arrangement');self.play(*[Indicate(x,color=self.palette['secondary']) for x in light[-2:]],run_time=1);self.finish()
