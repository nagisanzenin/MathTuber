from scenes._shared.design import *
class Shot4(Stage):
 sid="s04"
 def construct(self):
  self.title('REINFORCEMENT CHANGES EVERYTHING','Fair rules. Lopsided outcomes.')
  self.add(VGroup(urn(5,1).scale(.65).move_to([-1.8,1.8,0]),urn(1,5).scale(.65).move_to([1.8,1.8,0])))
  self.at('every possible number');self.show(equation(r'P(R_n=r)=\frac1{n+1}',y=-.1));self.show(text('r = 1, 2, …, n + 1',27,MUTED).move_to(DOWN*1.2))
  self.at('Those effects balance');card=chip('MORE ORDERS × SMALLER CHANCES',GOLD,size=26);self.show(card)
  self.at('Reinforcement turns');self.play(Transform(card,chip('EARLY LUCK → FUTURE ADVANTAGE',WHITE,size=27)),run_time=.8)
  self.finish()
