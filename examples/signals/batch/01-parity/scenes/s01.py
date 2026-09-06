from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  data=[[1,0,1,1],[0,1,0,0],[1,1,0,1],[0,1,1,0]]
  self.say('One bit changed. Where?',5.25)
  cells={};digits={}
  for r in range(4):
   for c in range(4):
    pos=np.array([-1.65+1.05*c,3.5-1.05*r,0]);cells[r,c]=Square(.93,stroke_color=self.palette['muted'],stroke_width=1.5,fill_color=self.palette['surface'],fill_opacity=.65).move_to(pos);digits[r,c]=self.label(str(data[r][c]),pos)
  self.add(*cells.values(),*digits.values())
  self.at('Arrange the bits');self.say('Make each total even',5.25)
  rowbits=VGroup(*[self.label(str(sum(row)%2),[2.65,3.5-1.05*r,0],'primary') for r,row in enumerate(data)])
  colbits=VGroup(*[self.label(str(sum(data[r][c] for r in range(4))%2),[-1.65+1.05*c,-.95,0],'primary') for c in range(4)])
  rule=self.label('extra check bits',[0,-1.75,0],'primary');self.play(FadeIn(rowbits),FadeIn(rule),run_time=.6)
  self.at('Then do the same');self.play(FadeIn(colbits),run_time=.6)
  self.at('Now flip this bit');self.say('One row fails. One column fails.',5.25)
  self.play(FadeOut(digits[1,2]),run_time=.2);digits[1,2]=self.label('1',cells[1,2].get_center(),'secondary');self.play(FadeIn(digits[1,2]),run_time=.4)
  self.at('Its row');rh=SurroundingRectangle(VGroup(*[cells[1,c] for c in range(4)],rowbits[1]),color=self.palette['secondary'],buff=.1);self.play(Create(rh),run_time=.6)
  self.at('So does its column');ch=SurroundingRectangle(VGroup(*[cells[r,2] for r in range(4)],colbits[2]),color=self.palette['accent'],buff=.14);self.play(Create(ch),run_time=.6)
  self.at('Follow the failed');self.focus_outline(cells[1,2]);self.at('Flip it back');self.play(FadeOut(digits[1,2]),run_time=.2);digits[1,2]=self.label('0',cells[1,2].get_center());self.play(FadeIn(digits[1,2]),FadeOut(rh),FadeOut(ch),run_time=.5);self.say("Both checks are even again",5.25)
  self.at('This demonstration assumes');self.say('One data-bit error',5.25);note=self.label('check bits intact',[0,-2.6,0]);self.play(FadeIn(note),run_time=.5)
  self.at('Watch four bits');self.play(FadeOut(note),FadeOut(rule),run_time=.3);self.say('Four changes can hide',5.25)
  corners=[(0,0),(0,2),(2,0),(2,2)];marks=VGroup(*[SurroundingRectangle(cells[k],color=self.palette['secondary'],buff=.04) for k in corners]);self.play(Create(marks),run_time=.5)
  for k in corners:
   new=self.label(str(1-data[k[0]][k[1]]),cells[k].get_center(),'secondary');self.play(FadeOut(digits[k]),FadeIn(new),run_time=.35);digits[k]=new
  self.at('Every affected row');note=self.label('2 flips in each affected row',[0,-1.5,0]);self.play(FadeIn(note),run_time=.5)
  self.at('Every affected column');self.replace_label(note,self.label('2 flips in each affected column',[0,-1.5,0]))
  self.at('All the parity');self.say('Checks pass. Message changed.',5.25)
  self.at('Redundancy can reveal');self.assert_safe(VGroup(*cells.values()),self.caption);self.finish()
