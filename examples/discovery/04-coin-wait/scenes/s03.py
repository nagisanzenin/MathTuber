from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        self.title('WHY FOUR FLIPS?')
        start=state_node('E',LEFT*1.7+UP);done=coin('H').move_to(RIGHT*1.7+UP);self.show(VGroup(start,done));arr=Arrow(start.get_right(),done.get_left(),color=BLUE,buff=.1);self.show(arr)
        self.at('Half the time we finish');self.show(txt('½',29,GREEN).move_to(UP*1.55))
        self.at('back where we started');loop=CurvedArrow(start.get_left()+UP*.2,start.get_left()+DOWN*.2,angle=TAU*.8,color=RED);self.show(loop)
        self.at('E equals one plus half');self.show(eq(r'E=1+\frac12E',y=-1.1))
        self.at('which gives two');self.show(eq('E=2',y=-2.1,color=GREEN))
        self.at('Once a head arrives');self.play(FadeOut(start),FadeOut(loop),FadeOut(arr),done.animate.move_to(LEFT*1.25+UP),run_time=.6);t=coin('T').move_to(RIGHT*1.25+UP);self.show(t)
        self.at('Two plus two gives four');self.note('Find H: 2   +   Find T: 2   =   4',-3.5,GREEN)
        self.finish()
