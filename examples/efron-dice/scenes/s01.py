from scenes._shared.design import *
class Shot1(Stage):
 sid="s01"
 def construct(self):
  self.title('EFRON’S DICE','There is no best die.')
  b=dice_board();self.play(LaggedStart(*[FadeIn(d,scale=.8) for d in b],lag_ratio=.15),run_time=1.3)
  card=chip('A → B → C → D → A',GOLD);self.show(card)
  self.at('That sounds impossible');self.play(Indicate(b[0],color=BLUE),Indicate(b[3],color=GREEN),run_time=1)
  self.at('These are Efron');self.play(Transform(card,chip('NONTRANSITIVE DICE',WHITE)),run_time=.6)
  self.at('Every face');self.show(text('Six equally likely faces per die',24,MUTED).move_to(DOWN*4.35))
  self.finish()
