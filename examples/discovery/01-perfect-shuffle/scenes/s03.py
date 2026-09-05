from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        self.title('THE 52-CARD RULE')
        d=VGroup(*[Line([-2.7,2.8-i*.105,0],[2.7,2.8-i*.105,0],color=interpolate_color(ManimColor(BLUE),ManimColor(PURPLE),i/51),stroke_width=3) for i in range(52)]);self.show(d)
        self.at('Number its positions');a=txt('0',22,GOLD).next_to(d[0],LEFT);b=txt('51',22,GOLD).next_to(d[-1],LEFT);self.show(VGroup(a,b))
        self.at('doubles the position');self.play(FadeOut(d),FadeOut(a),FadeOut(b),run_time=.6);rule=eq(r'p \longmapsto 2p\pmod {51}',y=2);self.show(rule)
        self.at('position thirty');number=txt('30',80,BLUE).move_to(UP*.15);self.show(number)
        self.at('becomes sixty');self.play(Transform(number,txt('60',80,BLUE).move_to(UP*.15)),run_time=.7)
        self.at('then wraps to nine');self.play(Transform(number,txt('60 − 51 = 9',58,GREEN).move_to(UP*.15)),run_time=.8)
        self.at('The bottom card stays fixed');self.note('Bottom position 51 stays fixed',-2, MUTED)
        self.at('double, then take the remainder');self.note('Double. Wrap. Repeat.',-3.5)
        self.finish()
