from components import *

def tiles(n, color=BLUE):
    return VGroup(*[Square(side_length=.82, fill_color=color, fill_opacity=.75, stroke_color=INK, stroke_width=1.5).move_to([x*.87,y*.87,0]) for y in range(n) for x in range(n)]).move_to(ORIGIN)

def growth(n):
    old=tiles(n)
    old.shift(LEFT*.435+DOWN*.435)
    corner=old.get_corner(UR)
    edge=VGroup(*[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[0].get_x()+k*.87,old[-1].get_y()+.87,0]) for k in range(n+1)], *[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[-1].get_x()+.87,old[0].get_y()+k*.87,0]) for k in range(n)])
    return old,edge
class Scene2(NarratedScene):
    def construct(self):
        self.heading("ONE TILE → FOUR", "Add an L-shaped border")
        old,border=growth(1)
        self.play(FadeIn(old))
        self.cue(.18)
        self.play(LaggedStart(*[FadeIn(t,shift=UP*.15) for t in border],lag_ratio=.45),run_time=2)
        eq=MathTex("1+3=2^2",color=GOLD).shift(DOWN*3)
        self.cue(.68)
        self.play(Write(eq))
        self.play(Indicate(border,color=CORAL),run_time=1.2)
        self.finish()
