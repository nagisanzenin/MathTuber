from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        self.title('FOLLOW ONE CARD')
        d=cards();self.show(d);order=list(range(8));positions=VGroup(*[txt(str(i),18,MUTED).move_to([(i-3.5)*.78,-.95,0]) for i in range(8)]);self.show(positions)
        self.at('The first half');self.play(*[d[i].animate.set_opacity(.25) for i in range(4,8)],run_time=.4);order=shuffle(self,d,order)
        self.at('The second half');self.play(*[d[i].animate.set_opacity(1) for i in range(4,8)],run_time=.5)
        self.at('Follow just the card');self.play(*[d[i].animate.set_opacity(.15 if i!=1 else 1) for i in range(8)],run_time=.5)
        track=label('1 → 2',-2.4,BLUE,44);self.show(track)
        self.at('After the next');order=shuffle(self,d,order);self.play(Transform(track,label('1 → 2 → 4',-2.4,BLUE,44)),run_time=.4)
        self.at('After the third');order=shuffle(self,d,order);self.play(Transform(track,label('1 → 2 → 4 → 1',-2.4,GREEN,44)),run_time=.4)
        self.at('completed a three step orbit');self.play(Circumscribe(track,color=GREEN),run_time=1)
        self.at('a collection of loops');self.note('Same objects. Repeated rule.',-3.7)
        self.finish()
