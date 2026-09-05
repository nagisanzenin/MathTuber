from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        self.title('TOO PERFECT TO MIX?')
        d=cards();self.show(d);counter=label('8 cards • out-shuffle',-2.1,BLUE);self.show(counter)
        self.at('Split them exactly')
        self.play(*[d[i].animate.move_to([((i%4)-1.5)*.85,1.1 if i<4 else -1.1,0]) for i in range(8)],run_time=.8)
        self.at('then alternate');order=shuffle(self,d,list(range(8)));self.play(Transform(counter,label('Shuffle 1',-2.1,BLUE)),run_time=.15)
        self.at('Do it again');order=shuffle(self,d,order);self.play(Transform(counter,label('Shuffle 2',-2.1,BLUE)),run_time=.15)
        self.at('And once more');order=shuffle(self,d,order);self.play(Transform(counter,label('Shuffle 3: restored',-2.1,GREEN)),run_time=.15)
        self.at('This is a perfect');self.play(Indicate(d[0],color=GOLD),Indicate(d[7],color=GOLD),run_time=1)
        self.at('the mixing has a clock');self.note('A shuffle can be a loop.',-3.4)
        self.finish()
