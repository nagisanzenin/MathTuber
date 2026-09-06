from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        def card(name,p,color):return VGroup(RoundedRectangle(width=.85,height=.55,corner_radius=.09,fill_color=color,fill_opacity=.2,stroke_color=INK,stroke_width=1),self.lettering(name,'detail','ink')).move_to(p)
        left=VGroup(*[card(str(i),[-1.65,4-i*.75,0],TEAL) for i in range(1,7)])
        right=VGroup(*[card(str(i),[1.65,4-j*.75,0],CORAL) for j,i in enumerate([4,5,6,7,8])]);heads=VGroup(txt('drawing',[-1.65,4.6,0]),txt('music',[1.65,4.6,0]));self.add(left,right,heads)
        self.at('Two lists can contain');self.play(Indicate(right[:3],color=GOLD),run_time=.7)
        self.at('Six people');self.at('Three people');counts=txt('6 + 5 entries',[0,-1.6,0],'claim');self.play(FadeIn(counts),run_time=.5)
        self.at('Put the two');self.at('But these three');links=VGroup(*[Line(left[i+3].get_right(),right[i].get_left(),color=GOLD,stroke_width=2) for i in range(3)]);self.play(Create(links),run_time=.7)
        self.at('Pair each');self.play(*[right[i].animate.move_to(left[i+3].get_center()+RIGHT*1) for i in range(3)],FadeOut(links),run_time=.9)
        self.at('Keep one copy');self.play(FadeOut(right[:3]),run_time=.6);unique=VGroup(*left,*list(right)[3:]);self.play(*[c.animate.move_to([-2.1+(i%4)*1.4,3-(i//4)*1.1,0]) for i,c in enumerate(unique)],FadeOut(heads),run_time=.8)
        self.at('Eight different');counts=self.replace_label(counts,txt('8 people',[0,-1.6,0],'claim'))
        self.at('That is six');formula=txt('6 + 5 − 3 = 8',[0,.5,0],'claim');self.play(FadeIn(formula),run_time=.6)
        self.at('The subtraction');self.play(Indicate(VGroup(*list(unique)[3:6]),color=GOLD),run_time=.8)
        self.at('It removes');self.at('This is the two');title=txt('count each person once',[0,4.8,0],'claim');self.play(FadeIn(title),run_time=.5)
        self.at('Count the first');self.at('Someone in one');self.at('Now imagine');self.play(FadeOut(counts),run_time=.4)
        self.at('If that person');highlight=SurroundingRectangle(unique[0],color=CORAL,buff=.1);self.play(Create(highlight),run_time=.5)
        self.at('The music count');formula=self.replace_label(formula,txt('6 + 6 − 4 = 8',[0,.5,0],'claim'));change=txt('already present: no new person',[0,-1.2,0]);self.play(FadeIn(change),run_time=.5)
        self.at('If instead');self.play(FadeOut(highlight),FadeOut(change),FadeOut(formula),run_time=.4);ninth=card('9',[0,-.6,0],CORAL);self.play(FadeIn(ninth),run_time=.5)
        self.at('Then the total');formula=self.replace_label(formula,txt('6 + 6 − 3 = 9',[0,.5,0],'claim'));ending=txt('new person: total grows by one',[0,-1.8,0]);self.play(FadeIn(ending),run_time=.5)
        self.at('Before adding');self.finish()
