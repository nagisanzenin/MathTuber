from scenes._shared.design import *
def fillings(n):
 if n==0:return [()]
 return [(a,)+rest for a in (1,2) if a<=n for rest in fillings(n-a)]
class Film(Stage):
 def strip(self,parts,center,unit=.46,outline_last=False):
  total=sum(parts)*unit;left=center[0]-total/2;g=VGroup()
  for i,k in enumerate(parts):
   tile=Rectangle(width=k*unit-.04,height=.38,stroke_color=self.palette['ink'],stroke_width=1.2,fill_color=self.palette['primary' if k==1 else 'secondary'],fill_opacity=1).move_to([left+k*unit/2,center[1],0]);left+=k*unit;g.add(tile)
  if outline_last:g.add(SurroundingRectangle(g[-1],color=self.palette['accent'],buff=.035,stroke_width=2))
  return g
 def construct(self):
  self.say('How many ways to fill a path?',5.25)
  path=VGroup(*[Square(.92,stroke_color=self.palette['muted'],stroke_width=2).move_to([-2+v,2.4,0]) for v in range(5)])
  tiles=VGroup(self.strip((1,),[-1.5,.4,0],.9),self.strip((2,),[1.1,.4,0],.9));self.add(path,tiles)
  self.at('For a path of one');self.play(FadeOut(path),FadeOut(tiles),run_time=.4)
  base=VGroup(self.label('length 1 → 1 way',[0,3.5,0]),self.strip((1,),[0,2.7,0],.8));self.play(FadeIn(base),run_time=.5)
  self.at('For two squares');two=VGroup(self.label('length 2 → 2 ways',[0,1.6,0]),self.strip((1,1),[-1.3,.7,0],.65),self.strip((2,),[1.3,.7,0],.65));self.play(FadeIn(two),run_time=.6)
  self.at('Instead of guessing');self.play(FadeOut(base),FadeOut(two),run_time=.4);self.say('Look at the last tile',5.25)
  lefthead=self.label('length 4',[-1.65,3.7,0]);righthead=self.label('length 3',[1.65,3.7,0]);self.add(lefthead,righthead)
  left=VGroup(*[self.strip(parts,[-1.9,2.8-i*.8,0]) for i,parts in enumerate(fillings(4))]);right=VGroup(*[self.strip(parts,[1.2,2.8-i*.8,0]) for i,parts in enumerate(fillings(3))])
  self.at('If a five square');self.play(FadeIn(left),run_time=.7)
  self.at('Every filling of four');fullleft=VGroup(*[self.strip(parts+(1,),[-1.67,2.8-i*.8,0],outline_last=True) for i,parts in enumerate(fillings(4))]);self.play(*[FadeIn(VGroup(g[-2],g[-1])) for g in fullleft],run_time=1);self.remove(left);self.add(fullleft);lefthead=self.replace_label(lefthead,self.label('ends with 1',[-1.65,3.7,0]))
  self.at('If it ends with a long');self.play(FadeIn(right),run_time=.7)
  self.at('Every filling of three');fullright=VGroup(*[self.strip(parts+(2,),[1.66,2.8-i*.8,0],outline_last=True) for i,parts in enumerate(fillings(3))]);self.play(*[FadeIn(VGroup(g[-2],g[-1])) for g in fullright],run_time=1);self.remove(right);self.add(fullright);righthead=self.replace_label(righthead,self.label('ends with 2',[1.65,3.7,0]))
  self.at('These two groups');self.focus_outline(fullleft);self.focus_outline(fullright)
  self.at('So the number for five');eq=self.label('5 + 3 = 8',[0,-1.9,0],'ink','claim');self.play(FadeIn(eq),run_time=.5)
  self.at('The counts grow');seq=self.label('1, 2, 3, 5, 8',[0,4.4,0],'primary');self.play(FadeIn(seq),run_time=.5)
  self.at('Add one more square');self.play(FadeOut(VGroup(fullleft,fullright,lefthead,righthead,eq,seq)),run_time=.5);self.say('One more square: length 6',5.25)
  ending1=self.strip((2,2,1,1),[0,2.8,0],.75,True);ending2=self.strip((2,2,2),[0,.8,0],.75,True)
  labels=VGroup(self.label('8 ways · ends with 1',[0,3.5,0]),self.label('5 ways · ends with 2',[0,1.5,0]));self.play(FadeIn(ending1),FadeIn(ending2),FadeIn(labels),run_time=.7)
  self.at('Thirteen in total');result=self.label('8 + 5 = 13',[0,-.5,0],'ink','claim');self.play(FadeIn(result),run_time=.6)
  self.add(self.label('one example from each ending group',[0,-2.65,0],role='detail'))
  self.at('These are Fibonacci');self.say('Fibonacci, without a spiral',5.25);rule=self.label('count(n) = count(n−1) + count(n−2)',[0,-1.7,0]);self.play(FadeIn(rule),run_time=.5)
  self.at('A number pattern');self.assert_safe(rule,result,labels);self.finish()
