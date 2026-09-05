from scenes._shared.design import *

class Shot5(Stage):
    sid="s05"
    def construct(self):
        self.title('THE MIRROR SCALES UP')
        self.show(grid(4,.92,np.array([-1.9,-1.6,0])));self.play(Create(path('RRURURUU',BLUE,.92,np.array([-1.9,-1.6,0]))),run_time=1.5)
        self.at('seventy unrestricted');self.show(label('70 unrestricted',3.05,BLUE,31))
        self.at('fifty six forbidden');self.show(label('− 56 forbidden',-2.5,RED,31))
        self.at('leaving fourteen');self.show(eq('70-56=14',y=-3.6,size=45,color=GREEN))
        self.at('the Catalan numbers');self.play(FadeOut(*list(self.mobjects)[2:]),run_time=.8);self.show(txt('1, 2, 5, 14, …',57,GOLD).move_to(UP*.8));self.show(label('CATALAN NUMBERS',-.3,BLUE,28))
        self.at('transform them back');self.note('Transform it. Count it. Undo it.',-3.4,GREEN)
        self.finish()
