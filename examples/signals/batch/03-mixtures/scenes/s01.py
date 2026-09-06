from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Better in both. Worse together?',5.25)
  heads=VGroup(self.label('TEAM A',[-1.65,4.1,0],'primary','claim'),self.label('TEAM B',[1.65,4.1,0],'secondary','claim'));self.add(heads)
  def bar(x,y,n,success,den=100):
   w=2.4*n/den;left=x-1.2
   bg=Rectangle(width=w,height=.42,fill_color=self.palette['surface'],fill_opacity=1,stroke_width=0).move_to([left+w/2,y,0]);fg=Rectangle(width=w*success/n,height=.42,fill_color=self.palette['primary'] if x<0 else self.palette['secondary'],fill_opacity=1,stroke_width=0).align_to(bg,LEFT).set_y(y)
   return VGroup(bg,fg)
  easy=VGroup(self.label('easy tasks',[0,3.2,0]),self.label('9 / 10 = 90%',[-1.65,2.5,0]),self.label('80 / 100 = 80%',[1.65,2.5,0]),bar(-1.65,1.85,10,9),bar(1.65,1.85,100,80))
  hard=VGroup(self.label('hard tasks',[0,.9,0]),self.label('20 / 100 = 20%',[-1.65,.2,0]),self.label('1 / 10 = 10%',[1.65,.2,0]),bar(-1.65,-.45,100,20),bar(1.65,-.45,10,1))
  legend=self.label('filled = success · full bar = attempts',[0,-1.65,0],role='detail')
  self.add(easy,hard)
  self.at('These are invented');self.play(FadeIn(legend),run_time=.5)
  self.at('On easy tasks, A succeeds');self.focus_outline(easy,run_time=.7)
  self.at('On hard tasks, A succeeds');self.focus_outline(hard,run_time=.7)
  self.at('A leads in both');self.focus_outline(easy[1]);self.focus_outline(hard[1])
  self.at('Now put the groups');self.say('Add counts before dividing',5.25);self.play(FadeOut(VGroup(*easy[:3],*hard[:3],legend)),run_time=.4)
  moving=VGroup(easy[3][1],hard[3][1],easy[4][1],hard[4][1]);targets=[]
  for x,counts,color in [(-1.65,[9,20],'primary'),(1.65,[80,1],'secondary')]:
   left=x-1.2
   for n in counts:
    w=2.4*n/110;targets.append(Rectangle(width=w,height=.42,fill_color=self.palette[color],fill_opacity=1,stroke_width=0).move_to([left+w/2,2,0]));left+=w
  self.play(*[Transform(a,b) for a,b in zip(moving,targets)],*[FadeOut(g[0]) for g in (easy[3],hard[3],easy[4],hard[4])],run_time=1.2)
  self.clear();self.add(self.caption,heads)
  totals=VGroup(self.label('29 / 110',[-1.65,2.9,0],'ink','claim'),self.label('81 / 110',[1.65,2.9,0],'ink','claim'),bar(-1.65,2,110,29,110),bar(1.65,2,110,81,110));self.play(FadeIn(totals),run_time=.7)
  self.at('The ranking reverses');rates=VGroup(self.label('26.4%',[-1.65,1.2,0],'primary','claim'),self.label('73.6%',[1.65,1.2,0],'secondary','claim'));self.play(FadeIn(rates),run_time=.6)
  self.at('The key is the mixture');mix=VGroup(self.label('mostly hard',[-1.65,-.2,0]),self.label('mostly easy',[1.65,-.2,0]));self.play(FadeIn(mix),run_time=.6)
  self.at('An overall rate');note=self.label('group size determines its weight',[0,-1.4,0]);self.play(FadeIn(note),run_time=.5)
  self.at('Give both teams');self.play(FadeOut(VGroup(totals,rates,mix,note)),run_time=.5);self.say('Same mix: half easy, half hard',5.25)
  eq=VGroup(self.label('(90% + 20%) / 2',[-1.65,2.7,0],role='detail'),self.label('(80% + 10%) / 2',[1.65,2.7,0],role='detail'),bar(-1.65,1.9,100,55),bar(1.65,1.9,100,45));self.play(FadeIn(eq),run_time=.7)
  self.at('The reversal disappears');rates=VGroup(self.label('55%',[-1.65,1,0],'primary','claim'),self.label('45%',[1.65,1,0],'secondary','claim'));self.play(FadeIn(rates),run_time=.6)
  self.at('This is Simpson');self.say("Simpson’s paradox",5.25)
  self.at('These totals alone');note=self.label('comparison ≠ explanation of cause',[0,-1.4,0]);self.play(FadeIn(note),run_time=.5);self.assert_safe(eq,rates,note);self.finish()
