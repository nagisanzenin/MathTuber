from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        def position(i):return np.array([-2.45+(i%8)*.7,3.8-(i//8)*.8,0])
        def frame(i):return Square(side_length=.62,stroke_color=INK,stroke_width=1.5).move_to(position(i))
        def item(i):return VGroup(Square(side_length=.46,fill_color=TEAL,fill_opacity=.65,stroke_width=0),self.lettering(str(i+1),'detail','ink').scale(.9)).move_to(position(i))
        capacity=1;stored=VGroup();slots=VGroup(frame(0));self.add(slots);heading=txt('a growing list',[0,5.3,0],'claim');self.add(heading)
        self.at('A growing list');self.at('Why is adding');self.at('Imagine storage');stored.add(item(0));self.play(FadeIn(stored),run_time=.6);cost=txt('written: 1     copied: 0',[0,1.5,0]);self.play(FadeIn(cost),run_time=.4)
        writes=1;copies=0
        # Temporary lower copies make the physical relocation visible before settling.
        # Variables are scene-local; return updated counters explicitly.
        def append_state(n,capacity,copies):
         if n==capacity:
          self.remove(cost);newslots=VGroup(*[frame(i) for i in range(capacity*2)]).shift(DOWN*2.6);self.play(FadeIn(newslots),run_time=.3)
          moving=stored.copy();self.add(moving);self.play(moving.animate.shift(DOWN*2.6),run_time=.5);self.remove(stored,slots);slots.become(newslots);stored.become(moving);self.remove(newslots,moving);self.add(slots,stored);self.play(slots.animate.shift(UP*2.6),stored.animate.shift(UP*2.6),run_time=.5)
          copies+=n;capacity*=2
         newitem=item(n);stored.add(newitem);self.play(FadeIn(newitem),run_time=.25)
         return capacity,copies
        self.at('The second');capacity,copies=append_state(1,capacity,copies);cost=self.replace_label(cost,txt('written: 2     copied: 1',[0,1.5,0]))
        self.at('The third');capacity,copies=append_state(2,capacity,copies);cost=self.replace_label(cost,txt('written: 3     copied: 3',[0,1.5,0]))
        self.at('The fourth');capacity,copies=append_state(3,capacity,copies);cost=self.replace_label(cost,txt('written: 4     copied: 3',[0,1.5,0]))
        self.at('For the fifth');capacity,copies=append_state(4,capacity,copies);cost=self.replace_label(cost,txt('written: 5     copied: 7',[0,1.5,0]))
        self.at('The next three');self.remove(cost);
        for n in range(5,8):capacity,copies=append_state(n,capacity,copies)
        cost=self.replace_label(cost,txt('written: 8     copied: 7',[0,1.5,0]))
        self.at('Eight appends');self.at('That is fifteen');total=txt('8 + 7 = 15 operations',[0,.3,0],'claim');self.play(FadeIn(total),run_time=.5)
        self.at('The expensive');self.play(FadeOut(total),run_time=.4);blocks=VGroup(*[Rectangle(width=.22*2**i,height=.55,fill_color=TEAL,fill_opacity=.6,stroke_color=INK,stroke_width=1).move_to([-2.3+sum(.22*2**j+.14 for j in range(i))+.11*2**i,-.4,0]) for i in range(4)]);labels=VGroup(*[txt(str(2**i),b.get_center()+DOWN*.65) for i,b in enumerate(blocks)]);self.play(FadeIn(blocks),FadeIn(labels),run_time=.7)
        self.at('Each copied');self.play(Indicate(blocks[-1],color=GOLD),run_time=.7)
        self.at('All the earlier');relation=txt('1 + 2 + 4 < 8',[0,-2.1,0],'claim');self.play(FadeIn(relation),run_time=.5)
        self.at('After any number');relation=self.replace_label(relation,txt('total copies < 2n',[0,-2.1,0],'claim'))
        self.at('Adding one write');relation=self.replace_label(relation,txt('n writes + copies < 3n',[0,-2.1,0],'claim'))
        self.at('This is amortized');self.at('We count item');self.at('Now the eight');self.play(FadeOut(VGroup(blocks,labels,relation,cost)),run_time=.5)
        self.at('Eight old items');capacity,copies=append_state(8,capacity,copies);cost=txt('item 9: 8 copies + 1 write',[0,.7,0],'claim');self.play(FadeIn(cost),run_time=.5)
        self.at('Item ten');capacity,copies=append_state(9,capacity,copies);nextcost=txt('item 10: 1 write',[0,-.5,0],'claim');self.play(FadeIn(nextcost),run_time=.5)
        self.at('Occasional expensive');self.play(Indicate(VGroup(*list(slots)[10:]),color=GOLD),run_time=.8);self.finish()
