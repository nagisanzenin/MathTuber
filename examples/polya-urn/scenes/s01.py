from scenes._shared.design import *
class Shot1(Stage):
 sid="s01"
 def construct(self):
  self.title('PÓLYA’S URN','Early luck changes the odds.')
  u=urn(1,1);self.add(u)
  self.at('Draw one');ball=Dot([-.35,.2,0],radius=.25,color=ORANGE);self.play(ball.animate.move_to([0,2.75,0]),run_time=.8)
  self.at('return it');new=urn(2,1);self.play(FadeOut(ball),ReplacementTransform(u,new),run_time=.8);u=new
  self.at('A color that gets ahead');new=urn(3,1);self.play(ReplacementTransform(u,new),run_time=.8);u=new
  self.show(equation(r'\frac12\;\longrightarrow\;\frac23\;\longrightarrow\;\frac34'))
  self.at('But this is');self.show(text('Draw · replace · add the same color',24,MUTED).move_to(DOWN*4.4))
  self.finish()
