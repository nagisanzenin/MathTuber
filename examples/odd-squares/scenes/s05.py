from components import *

def tiles(n, color=BLUE):
    return VGroup(*[Square(side_length=.82, fill_color=color, fill_opacity=.75, stroke_color=INK, stroke_width=1.5).move_to([x*.87,y*.87,0]) for y in range(n) for x in range(n)]).move_to(ORIGIN)

def growth(n):
    old=tiles(n)
    old.shift(LEFT*.435+DOWN*.435)
    corner=old.get_corner(UR)
    edge=VGroup(*[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[0].get_x()+k*.87,old[-1].get_y()+.87,0]) for k in range(n+1)], *[Square(side_length=.82,fill_color=GOLD,fill_opacity=.85,stroke_color=INK,stroke_width=1.5).move_to([old[-1].get_x()+.87,old[0].get_y()+k*.87,0]) for k in range(n)])
    return old,edge
class Scene5(NarratedScene):
    def construct(self):
        self.heading("THE SAME IDEA, IN ALGEBRA", "New area minus old area")
        eq=MathTex("(n+1)^2-n^2",color=INK).shift(UP*2)
        expanded=MathTex("n^2+2n+1-n^2",color=INK)
        result=MathTex("2n+1",color=GOLD).scale(1.4).shift(DOWN*2)
        self.play(Write(eq))
        self.cue(.35)
        self.play(Write(expanded))
        self.cue(.71)
        self.play(Write(result))
        caption=Text("Exactly the L-shaped border",font_size=28,color=GOLD).shift(DOWN*4)
        self.cue(.83)
        self.play(FadeIn(caption))
        self.finish()
