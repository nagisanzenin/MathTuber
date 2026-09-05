from components import *

def tiles(n, color=BLUE):
    return VGroup(*[Square(side_length=.82, fill_color=color, fill_opacity=.75, stroke_color=INK, stroke_width=1.5).move_to([x*.87,y*.87,0]) for y in range(n) for x in range(n)]).move_to(ORIGIN)

def growth(n):
    old=tiles(n)
    old.shift(LEFT*.435+DOWN*.435)
    corner=old.get_corner(UR)
    edge=VGroup(*[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[0].get_x()+k*.87,old[-1].get_y()+.87,0]) for k in range(n+1)], *[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[-1].get_x()+.87,old[0].get_y()+k*.87,0]) for k in range(n)])
    return old,edge
class Scene1(NarratedScene):
    def construct(self):
        self.heading("ODD NUMBERS. SQUARE TOTALS.", "A proof you can build")
        equation=MathTex("1+3+5+7=16",color=GOLD).scale(1.05).shift(UP*3)
        self.play(Write(equation),run_time=1.2)
        grid=tiles(4)
        self.cue(.18)
        self.play(LaggedStart(*[FadeIn(t,scale=.6) for t in grid],lag_ratio=.1),run_time=2.4)
        side=Brace(grid,DOWN,color=GOLD)
        number=MathTex("4",color=GOLD).next_to(side,DOWN)
        self.cue(.55)
        self.play(GrowFromCenter(side),Write(number))
        why=Text("Why does this always work?",font_size=29,color=INK).shift(DOWN*4)
        self.cue(.77)
        self.play(FadeIn(why,shift=UP*.2))
        self.finish()
