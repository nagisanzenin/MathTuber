from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        from mathtuber.tiled_paths import connected_paths,tile_arcs
        import random
        rng=random.Random(23);rows=[[rng.randrange(2) for c in range(7)] for r in range(7)];paths=connected_paths(rows);O=np.array([-3.5,-2.5,0]);TEAL=self.palette['primary'];CORAL=self.palette['secondary'];INK=self.palette['ink']
        def place(p):return np.array(p)+O
        def arc_line(a,color=TEAL,width=5):return VMobject(stroke_color=color,stroke_width=width).set_points_as_corners([place(a.point(j/30)) for j in range(31)])
        def route_line(p,color=TEAL,width=4):return VMobject(stroke_color=color,stroke_width=width).set_points_as_corners([place(a.point(j/30)) for a in p.arcs for j in range(31)])
        tiles=VGroup(*[Square(side_length=1,fill_color='#E2D6BE' if (r+c)%2 else '#EEE3D0',fill_opacity=1,stroke_color='#CBBFA8',stroke_width=.8).move_to(place((c+.5,r+.5,0))) for r in range(7) for c in range(7)]);lines=VGroup(*[route_line(p) for p in paths]);self.add(tiles,lines)
        route=max((p for p in paths if not p.closed),key=lambda p:len(p.arcs));q=ValueTracker(0);trace=self.trace_curve(lambda t:place(route.point(t)),q.get_value,samples=len(route.arcs)*24+1,color='secondary',stroke_width=7);dot=always_redraw(lambda:Dot(place(route.point(q.get_value())),radius=.08,color=INK));self.add(trace,dot)
        self.at('Follow one line');self.play(q.animate.set_value(.3),run_time=2.3,rate_func=linear);self.at('It bends');self.play(q.animate.set_value(.65),run_time=3,rate_func=linear);self.at('A whole pattern');self.play(q.animate.set_value(1),run_time=2.5,rate_func=linear)
        self.at('Lift a single');self.play(FadeOut(trace),FadeOut(dot),lines.animate.set_stroke(opacity=.16),run_time=.4)
        r=c=3;unit=VGroup(tiles[r*7+c].copy(),*[arc_line(a) for a in tile_arcs(c,r,rows[r][c])]);self.add(unit);self.play(unit.animate.scale(3).move_to([0,1,0]),run_time=1.2)
        self.at('Two curved strokes');marks=VGroup(*[Dot([x,y,0],radius=.085,color=CORAL) for x,y in [(0,2.5),(1.5,1),(0,-.5),(-1.5,1)]]);self.play(FadeIn(marks),run_time=.4)
        self.at('Turn the tile');self.play(Rotate(unit,PI/2,about_point=[0,1,0]),run_time=1.5)
        self.at('The curves change');claim=self.label('same four meeting places',[0,-3.2,0],role='claim');self.play(FadeIn(claim),run_time=.4)
        self.at('Put the tile back');self.play(Rotate(unit,-PI/2,about_point=[0,1,0]),run_time=.7);self.play(FadeOut(marks),FadeOut(claim),unit.animate.scale(1/3).move_to(place((3.5,3.5,0))),run_time=.9);self.remove(unit)
        # Enlarge an actual pair of neighboring arcs, retaining the board behind it.
        a,b=route.arcs[1:3];join=place(a.point(1));pair=VGroup(arc_line(a,CORAL,7),arc_line(b,INK,7));pair.scale(3,about_point=join).shift(np.array([0,1,0])-join);seam=DashedLine([-2,1,0],[2,1,0],color='#A99E87',stroke_width=2)
        # Seam orientation follows the actual shared edge.
        if a.end[0]%2==0:seam.rotate(PI/2,about_point=[0,1,0])
        self.add(seam);self.at('A curve arrives');self.play(Create(pair[0]),run_time=1.5);self.at('Exactly one curve');self.play(Create(pair[1]),run_time=1.6);self.at('There is no loose');claim=self.label('one way in · one way onward',[0,-3.2,0],role='claim');self.play(FadeIn(claim),run_time=.4)
        self.at('Now follow');self.play(FadeOut(pair),FadeOut(seam),FadeOut(claim),lines.animate.set_stroke(opacity=1),run_time=.7)
        loop=max((p for p in paths if p.closed),key=lambda p:len(p.arcs));loopline=route_line(loop,CORAL,7)
        self.at('It can return');self.play(Create(loopline),run_time=3,rate_func=linear)
        self.at('Or it can');edgeline=route_line(route,INK,6);self.play(Create(edgeline),run_time=2.3,rate_func=linear)
        self.at('On a finite');claim=self.label('a loop, or the outer edge',[0,-3.2,0],role='claim');self.play(FadeIn(claim),run_time=.4)
        self.at('Turn a different');self.play(FadeOut(loopline),FadeOut(edgeline),FadeOut(claim),run_time=.3)
        # Discrete before/after re-pairing: rotate the two arcs in place, then rebuild graph.
        r,c=2,2;oldarcs=VGroup(*[arc_line(a) for a in tile_arcs(c,r,rows[r][c])]); 
        self.play(FadeOut(lines),run_time=.2);other=VGroup(*[arc_line(a) for rr in range(7) for cc in range(7) if (rr,cc)!=(r,c) for a in tile_arcs(cc,rr,rows[rr][cc])]);self.add(other,oldarcs);self.play(Rotate(oldarcs,PI/2,about_point=place((c+.5,r+.5,0))),run_time=1.7);rows[r][c]=1-rows[r][c]
        self.at('The same midpoint');self.remove(other,oldarcs);newpaths=connected_paths(rows);lines=VGroup(*[route_line(p) for p in newpaths]);self.add(lines)
        self.at('This is a Truchet');claim=self.label('Truchet tiles',[0,-3.2,0],role='claim');self.play(FadeIn(claim),run_time=.4)
        self.at('A little agreement');newroute=max(newpaths,key=lambda p:len(p.arcs));self.play(Create(route_line(newroute,CORAL,6)),run_time=3.3,rate_func=linear);self.finish()
