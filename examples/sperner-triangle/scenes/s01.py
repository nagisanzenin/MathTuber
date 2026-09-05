from scenes._shared.design import *
class Shot1(Stage):
 sid="s01"
 def construct(self):
  self.title('SPERNER’S LEMMA','Try to erase every rainbow.')
  m=mesh(4);self.play(Create(m[1]),FadeIn(m[2]),run_time=1.4)
  self.at('Along each outer edge');self.show(chip('EDGES: ONLY THEIR CORNER COLORS',WHITE,size=25))
  self.at('Inside');self.play(Indicate(m[2],color=GOLD),run_time=.8)
  self.at('The challenge is impossible');self.play(FadeIn(mesh(4,True)[0]),run_time=.7)
  self.finish()
