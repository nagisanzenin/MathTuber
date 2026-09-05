from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        self.title('STEAL THE REPLY')
        left=chocolate().scale(.65).move_to(LEFT*1.65);right=chocolate().scale(.65).move_to(RIGHT*1.65);self.show(left)
        self.at('chosen B immediately');self.show(right);self.play(FadeOut(bite(left,2,1)),FadeOut(bite(right,2,1)),run_time=1)
        self.at('exactly the same shape');self.show(label('Corner → B       Just B',-2,BLUE,27));self.play(Indicate(left[0],color=GREEN),Indicate(right[0],color=GREEN),run_time=.8)
        self.at('you would be the player');self.show(label('Me to move       You to move',-2.8,GOLD,25))
        self.at('That contradicts');self.note('Same position. Roles reversed.',-3.7,GREEN)
        self.at('first player must');self.show(txt('A winning opening EXISTS',35,GREEN).move_to(UP*2.9))
        self.finish()
