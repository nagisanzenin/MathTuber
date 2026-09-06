from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Check a product using its digits');self.add(self.label('247 × 3 = 741 ?',[0,2,0],'ink','claim'))
  self.at('Take two hundred');self.wipe();self.say('Keep only the remainder after nines');cards=VGroup(*[self.card(s,[x,2.7,0],w=1.6) for x,s in zip([-2,0,2],['2 × 100','4 × 10','7 × 1'])]);self.add(cards)
  self.at('A hundred leaves');self.add(self.label('100 = 11 × 9 + 1',[0,1.2,0]));self.at('So does ten');self.add(self.label('10 = 1 × 9 + 1',[0,.2,0]))
  self.at('Replace each hundred');new=VGroup(*[self.card(s,[x,2.7,0],w=1.6) for x,s in zip([-2,0,2],['2 × 1','4 × 1','7 × 1'])]);self.play(FadeOut(cards),FadeIn(new),run_time=.8)
  self.at('Our digit sum');self.add(self.label('2 + 4 + 7 = 13 → remainder 4',[0,-1.2,0],'primary'))
  self.at('Now check');self.wipe();self.say('The two sides must agree');self.add(self.label('247 × 3',[0,3,0],'ink','claim'),self.label('4 × 3 = 12 → remainder 3',[0,1.8,0],'primary'))
  self.at('The proposed answer');ans=self.label('741: 7 + 4 + 1 = 12 → 3',[0,.2,0],'primary');self.add(ans)
  self.at('Change the answer');self.remove(ans);ans=self.label('742: 7 + 4 + 2 = 13 → 4',[0,.2,0],'secondary');self.add(ans)
  self.at('The remainders disagree');self.add(self.label('Mismatch proves an error',[0,-1.3,0],'secondary','claim'))
  self.at('But passing is not proof');self.wipe();self.say('A wrong answer can still pass');digits=VGroup(*[self.card(str(v),[x,2.6,0]) for x,v in zip([-1.4,0,1.4],[7,4,1])]);self.add(digits)
  self.at('Swap the last two');self.play(Swap(digits[1],digits[2],path_arc=PI/2),run_time=1.2)
  self.at('Seven hundred fourteen');self.add(self.label('7 + 1 + 4 = 12 → remainder 3',[0,.9,0],'primary'),self.label('714 − 741 = −27 = −3 × 9',[0,-.2,0],'secondary'))
  self.at('Every power of ten');self.say('Place value explains the check');self.at('A small check catches');self.add(self.label('Same remainder does not mean same number',[0,-1.5,0]));self.finish()
