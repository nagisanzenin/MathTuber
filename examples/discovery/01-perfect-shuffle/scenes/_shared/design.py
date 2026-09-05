from components import *
from pathlib import Path
import json,itertools
import manimpango
FONT='Avenir Next' if 'Avenir Next' in manimpango.list_fonts() else 'DejaVu Sans'
WHITE='#F5F2E9';BLUE='#73D9F1';GOLD='#FFD078';RED='#FF8F8B';GREEN='#93E0B1';PURPLE='#BBACF7';MUTED='#8794AC';DARK='#0B1020'
def txt(s,size=32,color=WHITE):
    t=Text(s,font=FONT,font_size=size,color=color)
    if t.width>6.4:t.scale_to_fit_width(6.4)
    return t

def label(s,y=-3.3,color=GOLD,size=32):return txt(s,size,color).move_to(UP*y)
def eq(s,y=-3.1,size=45,color=GOLD):
    m=MathTex(s,font_size=size,color=color)
    if m.width>6.3:m.scale_to_fit_width(6.3)
    return m.move_to(UP*y)
class Stage(NarratedScene):
    sid='s01'
    def setup(self):
        super().setup();self.camera.background_color=DARK
        self.times=json.loads((Path(__file__).resolve().parents[2]/'assets/timing.json').read_text())[self.sid]
        self.add(txt('I VISUALIZE THINGS',17,MUTED).move_to(UP*6.05))
        self.add(Line([-3.2,5.75,0],[3.2,5.75,0],color='#293148',stroke_width=1))
    def title(self,s):self.add(txt(s,43).move_to(UP*4.8))
    def at(self,phrase):
        dt=self.times[phrase]-self.renderer.time
        if dt<-.4:raise ValueError(f'Overrun {phrase}: {-dt:.2f}s')
        if dt>0:self.wait(dt)
    def show(self,m):self.play(FadeIn(m,shift=UP*.08),run_time=.45)
    def note(self,s,y=-3.3,color=GOLD):
        m=label(s,y,color);self.show(m);return m

def cards(n=8):
    colors=[interpolate_color(ManimColor(BLUE),ManimColor(PURPLE),i/max(n-1,1)) for i in range(n)]
    return VGroup(*[VGroup(RoundedRectangle(width=.64,height=1.1,corner_radius=.08,fill_opacity=1,fill_color=colors[i],stroke_width=0),txt(str(i),29,DARK)).move_to([(i-(n-1)/2)*.78,0,0]) for i in range(n)])
def shuffle(scene,deck,order):
    n=len(order);new=[x for pair in zip(order[:n//2],order[n//2:]) for x in pair]
    scene.play(*[deck[k].animate.move_to([(j-(n-1)/2)*.78,0,0]) for j,k in enumerate(new)],run_time=.75,path_arc=.7)
    return new

def chocolate(w=5,h=4,size=.82):
    g=VGroup()
    for y in range(h):
        for x in range(w):
            pos=np.array([(x-(w-1)/2)*size,(y-(h-1)/2)*size+.25,0])
            tile=RoundedRectangle(width=size*.91,height=size*.91,corner_radius=.075,fill_color='#75462F',fill_opacity=1,stroke_color='#BC8351',stroke_width=1.8).move_to(pos)
            if x==0 and y==0:tile.set_fill(RED);tile.add(txt('X',30,DARK).move_to(pos))
            tile.xy=(x,y);g.add(tile)
    return g

def bite(g,x,y):return VGroup(*[t for t in g if t.xy[0]>=x and t.xy[1]>=y])
def packet(n,scale=1):
    g=VGroup(*[Dot(radius=.075,color=GOLD) for i in range(n)]).arrange(RIGHT,buff=.07)
    box=RoundedRectangle(width=g.width+.25,height=.52,corner_radius=.08,fill_color='#273045',fill_opacity=1,stroke_color=BLUE if n==4 else RED,stroke_width=2)
    return VGroup(box,g).scale(scale)
def order_row(total,counts,y):
    boxes=VGroup(*[packet(n,.9) for n in counts]).arrange(RIGHT,buff=.13)
    if boxes.width>4.9:boxes.scale_to_fit_width(4.9)
    return VGroup(txt(str(total),33,GOLD).move_to([-2.8,y,0]),boxes.move_to([.45,y,0]))
def coin(s):
    c=BLUE if s=='H' else GOLD
    return VGroup(Circle(radius=.48,fill_color=c,fill_opacity=1,stroke_color=WHITE,stroke_width=1),txt(s,36,DARK))
def pattern(s):return VGroup(*[coin(x) for x in s]).arrange(RIGHT,buff=.16)
def state_node(s,pos,color=BLUE):
    return VGroup(Circle(radius=.66,color=color,fill_color='#1B253B',fill_opacity=1),txt(s,32,color)).move_to(pos)
def grid(n=3,unit=1.25,origin=np.array([-2.,-1.5,0]),wide=None):
    w=wide or n
    lines=VGroup(*[Line(origin+RIGHT*i*unit,origin+RIGHT*i*unit+UP*n*unit,color='#32435F',stroke_width=1.3) for i in range(w+1)],*[Line(origin+UP*i*unit,origin+UP*i*unit+RIGHT*w*unit,color='#32435F',stroke_width=1.3) for i in range(n+1)])
    diag=DashedLine(origin,origin+np.array([n*unit,n*unit,0]),color=RED,dash_length=.13,stroke_width=2)
    return VGroup(lines,diag)
def vertices(seq,unit=1.25,origin=np.array([-2.,-1.5,0])):
    out=[origin.copy()]
    for s in seq:out.append(out[-1]+(RIGHT if s=='R' else UP)*unit)
    return out
def path(seq,color=BLUE,unit=1.25,origin=np.array([-2.,-1.5,0])):
    return VMobject(color=color,stroke_width=6).set_points_as_corners(vertices(seq,unit,origin))
