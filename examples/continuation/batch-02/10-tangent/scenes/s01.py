from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Let the tangent improve the guess');ax=Axes(x_range=[0,2.5,.5],y_range=[-2,4,1],x_length=5,y_length=4.8,tips=False,axis_config={'color':self.palette['ink']}).move_to(UP*1.6);curve=ax.plot(lambda x:x*x-2,x_range=[0,2.4],color=self.palette['primary']);self.add(ax,curve,self.label('y = x² − 2',[0,4.3,0]))
  self.at('Start at x equals two');point=Dot(ax.c2p(2,2),radius=.11,color=self.palette['secondary']);self.add(point,self.label('start: 2',[0,-1.4,0]))
  self.at('Follow the tangent');t=ax.plot(lambda x:4*x-6,x_range=[1,2.35],color=self.palette['accent']);self.play(Create(t),run_time=1)
  self.at('The next guess');marker=Dot(ax.c2p(1.5,0),radius=.1,color=self.palette['accent']);self.play(FadeIn(marker),run_time=.5)
  self.at('At that point');self.play(point.animate.move_to(ax.c2p(1.5,.25)),FadeOut(t),run_time=.7);t=ax.plot(lambda x:3*x-4.25,x_range=[.9,2],color=self.palette['accent']);self.play(Create(t),run_time=.7)
  self.at('Our new guess');self.play(marker.animate.move_to(ax.c2p(17/12,0)),run_time=.6);self.add(self.label('2 → 1.5 → 1.4167…',[0,-2.2,0],'primary'))
  self.at('Each step replaces');self.say('Solve the tangent, then repeat')
  self.at('This is Newton');self.wipe();self.say('Newton’s method');self.add(self.label('x next = x − f(x) / f′(x)',[0,3,0],'ink','claim'))
  self.at('For this curve');self.add(self.label('= (x + 2/x) / 2',[0,1.6,0],'primary','claim'),self.label('2 → 3/2 → 17/12 → … → √2',[0,.1,0]))
  self.at('But a tangent');self.say('Local approximation, not a global guarantee')
  self.at('Start at zero');self.wipe();self.say('A flat tangent can stop the method');self.add(ax,curve,Dot(ax.c2p(0,-2),radius=.12,color=self.palette['secondary']));self.play(Create(ax.plot(lambda x:-2,x_range=[0,2.4],color=self.palette['accent'])),run_time=.8)
  self.at('The tangent is horizontal');self.add(self.label('f′(0) = 0 · cannot divide by zero',[0,-1.7,0],'secondary'));self.finish()
