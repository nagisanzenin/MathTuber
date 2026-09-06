from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        vals=[3,4,5]
        def piles(v):return VGroup(*[VGroup(*[Circle(radius=.16,fill_color=TEAL,fill_opacity=.8,stroke_width=0).move_to([-2+i*2,3.8-j*.45,0]) for j in range(n)]) for i,n in enumerate(v)])
        pile=piles(vals);title=txt('3          4          5',[0,5,0],'claim');self.add(pile,title)
        self.at('Three piles');self.focus_outline(pile,run_time=.6)
        self.at('In Nim');rule=txt('one pile per turn · last stone wins',[0,.7,0]);self.play(FadeIn(rule),run_time=.5)
        self.at('Write the sizes');self.play(FadeOut(rule),run_time=.3);heads=txt('4    2    1',[0,.6,0]);bits=txt('0    1    1\n1    0    0\n1    0    1',[0,-.9,0],'claim');self.play(FadeIn(heads),FadeIn(bits),run_time=.5)
        self.at('Count the ones');self.focus_outline(bits,run_time=.7)
        self.at('Our result');result=txt('XOR: 0    1    0',[0,-2.6,0],'claim');self.play(FadeIn(result),run_time=.5)
        self.at('Reduce the first');self.play(FadeOut(VGroup(bits,result,title)),FadeOut(pile[0][1:]),run_time=.5);title=txt('1          4          5',[0,5,0],'claim');bits=txt('0    0    1\n1    0    0\n1    0    1',[0,-.9,0],'claim');self.play(FadeIn(title),FadeIn(bits),run_time=.5)
        self.at('Every column');result=txt('XOR: 0    0    0',[0,-2.6,0],'claim');self.play(FadeIn(result),run_time=.5)
        self.at('Any legal');self.at('From a nonzero');self.at('Choose a pile');note=txt('highest unmatched bit → smaller pile',[0,1.3,0]);self.play(FadeIn(note),run_time=.5)
        self.at('Repeating this');self.at('Try a reply');self.play(FadeOut(VGroup(pile,title,bits,result,note)),run_time=.4);pile=piles([1,2,5]);title=txt('1          2          5',[0,5,0],'claim');bits=txt('0    0    1\n0    1    0\n1    0    1',[0,-.9,0],'claim');self.play(FadeIn(pile),FadeIn(title),FadeIn(bits),run_time=.5)
        self.at('The sizes are one');result=txt('XOR: 1    1    0',[0,-2.6,0],'claim');self.play(FadeIn(result),run_time=.5)
        self.at('Reduce five');self.play(FadeOut(VGroup(bits,title,result)),FadeOut(pile[2][3:]),run_time=.4);title=txt('1          2          3',[0,5,0],'claim');bits=txt('0    0    1\n0    1    0\n0    1    1',[0,-.9,0],'claim');result=txt('XOR: 0    0    0',[0,-2.6,0],'claim');self.play(FadeIn(title),FadeIn(bits),FadeIn(result),run_time=.5)
        self.at('This strategy');self.finish()
