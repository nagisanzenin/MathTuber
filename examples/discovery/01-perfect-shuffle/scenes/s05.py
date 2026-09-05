from scenes._shared.design import *

class Shot5(Stage):
    sid="s05"
    def construct(self):
        self.title('CHANGE THE DECK')
        conditions=VGroup(*[txt(s,29,c) for s,c in [('Equal halves',BLUE),('Perfect alternation',BLUE),('Top card stays on top',BLUE)]]).arrange(DOWN,buff=.35).move_to(UP*1.5);self.show(conditions)
        self.at('A sloppy shuffle');warning=label('Ordinary shuffle ≠ this rule',-1,RED);self.show(warning)
        self.at('Try the same idea');self.play(FadeOut(conditions),FadeOut(warning),run_time=.5);d=cards(6);self.show(d);order=list(range(6))
        self.at('Track position one');track=label('1',-2,BLUE,40);self.show(track)
        for k,seq in enumerate(['1 → 2','1 → 2 → 4','1 → 2 → 4 → 3','1 → 2 → 4 → 3 → 1']):
            order=shuffle(self,d,order);self.play(Transform(track,label(seq,-2,BLUE,40)),run_time=.2)
        self.at('the length of a mathematical loop');self.note('Random looking ≠ random',-3.6,GREEN)
        self.finish()
