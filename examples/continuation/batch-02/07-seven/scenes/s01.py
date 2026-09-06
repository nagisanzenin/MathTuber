from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('3⁶ = 729 = 104 × 7 + 1');self.add(self.label('Why remainder 1?',[0,2,0],'primary','claim'))
  self.at('Look at the six');self.wipe();self.say('Nonzero remainders modulo 7');xs=[-2.5+i for i in range(6)];a=VGroup(*[self.card(str(v),[x,3,0],w=.75) for x,v in zip(xs,range(1,7))]);self.add(a)
  self.at('Multiply each by three');b=VGroup(*[self.card(str(v),[x,1.4,0],'secondary',w=.75) for x,v in zip(xs,[3,6,2,5,1,4])]);self.play(FadeIn(b),run_time=.7);self.add(self.label('multiply by 3 · keep remainder',[0,2.2,0]))
  self.at('The order changed');self.play(*[b[i].animate.move_to([xs[v-1],1.4,0]) for i,v in enumerate([3,6,2,5,1,4])],run_time=1.3)
  self.at('Multiply every entry');self.wipe();self.say('Same factors. Same product.');self.add(self.label('P = 1 × 2 × 3 × 4 × 5 × 6',[0,3,0]),self.label('3⁶ P ≡ P  (mod 7)',[0,1.5,0],'primary','claim'))
  self.at('We can cancel');self.add(self.label('P has no factor 7',[0,.3,0]));self.at('What remains');self.add(self.label('3⁶ ≡ 1  (mod 7)',[0,-1,0],'accent','claim'))
  self.at('The same argument');self.say('Prime modulus · nonzero remainder');self.at('This is Fermat');self.add(self.label('aᵖ⁻¹ ≡ 1  (mod p)',[0,-2.1,0],'primary'))
  self.at('The prime condition matters');self.wipe();self.say('Modulo 6, this permutation breaks');self.add(self.label('1   2   3   4   5',[0,3.3,0],'ink','claim'),self.label('×2, modulo 6',[0,2.3,0]));self.at('Modulo six');self.add(self.label('2   4   0   2   4',[0,1.3,0],'secondary','claim'))
  self.at('Two to the fifth');self.add(self.label('2⁵ = 32 ≡ 2  (mod 6)',[0,-.2,0],'secondary','claim'));self.finish()
