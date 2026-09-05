from components import *
from pathlib import Path
import json,random,itertools
import manimpango
FONT = "Avenir Next" if "Avenir Next" in manimpango.list_fonts() else "DejaVu Sans"

BLUE='#56C9F5'; ORANGE='#FF977A'; PURPLE='#B89AFF'; GREEN='#9AE5AA'; GOLD='#F6D76C'; WHITE='#F4F6FA'; MUTED='#8D9AB0'; DARK='#080E1B'
COLORS=[BLUE,ORANGE,PURPLE,GREEN]
def text(s,size=34,color=WHITE,bold=False):return Text(s,font=FONT,font_size=size,color=color,weight=BOLD if bold else NORMAL)
def equation(s,y=-3.35,color=GOLD,size=48):
 m=MathTex(s,font_size=size,color=color)
 if m.width>6.3:m.scale_to_fit_width(6.3)
 return m.move_to(UP*y)
def chip(s,color=WHITE,y=-3.5,size=31):
 bg=RoundedRectangle(width=6.4,height=.9,corner_radius=.18,fill_color='#132035',fill_opacity=1,stroke_color='#2B3D58',stroke_width=1)
 t=text(s,size,color,True)
 if t.width>6:t.scale_to_fit_width(6)
 return VGroup(bg,t).move_to(UP*y)
class Stage(NarratedScene):
 sid='s01'
 def setup(self):
  super().setup();self.camera.background_color=DARK
  p=Path(__file__).resolve().parents[2]/'assets/timing.json';self.times=json.loads(p.read_text())[self.sid]
  self.add(Line([-3.3,6.2,0],[3.3,6.2,0],color='#26364B',stroke_width=2),Line([-3.3,6.2,0],[-3.3+6.6*int(self.sid[1:])/4,6.2,0],color=BLUE,stroke_width=3))
 def title(self,kicker,headline):
  self.add(text(kicker,20,BLUE,True).move_to(UP*5.73))
  m=text(headline,47,WHITE,True)
  if m.width>6.5:m.scale_to_fit_width(6.5)
  self.add(m.move_to(UP*4.8))
 def at(self,phrase):
  t=self.times[phrase]-self.renderer.time
  if t<-.4:raise ValueError(f'cue {phrase}: overrun {-t:.2f}s')
  if t>0:self.wait(t)
 def show(self,mob):self.play(FadeIn(mob,shift=UP*.12),run_time=.55)

DICE=[[4,4,4,4,0,0],[3]*6,[2,2,2,2,6,6],[1,1,1,5,5,5]]
def die(index,width=2.65):
 color=COLORS[index];bg=RoundedRectangle(width=width,height=1.6,corner_radius=.17,fill_color='#142239',fill_opacity=1,stroke_color=color,stroke_width=2)
 title=text('ABCD'[index],24,color,True).move_to(UP*.5)
 nums=VGroup(*[text(str(v),29,color,True) for v in DICE[index]]).arrange_in_grid(rows=2,cols=3,buff=(.34,.18)).move_to(DOWN*.18)
 if nums.width>width-.3:nums.scale_to_fit_width(width-.3)
 return VGroup(bg,title,nums)
def dice_board():return VGroup(*[die(i).move_to([(-1 if i%2==0 else 1)*1.68,(1 if i<2 else -1)*1.35+.35,0]) for i in range(4)])
def wins(a,b):return sum(x>y for x in DICE[a] for y in DICE[b])
def boxes():
 cells=VGroup()
 for i in range(100):
  box=RoundedRectangle(width=.52,height=.43,corner_radius=.045,fill_color='#142239',fill_opacity=1,stroke_color='#456079',stroke_width=.8)
  box.add(text(str(i+1),15,MUTED));box.move_to([(i%10-4.5)*.59,(4.5-i//10)*.51+.5,0]);cells.add(box)
 return cells

def cycle_graph(length,radius,center,color):
 positions=[np.array(center)+radius*np.array([np.cos(TAU*i/length),np.sin(TAU*i/length),0]) for i in range(length)]
 edges=VGroup(*[Line(positions[i],positions[(i+1)%length],color=color,stroke_width=1) for i in range(length)])
 dots=VGroup(*[Dot(x,radius=.045,color=color) for x in positions]);label=text(str(length),34,color,True).move_to(center)
 return VGroup(edges,dots,label)

def circle_diagram():
 c=UP*.65;r=2.4;circle=Circle(radius=r,color=BLUE,stroke_width=3).move_to(c)
 vertices=[c+r*np.array([np.cos(t),np.sin(t),0]) for t in [PI/2,7*PI/6,11*PI/6]]
 tri=Polygon(*vertices,color=MUTED,stroke_width=2,fill_opacity=0)
 return c,r,circle,tri

# Sperner triangulation: barycentric integer coordinates, boundary labels restricted.
def mesh_data(seed=4,n=6):
 rng=random.Random(seed);coords={};labels={}
 corners=[np.array([-2.9,-1.6,0]),np.array([2.9,-1.6,0]),np.array([0,3.1,0])]
 for i in range(n+1):
  for j in range(n+1-i):
   key=(i,j);coords[key]=corners[0]*(n-i-j)/n+corners[1]*i/n+corners[2]*j/n
   if i==0 and j==0:allowed=[0]
   elif i==n:allowed=[1]
   elif j==n:allowed=[2]
   elif j==0:allowed=[0,1]
   elif i==0:allowed=[0,2]
   elif i+j==n:allowed=[1,2]
   else:allowed=[0,1,2]
   labels[key]=(random.Random(i*971+j*137).choice(allowed) if i==0 or j==0 or i+j==n else rng.choice(allowed))
 tris=[]
 for i in range(n):
  for j in range(n-i):
   tris.append(((i,j),(i+1,j),(i,j+1)))
   if i+j<n-1:tris.append(((i+1,j),(i+1,j+1),(i,j+1)))
 edges={}
 for index,tri in enumerate(tris):
  for a,b in zip(tri,tri[1:]+tri[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(index)
 rainbow=[k for k,t in enumerate(tris) if {labels[v] for v in t}=={0,1,2}]
 gates={e:ts for e,ts in edges.items() if {labels[v] for v in e}=={0,1}}
 return coords,labels,tris,edges,rainbow,gates

def mesh(seed=4,highlight=False):
 coords,labels,tris,edges,rainbow,gates=mesh_data(seed)
 fills=VGroup(*[Polygon(*[coords[v] for v in tris[k]],fill_color=GOLD,fill_opacity=.2,stroke_width=0) for k in rainbow]) if highlight else VGroup()
 lines=VGroup(*[Line(coords[a],coords[b],color='#42516A',stroke_width=1.7) for a,b in edges])
 dots=VGroup(*[Dot(coords[v],radius=.09,color=[ORANGE,BLUE,GOLD][labels[v]]) for v in coords]);return VGroup(fills,lines,dots)
def gate_path(seed=4):
 coords,labels,tris,edges,rainbow,gates=mesh_data(seed)
 for edge,owners in gates.items():
  if len(owners)!=1:continue
  current=owners[0];incoming=edge;seen=set();path=[(coords[edge[0]]+coords[edge[1]])/2+DOWN*.45,(coords[edge[0]]+coords[edge[1]])/2]
  while current not in seen:
   seen.add(current);path.append(sum((coords[v] for v in tris[current]))/3)
   exits=[e for e,ts in gates.items() if current in ts and e!=incoming]
   if not exits:return path,current
   e=exits[0];path.append((coords[e[0]]+coords[e[1]])/2)
   if len(gates[e])==1:break
   current=next(t for t in gates[e] if t!=current);incoming=e
 raise ValueError('No rainbow endpoint found')
def marbles(red,blue,scale=1):
 dots=VGroup(*[Dot(radius=.24,color=ORANGE) for _ in range(red)],*[Dot(radius=.24,color=BLUE) for _ in range(blue)])
 dots.arrange_in_grid(cols=min(5,len(dots)),buff=.17);return dots.scale(scale)
def urn(red,blue):
 outline=VMobject(stroke_color=MUTED,stroke_width=3).set_points_as_corners([[-2,1.3,0],[-1.8,-1.5,0],[1.8,-1.5,0],[2,1.3,0]])
 balls=marbles(red,blue).move_to(DOWN*.6)
 return VGroup(outline,balls).shift(UP*.8)
def sequence(seq,y=0):
 return VGroup(*[Dot(radius=.22,color=ORANGE if x=='R' else BLUE) for x in seq]).arrange(RIGHT,buff=.25).move_to(UP*y)
