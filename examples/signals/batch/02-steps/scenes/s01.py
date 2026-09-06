from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Downhill direction. Wrong distance?',5.25)
  ax=Axes(x_range=[-4,4,2],y_range=[0,16,4],x_length=5.8,y_length=4.7,axis_config={'color':self.palette['muted'],'include_tip':False}).move_to([0,1.3,0]);curve=ax.plot(lambda x:x*x,x_range=[-3.8,3.8],color=self.palette['primary']);dot=Dot(ax.c2p(2,4),radius=.12,color=self.palette['secondary']);zero=self.label('0',ax.c2p(0,0)+DOWN*.35);self.add(ax,curve,dot,zero,*[self.label(str(v),ax.c2p(v,0)+DOWN*.35,role="detail") for v in (-2,2)])
  formula=self.label('loss = x²',[0,4.4,0]);value=None;trail=VGroup()
  def jumps(eta,values):
   nonlocal value,trail
   self.remove(*trail);trail=VGroup();dot.move_to(ax.c2p(values[0],values[0]**2))
   if value is not None:self.remove(value)
   value=self.label('step size = '+str(eta),[0,-1.8,0]);self.add(value)
   for a,b in zip(values,values[1:]):
    line=Line(ax.c2p(a,a*a),ax.c2p(b,b*b),color=self.palette['accent'],stroke_width=2)
    self.play(Create(line),dot.animate.move_to(ax.c2p(b,b*b)),run_time=.65);trail.add(line)
  self.at('Here is a tiny');self.play(FadeIn(formula),run_time=.5)
  self.at('At any position');slope=self.label('slope = 2x',[0,-2.6,0]);self.play(FadeIn(slope),run_time=.5)
  self.at('Gradient descent subtracts');self.say('new x = x − step × 2x',5.25)
  self.at('With a step size of one quarter');jumps(.25,[2,1])
  self.at('Then one half Each update');jumps(.25,[1,.5])
  self.at('Each update halves');jumps(.25,[.5,.25,.125])
  self.at('Now use a step size');self.say('Crossing can still converge',5.25);jumps(.75,[2])
  self.at('Two becomes minus one');jumps(.75,[2,-1])
  self.at('then one half The point');jumps(.75,[-1,.5])
  self.at('The point crosses');jumps(.75,[.5,-.25,.125])
  self.at('With a step size of one, two');self.say('Same distance. No progress.',5.25);jumps(1,[2,-2,2,-2,2])
  self.at('Make the step even larger');self.say('The jumps grow',5.25);jumps(1.1,[2,-2.4,2.88,-3.456])
  self.at('For this particular loss');self.play(FadeOut(value),FadeOut(slope),run_time=.4);rule=self.label('new x = (1 − 2 × step) x',[0,-1.8,0],'ink','claim');self.play(FadeIn(rule),run_time=.5)
  self.at('We need that multiplier');self.say('Shrink the distance each time',5.25)
  self.remove(*trail);dot.move_to(ax.c2p(2,4))
  for a,b in zip([2,1,.5,.25],[1,.5,.25,.125]):
   line=Line(ax.c2p(a,a*a),ax.c2p(b,b*b),color=self.palette['accent'],stroke_width=2)
   self.play(Create(line),dot.animate.move_to(ax.c2p(b,b*b)),run_time=.5)
  self.at('So a positive step');bound=self.label('0 < step < 1',[0,-2.7,0],'primary','claim');self.play(FadeIn(bound),run_time=.5)
  self.at('Real models');self.assert_safe(rule,bound);self.finish()
