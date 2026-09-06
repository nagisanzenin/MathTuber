from scenes._shared.design import *
class Film(Stage):
 def construct(self):
  self.say('Two colors. Every edge must cross colors.')
  def graph(points):
   pts=[np.array(p) for p in points];e=VGroup(*[self.line(pts[i],pts[(i+1)%len(pts)],'ink',3) for i in range(len(pts))]);n=VGroup(*[Dot(p,radius=.25,color=self.palette['ink']) for p in pts]);return e,n
  e,n=graph([(-1.7,3.6,0),(1.7,3.6,0),(1.7,.2,0),(-1.7,.2,0)]);self.add(e,n)
  self.at('Make one corner');self.play(n[0].animate.set_color(self.palette['primary']),run_time=.4)
  self.at('Its neighbor');self.play(n[1].animate.set_color(self.palette['secondary']),run_time=.4)
  self.at('The next is teal');self.play(n[2].animate.set_color(self.palette['primary']),n[3].animate.set_color(self.palette['secondary']),run_time=.7)
  self.at('The final connection');self.add(self.label('even cycle: consistent',[0,-1.2,0],'primary'))
  self.at('Now try a triangle');self.wipe();self.say('Three switches cannot close consistently');e,n=graph([(0,3.8,0),(-2,.5,0),(2,.5,0)]);self.add(e,n)
  self.at('Teal, coral, teal');self.play(*[n[i].animate.set_color(self.palette['primary' if i%2==0 else 'secondary']) for i in range(3)],run_time=.9)
  self.at('The last connection');self.play(e[2].animate.set_color(self.palette['accent']).set_stroke(width=8),run_time=.6);self.add(self.label('same color at both ends',[0,-1,0],'accent'))
  self.at('Each edge switches');self.say('Every edge flips the required color')
  self.at('This obstruction is also');self.wipe();self.say('No odd cycles → two colors');self.add(self.label('color by distance from a starting dot',[0,3.6,0]))
  layers=VGroup(*[self.card(str(i),[-2.4+i*1.2,2,0],'primary' if i%2==0 else 'secondary',w=.8) for i in range(5)]);self.add(layers,*[self.line([-2+i*1.2,2,0],[-1.6+i*1.2,2,0],'ink',2) for i in range(4)],self.label('even · odd · even · odd · even',[0,.6,0]))
  self.at('An edge joining equal');self.add(self.label('equal parity edge → odd closed walk',[0,-.6,0]),self.label('an odd closed walk contains an odd cycle',[0,-1.5,0]))
  self.at('So two colors work');self.say('Bipartite ⇔ no odd cycle')
  self.at('A single new diagonal');self.wipe();self.say('One extra connection can break it');e,n=graph([(-1.7,3.6,0),(1.7,3.6,0),(1.7,.2,0),(-1.7,.2,0)]);self.add(e,n)
  for i in range(4):n[i].set_color(self.palette['primary' if i%2==0 else 'secondary'])
  self.play(Create(self.line(n[0].get_center(),n[2].get_center(),'accent',7)),run_time=1);self.add(self.label('The diagonal creates odd cycles',[0,-1.2,0]));self.finish()
