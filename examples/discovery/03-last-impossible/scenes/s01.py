from scenes._shared.design import *

class Shot1(Stage):
    sid="s01"
    def construct(self):
        self.title('THE LAST IMPOSSIBLE ORDER')
        a=packet(4).scale(1.5).move_to(LEFT*1.5+UP);b=packet(7).scale(1.5).move_to(RIGHT*1.5+UP);self.show(VGroup(a,b));self.show(label('4 cookies              7 cookies',2.3,BLUE,29))
        self.at('An order of eleven');self.show(eq('4+7=11',y=-.6));self.play(a.animate.shift(RIGHT*.3),b.animate.shift(LEFT*.3),run_time=.6)
        self.at('seventeen is impossible');self.show(label('17   ×',-2.1,RED,51))
        self.at('Every larger whole number');self.note('18, 19, 20, 21, 22, … ALL possible',-3.6,GREEN)
        self.finish()
