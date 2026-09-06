from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('A worse fit. A lower total cost?');axis=NumberLine(x_range=[0,4,1],length=5,include_numbers=False,color=self.palette['ink']).move_to(UP*3);self.add(axis)
  for v in [0,2,4]:self.add(self.label(str(v),axis.n2p(v)+DOWN*.4))
  dot=Dot(axis.n2p(4),radius=.12,color=self.palette['accent']);self.add(dot)
  self.at('The training target is four');self.add(self.label('weight',[2.5,4,0],'primary'))
  self.at('Now add a price');self.add(self.label('fit: (w − 4)²',[0,1.8,0],'primary'),self.label('penalty: w²',[0,.9,0],'secondary'))
  def square(v,pos,col):
   side=max(.015,abs(v)*.5);return Square(side_length=side,fill_color=self.palette[col],fill_opacity=.5,stroke_color=self.palette[col]).move_to(pos)
  self.at('At weight four');fit=square(0,[-1.4,-.5,0],'primary');pen=square(4,[1.4,-.5,0],'secondary');self.add(fit,pen);cost=self.label('0 + 16 = 16',[0,-2.1,0]);self.add(cost)
  self.at('At weight two, each cost');self.play(dot.animate.move_to(axis.n2p(2)),Transform(fit,square(2,[-1.4,-.5,0],'primary')),Transform(pen,square(2,[1.4,-.5,0],'secondary')),run_time=1.2);self.remove(cost);cost=self.label('4 + 4 = 8',[0,-2.1,0],'accent','claim');self.add(cost)
  self.at('The two squared distances');self.say('The midpoint balances the two costs')
  self.at('Algebra gives');self.wipe();self.say('Complete the square');self.add(self.label('(w − 4)² + w²',[0,3.2,0],'ink','claim'),self.label('= 2(w − 2)² + 8',[0,1.8,0],'primary','claim'),self.label('minimum: 8 at w = 2',[0,.3,0]))
  self.at('We can turn the penalty');self.wipe();self.say('Change the price of a large weight');self.add(self.label('(w − 4)² + λw²',[0,3.3,0],'ink','claim'));labels=VGroup(self.label('λ = 1    → w = 2',[0,2,0]),self.label('λ = 1/3 → w = 3',[0,1,0]),self.label('λ = 0    → w = 4',[0,0,0]));self.add(*labels)
  self.at('In this example');self.add(self.label('best w = 4 / (1 + λ)',[0,-1.3,0],'primary','claim'))
  self.at('It does not guarantee');self.say('Smaller weights ≠ guaranteed better tests');self.finish()
