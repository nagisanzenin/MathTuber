from scenes._shared.design import *
class Shot3(Stage):
 sid="s03"
 def construct(self):
  self.title('THE GROUP SUCCEEDS IF…','No loop exceeds fifty.')
  a=VGroup(cycle_graph(48,1.25,[-1.7,.8,0],BLUE),cycle_graph(52,1.25,[1.7,.8,0],ORANGE));self.add(a)
  card=chip('52 MEMBERS → TOO LONG',ORANGE);self.show(card)
  self.at('Here, all three');b=VGroup(cycle_graph(38,1,[-2,1.1,0],BLUE),cycle_graph(34,1,[.2,1.1,0],GREEN),cycle_graph(28,1,[1.5,-1.1,0],PURPLE));self.play(ReplacementTransform(a,b),Transform(card,chip('38 + 34 + 28 → EVERYONE SUCCEEDS',GREEN,size=25)),run_time=1.3)
  self.at('The strategy does not improve');self.show(text('Individual chance stays ½.',27,MUTED).move_to(DOWN*4.35))
  self.finish()
