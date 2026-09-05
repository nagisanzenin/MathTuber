from components import *

def tiles(n, color=BLUE):
    return VGroup(*[Square(side_length=.82, fill_color=color, fill_opacity=.75, stroke_color=INK, stroke_width=1.5).move_to([x*.87,y*.87,0]) for y in range(n) for x in range(n)]).move_to(ORIGIN)

def growth(n):
    old=tiles(n)
    old.shift(LEFT*.435+DOWN*.435)
    corner=old.get_corner(UR)
    edge=VGroup(*[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[0].get_x()+k*.87,old[-1].get_y()+.87,0]) for k in range(n+1)], *[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[-1].get_x()+.87,old[0].get_y()+k*.87,0]) for k in range(n)])
    return old,edge
class Scene3(NarratedScene):
    def construct(self):
        self.heading("FOUR TILES → NINE", "The next border has five tiles")
        old,border=growth(2)
        self.play(FadeIn(old))
        self.cue(.18)
        self.play(LaggedStart(*[FadeIn(t,scale=.6) for t in border],lag_ratio=.3),run_time=3)
        eq=MathTex("4+5=3^2",color=GOLD).shift(DOWN*3.2)
        self.cue(.53)
        self.play(Write(eq))
        label=Text("Same square. One new border.",font_size=25,color=INK).shift(DOWN*4.3)
        self.cue(.79)
        self.play(FadeIn(label))
        self.finish()
