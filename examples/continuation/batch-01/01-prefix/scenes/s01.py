from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('8 symbols · fewer than 16 bits?')
  letters='AAAABBCD';cards=VGroup(*[self.card(c,[-2.1+(i%4)*1.4,3-(i//4)*1.2,0]) for i,c in enumerate(letters)]);self.add(cards)
  self.at('Our message contains');self.wait(.4)
  self.at('Give letter A the code');self.wipe();self.say('A short path for a common symbol')
  rows=VGroup(*[self.label(s,[0,3.2-i*.8,0]) for i,s in enumerate(['A × 4     → 0','B × 2     → 10','C × 1     → 110','D × 1     → 111'])]);self.play(FadeIn(rows),run_time=.7)
  self.at('Follow the branches');self.wipe();self.say('A symbol ends at a leaf')
  pts=[np.array(p) for p in [(0,3.8,0),(-2,2.5,0),(1,2.5,0),(-.2,1,0),(2,1,0),(1.2,-.5,0),(2.8,-.5,0)]]
  edges=[(0,1,'0'),(0,2,'1'),(2,3,'0'),(2,4,'1'),(4,5,'0'),(4,6,'1')]
  tree=VGroup(*[self.line(pts[a],pts[b]) for a,b,c in edges],*[self.label(c,(pts[a]+pts[b])/2+LEFT*.2) for a,b,c in edges],*[Dot(p,color=self.palette['ink']) for p in pts],*[self.label(c,pts[i]+DOWN*.4) for i,c in [(1,'A'),(3,'B'),(5,'C'),(6,'D')]])
  self.play(FadeIn(tree),run_time=.8)
  self.at('The four letter A symbols');self.wipe();self.say('Count the bits actually sent')
  labels=['A: 4 × 1 = 4','B: 2 × 2 = 4','C: 1 × 3 = 3','D: 1 × 3 = 3'];costs=VGroup(*[self.label(s,[0,3.3-i*.85,0]) for i,s in enumerate(labels)]);self.play(FadeIn(costs),run_time=.6)
  self.at('Fourteen bits altogether');total=self.label('4 + 4 + 3 + 3 = 14',[0,-.6,0],'primary','claim');self.play(FadeIn(total),run_time=.6)
  self.at('Swap the lengths');self.wipe();self.say('Give A the longer code?');before=VGroup(self.label('A: 4 × 1 = 4',[-1.4,2.8,0]),self.label('C: 1 × 3 = 3',[1.4,2.8,0]));self.add(before)
  self.play(before[0].animate.shift(DOWN*1.2),before[1].animate.shift(DOWN*1.2),run_time=.7);self.remove(before);self.add(self.label('A: 4 × 3 = 12',[0,2.8,0]),self.label('C: 1 × 1 = 1',[0,1.7,0]),self.label('7 bits → 13 bits',[0,.3,0],'secondary','claim'))
  self.at('Short paths are scarce');self.say('Spend short codes where they recur')
  self.at('Huffman coding builds');self.add(self.label('join the two least frequent groups',[0,-1.1,0]))
  self.at('If all four symbols');self.wipe();self.say('Change the frequencies');self.add(self.label('A, B, C, D equally common',[0,3,0]),self.label('(1 + 2 + 3 + 3) / 4 = 2.25',[0,1.7,0],'secondary','claim'),self.label('fixed code: 2 bits per symbol',[0,.3,0],'primary','claim'))
  self.at('Compression depends');self.add(self.label('Codebook overhead excluded',[0,-1.2,0]));self.finish()
