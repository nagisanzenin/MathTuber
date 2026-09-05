from scenes._shared.design import *
class Shot2(Stage):
 sid="s02"
 def construct(self):
  self.title('RECOLOR THE INTERIOR','The count stays odd.')
  m=mesh(4,True);self.add(m);counter=text(f'{len(mesh_data(4)[4])} RAINBOW TRIANGLE',31,GOLD,True).move_to(DOWN*2.5);self.add(counter)
  self.at('Watch these legal colorings');
  for seed in [8,12,21,33,44]:
   new=mesh(seed,True);self.play(ReplacementTransform(m,new),Transform(counter,text(f'{len(mesh_data(seed)[4])} RAINBOW TRIANGLES',31,GOLD,True).move_to(DOWN*2.5)),run_time=.7);m=new
  self.at('This is not a rule');self.show(chip('ODD CAN NEVER BE ZERO.',GOLD))
  self.finish()
