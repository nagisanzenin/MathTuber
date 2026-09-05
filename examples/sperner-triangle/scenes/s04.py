from scenes._shared.design import *
class Shot4(Stage):
 sid="s04"
 def construct(self):
  self.title('THE PARITY PROOF','One entrance cannot pair up.')
  m=mesh(4,True);self.add(m);coords,labels,tris,edges,rainbows,gates=mesh_data(4);boundary=[e for e,t in gates.items() if len(t)==1]
  bdoors=VGroup(*[Line(coords[a],coords[b],color=WHITE,stroke_width=7) for a,b in boundary]);self.play(Create(bdoors),run_time=1.2)
  self.at('You need an odd number');self.show(text(f'{len(boundary)} BOUNDARY ENTRANCES',29,GOLD,True).move_to(DOWN*2.45))
  self.at('Paths that connect');self.show(chip('PAIRS USE 2. ODD LEAVES 1.',WHITE,size=29))
  self.at('Its path must end');points,end=gate_path(4);target=Polygon(*[coords[v] for v in tris[end]],color=GOLD,fill_color=GOLD,fill_opacity=.3);self.play(Indicate(target,color=GOLD),run_time=1)
  self.finish()
