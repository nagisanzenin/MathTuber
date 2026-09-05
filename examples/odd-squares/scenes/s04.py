from components import *

def tiles(n, color=BLUE):
    return VGroup(*[Square(side_length=.82, fill_color=color, fill_opacity=.75, stroke_color=INK, stroke_width=1.5).move_to([x*.87,y*.87,0]) for y in range(n) for x in range(n)]).move_to(ORIGIN)

def growth(n):
    old=tiles(n)
    old.shift(LEFT*.435+DOWN*.435)
    corner=old.get_corner(UR)
    edge=VGroup(*[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[0].get_x()+k*.87,old[-1].get_y()+.87,0]) for k in range(n+1)], *[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[-1].get_x()+.87,old[0].get_y()+k*.87,0]) for k in range(n)])
    return old,edge
class Scene4(NarratedScene):
    def construct(self):
        self.heading("THE GENERAL STEP", "An n × n square grows by one")
        old,border=growth(4)
        self.play(FadeIn(old))
        nlabel=MathTex("n^2",color=INK).move_to(old)
        self.add(nlabel)
        self.cue(.27)
        self.play(LaggedStart(*[FadeIn(t) for t in border[:4]],lag_ratio=.2),run_time=1.5)
        self.cue(.43)
        self.play(LaggedStart(*[FadeIn(t) for t in border[5:]],lag_ratio=.2),run_time=1.5)
        self.cue(.54)
        self.play(FadeIn(border[4],scale=1.4))
        eq=MathTex("n+n+1=2n+1",color=GOLD).shift(DOWN*3.5)
        self.cue(.64)
        self.play(Write(eq))
        self.finish()
