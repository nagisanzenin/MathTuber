from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('A shortcut. A slower journey?',5.25)
  S=np.array([-2.55,1.35,0]);A=np.array([0,3.4,0]);B=np.array([0,-.7,0]);T=np.array([2.55,1.35,0])
  edges=VGroup(self.line(S,A,width=6),self.line(A,T,'secondary',6),self.line(S,B,'secondary',6),self.line(B,T,width=6))
  nodes=VGroup(*[Dot(p,radius=.13,color=self.palette['ink']) for p in (S,A,B,T)])
  names=VGroup(self.label('start',S+LEFT*.1+DOWN*.45,role='detail'),self.label('finish',T+RIGHT*.05+DOWN*.45,role='detail'))
  count=self.label('4,000 drivers',[0,4.4,0]);self.add(edges,nodes,names,count)
  positions=[[-1.6,2.9,0],[1.6,2.9,0],[-1.6,-.25,0],[1.6,-.25,0]]
  costs=VGroup(*[self.label(s,p,'primary' if i in (0,3) else 'secondary',role='detail') for i,(s,p) in enumerate(zip(['n / 100','45 min','45 min','n / 100'],positions))])
  def update_cost(a,b):
   nonlocal costs
   new=VGroup(*[self.label(s,p,'primary' if i in (0,3) else 'secondary',role='detail') for i,(s,p) in enumerate(zip([a,'45 min','45 min',b],positions))]);self.play(FadeOut(costs),FadeIn(new),run_time=.4);costs=new
  def travel(points,color='accent'):
   dot=Dot(points[0],radius=.1,color=self.palette[color]);self.add(dot)
   for p in points[1:]:self.play(dot.animate.move_to(p),run_time=.6,rate_func=linear)
   self.remove(dot)
  self.at('The two teal');self.play(FadeIn(costs),run_time=.6);definition=self.label('n = drivers on that road section',[0,-2,0]);self.add(definition)
  self.at('Without a shortcut');self.remove(definition);self.say('2,000 drivers on each route',5.25);update_cost('20 min','20 min');travel([S,A,T]);travel([S,B,T])
  self.at('Sixty five minutes altogether');total=self.label('20 + 45 = 65 min',[0,-2,0],'ink','claim');self.play(FadeIn(total),run_time=.6)
  self.at('Now connect');total=self.replace_label(total,self.label('before: 65 min',[0,-2,0],'ink','claim'));connector=Arrow(A,B,buff=.18,color=self.palette['accent'],stroke_width=5);zero=self.label('0 min',[.55,1.4,0],'ink',role='detail');self.play(GrowArrow(connector),FadeIn(zero),run_time=.8);self.say('A zero-minute connector',5.25)
  self.at('A teal section never');update_cost('≤ 40 min','≤ 40 min')
  self.at('So each driver');travel([S,A,B,T]);self.play(edges[1].animate.set_opacity(.2),edges[2].animate.set_opacity(.2),run_time=.5)
  self.at('Everyone makes');self.say('4,000 drivers on both teal roads',5.25);update_cost('40 min','40 min');travel([S,A,B,T])
  self.at('Forty plus forty is eighty');new=self.label('40 + 40 = 80 min',[0,-2,0],'secondary','claim');self.replace_label(total,new);total=new
  self.at('One driver cannot');self.say('Switch alone? 85 minutes.',5.25);travel([S,A,T],'secondary')
  self.at('The old sixty five');self.say('Coordinate: the old route still exists',5.25);self.play(connector.animate.set_opacity(.2),zero.animate.set_opacity(.2),edges[1].animate.set_opacity(1),edges[2].animate.set_opacity(1),run_time=.6);update_cost('20 min','20 min');self.replace_label(total,self.label('20 + 45 = 65 min',[0,-2,0],'primary','claim'))
  self.at('They changed the incentives');self.say('Feasible is not the same as stable',5.25)
  self.at('This is Braess');self.assert_safe(edges,count);self.finish()
