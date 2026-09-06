from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Does longer mean more similar?');self.add(Arrow([-2,2,0],[2,4,0],buff=0,color=self.palette['secondary']),Arrow([-2,0,0],[-1.6,.2,0],buff=0,color=self.palette['primary']),self.label('same direction · lengths 10 : 1',[0,-1.4,0]));self.at('Let our reference');self.wipe();self.say('Compare each with a reference');origin=np.array([-1.6,.5,0]);ref=Arrow(origin,origin+RIGHT,buff=0,color=self.palette['primary']);v=Arrow(origin,origin+np.array([2,1,0]),buff=0,color=self.palette['secondary']);self.add(ref,v,self.label('reference: (1, 0)',[0,-.5,0],'primary'))
  self.at('Compare an arrow');lab=self.label('v = (2, 1)',[0,3,0],'secondary');self.add(lab)
  self.at('Their dot product');score=self.label('dot product = 2',[0,-1.6,0],'ink','claim');self.add(score)
  self.at('Stretch the second');self.play(Transform(v,Arrow(origin,origin+np.array([4,2,0]),buff=0,color=self.palette['secondary'])),run_time=1);self.remove(lab,score);lab=self.label('v = (20, 10)',[0,3.5,0],'secondary');score=self.label('dot product = 20',[0,-1.6,0],'ink','claim');self.add(lab,score,self.label('long arrow drawn at reduced scale',[0,-2.3,0]))
  self.at('A dot product mixes');self.say('Dot product includes vector length')
  self.at('Divide by the product');self.wipe();self.say('Normalize away the length');self.add(self.label('cosine = (u · v) / (|u| |v|)',[0,3,0],'primary','claim'))
  self.at('For the first comparison');self.add(self.label('2 / √5',[0,1.7,0],'secondary','claim'));self.at('For the stretched arrow');self.add(self.label('20 / (10√5) = 2 / √5',[0,.4,0],'secondary','claim'))
  self.at('Now turn the arrow');self.wipe();self.say('Direction still changes the score');origin=np.array([0,1.5,0]);ref=Arrow(origin,origin+RIGHT*2,buff=0,color=self.palette['primary']);v=Arrow(origin,origin+UP*2,buff=0,color=self.palette['secondary']);self.add(ref,v,self.label('perpendicular: cosine = 0',[0,-.2,0]))
  self.at('Turn it directly left');self.play(Rotate(v,PI/2,about_point=origin),run_time=1);self.add(self.label('opposite: cosine = −1',[0,-1.2,0],'secondary'))
  self.at('This is useful');self.say('A choice about what to ignore')
  self.at('A zero vector');self.wipe();self.say('Zero has no direction');self.add(Dot(UP*2,color=self.palette['ink']),self.label('zero length → denominator zero',[0,.7,0]),self.label('cosine similarity undefined',[0,-.6,0],'secondary','claim'));self.finish()
