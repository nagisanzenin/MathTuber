from scenes._shared.design import *
class Shot4(Stage):
 sid="s04"
 def construct(self):
  self.title('THE SECOND-PICK TRAP','You pick. I counter.')
  b=dice_board();self.add(b)
  choice=SurroundingRectangle(b[0],color=WHITE,buff=.1);counter=SurroundingRectangle(b[3],color=GOLD,buff=.14);self.add(choice)
  self.at('Choose blue');self.play(Create(counter),run_time=.7)
  self.at('Choose orange');self.play(Transform(choice,SurroundingRectangle(b[1],color=WHITE,buff=.1)),Transform(counter,SurroundingRectangle(b[0],color=GOLD,buff=.14)),run_time=.8)
  card=chip('BEATS MORE OFTEN ≠ GREATER THAN',GOLD,size=26)
  self.at('The trap');self.show(card)
  self.at('No loaded dice');self.show(text('An advantage, not a guaranteed win.',24,MUTED).move_to(DOWN*4.3))
  self.finish()
