from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Which pairing makes the largest total?');xs=[-2,0,2];top=VGroup(*[self.card(str(v),[x,3.2,0]) for x,v in zip(xs,[1,2,3])]);bot=VGroup(*[self.card(str(v),[x,1.1,0],'secondary') for x,v in zip(xs,[6,4,2])]);links=VGroup(*[self.line([x,2.7,0],[x,1.6,0],'ink',2) for x in xs]);self.add(top,bot,links)
  self.at('Start by matching');calc=self.label('1 × 6 + 2 × 4 + 3 × 2',[0,-.4,0]);self.play(FadeIn(calc),run_time=.4)
  self.at('The total is twenty');total=self.label('20',[0,-1.4,0],'secondary','claim');self.add(total)
  self.at('Now exchange');self.remove(calc,total);self.play(Swap(bot[0],bot[2],path_arc=PI/2),run_time=1.5)
  self.at('The total becomes');calc=self.label('1 × 2 + 2 × 4 + 3 × 6',[0,-.4,0]);total=self.label('28',[0,-1.4,0],'primary','claim');self.add(calc,total)
  self.at('The difference between three');self.say('The gain comes from two differences');self.remove(calc,total);self.add(self.label('(3 − 1) × (6 − 2) = 8',[0,-.5,0],'accent','claim'))
  self.at('In general');self.wipe();self.say('A local exchange proves the rule');self.add(self.label('a ≤ b       c ≤ d',[0,3.4,0]),self.label('same order:  ac + bd',[0,2.2,0],'primary'),self.label('crossed:       ad + bc',[0,1.2,0],'secondary'))
  self.at('The gain is the product');self.add(self.label('(ac + bd) − (ad + bc)',[0,-.1,0]),self.label('= (b − a)(d − c) ≥ 0',[0,-1.1,0],'accent','claim'))
  self.at('Keep removing reversed');self.say('Same order: maximum');self.at('Opposite orders');self.add(self.label('Opposite order: minimum',[0,-2,0]))
  self.at('If two numbers');self.wipe();self.say('Equal entries make the exchange neutral');self.add(self.label('a = b',[0,3,0],'primary','claim'),self.label('(b − a)(d − c) = 0',[0,1.7,0],'accent','claim'),self.label('No gain · no loss',[0,.3,0]));self.finish()
