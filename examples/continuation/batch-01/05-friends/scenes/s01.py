from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Same people. A different way to sample.');pts=[np.array(x) for x in [(0,2.6,0),(-2,4,0),(2,4,0),(-2,1,0),(2,1,0)]];edges=VGroup(*[self.line(pts[0],p,'ink',2) for p in pts[1:]]);nodes=VGroup(*[VGroup(Dot(p,radius=.23,color=self.palette['accent' if i==0 else 'primary']),self.label('C' if i==0 else str(i),p+DOWN*.5)) for i,p in enumerate(pts)]);self.add(edges,nodes)
  self.at('There are five people');self.add(self.label('degrees: 4, 1, 1, 1, 1',[0,-.3,0]))
  self.at('Sampling people equally');self.add(self.label('8 / 5 = 1.6',[0,-1.4,0],'primary','claim'))
  self.at('Now put a name');self.wipe();self.say('One name for each friendship end');tokens=VGroup(*[self.card(s,[-2.1+(i%4)*1.4,3.2-(i//4)*1.25,0],'accent' if s=='C' else 'primary') for i,s in enumerate(['C','C','C','C','1','2','3','4'])]);self.play(FadeIn(tokens),run_time=1)
  self.at('The central person');self.play(*[tokens[i].animate.shift(UP*.15) for i in range(4)],run_time=.5)
  self.at('Four names lead');self.add(self.label('4 copies × degree 4',[0,.5,0],'accent'),self.label('4 copies × degree 1',[0,-.4,0],'primary'))
  self.at('The average is twenty');self.add(self.label('(16 + 4) / 8 = 2.5',[0,-1.6,0],'ink','claim'))
  self.at('For any undirected network');self.wipe();self.say('Connections weight the sample');self.add(self.label('person average: E[D]',[0,3,0]),self.label('endpoint average: E[D²] / E[D]',[0,1.7,0],'primary'))
  self.at('It is at least');self.add(self.label('= E[D] + Var(D) / E[D]',[0,.4,0],'accent','claim'),self.label('variance ≥ 0 · at least one edge',[0,-.7,0]))
  self.at('If everyone has the same');self.wipe();self.say('Equal degrees remove the difference');ring=VGroup(*[Dot([1.6*math.cos(t),2+1.6*math.sin(t),0],radius=.16,color=self.palette['primary']) for t in np.arange(4)*PI/2]);self.add(*[self.line(ring[i].get_center(),ring[(i+1)%4].get_center(),'ink',2) for i in range(4)],ring,self.label('Every degree is 2 · both averages are 2',[0,-.4,0]))
  self.at('It does not say every');self.add(self.label('An average, not a claim about every person',[0,-1.6,0]));self.finish()
