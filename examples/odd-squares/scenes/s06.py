from components import *

def tiles(n, color=BLUE):
    return VGroup(*[Square(side_length=.82, fill_color=color, fill_opacity=.75, stroke_color=INK, stroke_width=1.5).move_to([x*.87,y*.87,0]) for y in range(n) for x in range(n)]).move_to(ORIGIN)

def growth(n):
    old=tiles(n)
    old.shift(LEFT*.435+DOWN*.435)
    corner=old.get_corner(UR)
    edge=VGroup(*[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[0].get_x()+k*.87,old[-1].get_y()+.87,0]) for k in range(n+1)], *[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[-1].get_x()+.87,old[0].get_y()+k*.87,0]) for k in range(n)])
    return old,edge
class Scene6(NarratedScene):
    def construct(self):
        self.heading("ODD NUMBERS BUILD SQUARES", "Every border is the next odd number")
        colors=[BLUE,GOLD,CORAL,"#B5A2CE"]
        grid=tiles(4)
        for idx,tile in enumerate(grid):
            x,y=idx%4,idx//4
            tile.set_fill(colors[max(x,y)],opacity=.85)
        self.play(LaggedStart(*[FadeIn(t) for t in grid],lag_ratio=.07),run_time=2)
        eq=MathTex("1+3+\\cdots+(2n-1)=n^2",color=INK).scale(.82).shift(DOWN*3.4)
        self.cue(.53)
        self.play(Write(eq),run_time=2)
        end=Text("A sum you can see.",font_size=31,color=GOLD).shift(DOWN*4.6)
        self.cue(.84)
        self.play(FadeIn(end,shift=UP*.2))
        self.finish()
