from scenes._shared.design import *
class Shot2(Stage):
 sid='s02'
 def construct(self):
  self.title('FOLLOW THE NUMBER','Your box starts a loop.')
  b=boxes().scale(.88).shift(UP*.6);self.add(b)
  path=[7,42,16,83];counter=text('PRISONER 7',28,GOLD,True).move_to(DOWN*2.75);self.add(counter)
  # Measured words from this narration: opens / follows / then / finally.
  for k,(label,cue) in enumerate(zip(path,[8.10,10.51,11.85,13.0])):
   self.wait(max(0,cue-self.renderer.time))
   actions=[b[label-1].animate.set_fill(BLUE,.9)]
   if k:actions.append(Create(Arrow(b[path[k-1]-1].get_center(),b[label-1].get_center(),color=GOLD,buff=.1).set_opacity(.7)))
   self.play(*actions,run_time=.25)
   if k==0:self.wait(max(0,9.35-self.renderer.time))
   result=path[(k+1)%4];card=chip(f'BOX {label}  →  NUMBER {result}',GOLD)
   if k==0:self.play(FadeIn(card),run_time=.35);current=card
   else:self.remove(current);self.add(card);current=card;self.wait(.35)
  self.at('Four openings');self.play(Transform(current,chip('FOUND 7 IN FOUR OPENINGS',GREEN)),run_time=.6)
  self.at('Because every number');self.show(text('A permutation is a collection of cycles.',23,MUTED).move_to(DOWN*4.4))
  self.finish()
