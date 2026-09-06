from manim import *
from mathtuber.tiled_paths import connected_paths, tile_arcs
import components
import json, random
from pathlib import Path
components.PROFILE=json.loads((Path(components.__file__).parent/'profiles/ivisualizethings-workshop.json').read_text())
config.frame_width=9
config.frame_height=16
config.pixel_width=540
config.pixel_height=960
config.frame_rate=20

class Prototype(components.WorkshopScene):
    def construct(self):
        rng=random.Random(23)
        rows=[[rng.randrange(2) for c in range(7)] for r in range(7)]
        paths=connected_paths(rows)
        shift=np.array([-3.5,-2.6,0])
        def place(p):return np.array(p)+shift
        def stroke(path,color='primary',width=5):
            points=[place(p) for a in path.arcs for p in [a.point(j/20) for j in range(21)]]
            return VMobject(stroke_color=self.palette[color],stroke_width=width).set_points_as_corners(points)
        tiles=VGroup(*[Square(side_length=.99,fill_color='#E2D6BE' if (r+c)%2 else '#EEE3D0',fill_opacity=1,stroke_color='#CBBFA8',stroke_width=.6).move_to(place((c+.5,r+.5,0))) for r in range(7) for c in range(7)])
        background=VGroup(*[stroke(p,width=4) for p in paths]);self.add(tiles,background)
        heading=self.lettering('A pattern that keeps going',role='claim').move_to(UP*5.5);self.add(heading)
        route=max((p for p in paths if not p.closed),key=lambda p:len(p.arcs))
        q=ValueTracker(0);trace=self.trace_curve(lambda t:place(route.point(t)),q.get_value,samples=len(route.arcs)*24+1,color='secondary',stroke_width=7);dot=always_redraw(lambda:Dot(place(route.point(q.get_value())),radius=.08,color=self.palette['ink']));self.add(trace,dot)
        self.play(q.animate.set_value(1),run_time=5,rate_func=linear);self.wait(.6)
        self.play(FadeOut(trace),FadeOut(dot),background.animate.set_stroke(opacity=.18),run_time=.6)
        # Lift one identified tile from the pattern; keep the field as context.
        r=c=3
        unit=VGroup(tiles[r*7+c].copy(),*[VMobject(stroke_color=self.palette['primary'],stroke_width=5).set_points_as_corners([place(a.point(j/30)) for j in range(31)]) for a in tile_arcs(c,r,rows[r][c])])
        self.add(unit);self.play(unit.animate.scale(3).move_to([0,.9,0]),run_time=1.3)
        heading=self.replace_label(heading,self.lettering('One tile. Two ways to turn.',role='claim').move_to(UP*5.5))
        marks=VGroup(*[Dot([x,y,0],radius=.09,color=self.palette['secondary']) for x,y in [(0,2.4),(1.5,.9),(0,-.6),(-1.5,.9)]])
        self.play(FadeIn(marks),run_time=.4);self.wait(1)
        self.play(Rotate(unit,PI/2,about_point=[0,.9,0]),run_time=2);self.wait(.8)
        caption=self.lettering('The joins stay at the edge midpoints.',max_width=7).move_to(DOWN*3.7);self.play(FadeIn(caption),run_time=.4);self.wait(2)
        # Return to the original orientation, then restore the original unit.
        self.play(Rotate(unit,-PI/2,about_point=[0,.9,0]),run_time=1);self.play(FadeOut(marks),FadeOut(caption),unit.animate.scale(1/3).move_to(place((3.5,3.5,0))),run_time=1.2);self.remove(unit)
        self.play(background.animate.set_stroke(opacity=1),run_time=.5)
        heading=self.replace_label(heading,self.lettering('Every inner join has a way onward.',role='claim').move_to(UP*5.5))
        # Show a local continuation through a seam, not only a complete route.
        a,b=route.arcs[1:3];local=VGroup(*[VMobject(stroke_color=self.palette['secondary'],stroke_width=8).set_points_as_corners([place(arc.point(j/30)) for j in range(31)]) for arc in (a,b)])
        seam=Circle(radius=.22,color=self.palette['ink'],stroke_width=2).move_to(place(a.point(1)))
        self.play(Create(local),Create(seam),run_time=2);self.wait(1.5);self.play(FadeOut(local),FadeOut(seam),run_time=.5)
        loop=max((p for p in paths if p.closed),key=lambda p:len(p.arcs));loopline=stroke(loop,'secondary',7)
        heading=self.replace_label(heading,self.lettering('A loop, or a journey to the edge.',role='claim').move_to(UP*5.5))
        self.play(Create(loopline),run_time=2.5,rate_func=linear);self.wait(.8)
        edgeline=stroke(route,'ink',6);self.play(Create(edgeline),run_time=4,rate_func=linear);self.wait(2)
