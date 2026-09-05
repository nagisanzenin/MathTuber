from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        self.title('WHY SIX FLIPS?')
        a=state_node('A',LEFT*1.65+UP*1.8);b=state_node('B',RIGHT*1.65+UP*1.8);self.show(VGroup(a,b));self.show(txt('fresh',24,BLUE).next_to(a,UP));self.show(txt('after H',24,BLUE).next_to(b,UP))
        self.at('From A, we spend');ab=CurvedArrow(a.get_right(),b.get_left(),angle=-.6,color=BLUE);self.show(ab);self.show(txt('H',24,BLUE).move_to([0,2.25,0]))
        self.at('From B');ba=CurvedArrow(b.get_bottom(),a.get_bottom(),angle=-.8,color=RED);self.show(ba);self.show(txt('T: reset',24,RED).move_to([0,.65,0]))
        self.at('two equations');form=VGroup(eq(r'A=1+\frac12A+\frac12B',y=-.6,size=42),eq(r'B=1+\frac12A',y=-1.65,size=42));self.show(form)
        self.at('Substitute B');self.play(Transform(form,VGroup(eq(r'A=\frac32+\frac34A',y=-.6,size=44),eq(r'\frac14A=\frac32',y=-1.65,size=44))),run_time=1)
        self.at('A becomes six');self.show(eq('A=6',y=-3.2,size=64,color=GREEN))
        self.finish()
