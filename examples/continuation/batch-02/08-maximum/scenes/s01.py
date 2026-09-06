from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Keep the larger of two draws');self.add(self.label('one draw: average 2.5',[0,3.8,0]))
  cells=VGroup();nums=VGroup()
  for i in range(4):
   for j in range(4):
    p=[-1.65+j*1.1,2.6-i*1.1,0];cells.add(Square(side_length=1.05,stroke_color=self.palette['ink'],stroke_width=1).move_to(p));nums.add(self.label(str(max(i,j)+1),p))
  self.at('There are sixteen');self.play(Create(cells),run_time=.8)
  self.at('Write the larger');self.play(FadeIn(nums),run_time=.6)
  self.at('Only one cell');self.play(cells[0].animate.set_fill(self.palette['accent'],.3),run_time=.4)
  self.at('Three have maximum');self.play(*[cells[i*4+j].animate.set_fill(self.palette['primary'],.3) for i in range(2) for j in range(2) if max(i,j)==1],run_time=.5)
  self.at('Five have maximum');self.play(*[cells[i*4+j].animate.set_fill(self.palette['secondary'],.3) for i in range(3) for j in range(3) if max(i,j)==2],run_time=.5)
  self.at('Seven have maximum');self.play(*[cells[i*4+j].animate.set_fill(self.palette['accent'],.3) for i in range(4) for j in range(4) if max(i,j)==3],run_time=.5)
  self.at('Why the odd counts');self.say('A new maximum adds an L-shaped border')
  self.at('Expanding from a square');self.add(self.label('k² − (k − 1)² = 2k − 1',[0,-2.1,0],'primary'))
  self.at('Weight each possible');self.wipe();self.say('Count × value, then divide by 16');self.add(self.label('maximum: 1    2    3    4',[0,3.2,0]),self.label('count:       1    3    5    7',[0,2.2,0]),self.label('1×1 + 2×3 + 3×5 + 4×7 = 50',[0,.9,0]))
  self.at('The new average is three');self.add(self.label('50 / 16 = 3.125',[0,-.3,0],'accent','claim'))
  self.at('If we copy');self.wipe();self.say('A copied draw offers no second chance');self.add(cells,nums)
  for i in range(4):
   for j in range(4):
    cells[i*4+j].set_fill(self.palette['primary'],.35 if i==j else 0);nums[i*4+j].set_opacity(1 if i==j else .15)
  self.at('The average returns');self.add(self.label('(1 + 2 + 3 + 4) / 4 = 2.5',[0,-2.1,0],'primary'));self.finish()
