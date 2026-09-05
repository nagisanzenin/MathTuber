from scenes._shared.design import *
class Shot3(Stage):
 sid="s03"
 def construct(self):
  self.title('TURN EDGES INTO DOORS','Follow a red–blue doorway.')
  m=mesh(4);self.add(m);coords,labels,tris,edges,rainbows,gates=mesh_data(4)
  doors=VGroup(*[Line(coords[a],coords[b],color=WHITE,stroke_width=4) for a,b in gates]);self.play(Create(doors),run_time=1)
  self.at('A rainbow triangle');idx=rainbows[0];tri=Polygon(*[coords[v] for v in tris[idx]],color=GOLD,fill_opacity=.2);self.show(tri)
  self.at('So a path');points,end=gate_path(4);trail=VMobject(color=GOLD,stroke_width=5).set_points_as_corners(points);self.play(Create(trail),run_time=3)
  self.at('Some paths');self.show(chip('0 OR 2 DOORS · RAINBOW HAS 1',WHITE,size=27))
  self.finish()
