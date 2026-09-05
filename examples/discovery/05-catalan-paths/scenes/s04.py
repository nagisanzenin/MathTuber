from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        self.title('TWENTY MINUS FIFTEEN')
        a=eq(r'\binom63=20',y=2.5,size=55,color=BLUE);b=eq(r'\binom62=15',y=1.1,size=55,color=RED)
        self.at('twenty ways');self.show(a)
        self.at('fifteen ways');self.show(b)
        self.at('Subtract');self.show(eq('20-15=5',y=-.1,size=57,color=GREEN))
        self.at('Watch all five');safe=[]
        for ups in itertools.combinations(range(6),3):
            seq=''.join('U' if i in ups else 'R' for i in range(6));v=vertices(seq,1,np.zeros(3))
            if all(pt[1]<=pt[0] for pt in v):safe.append(seq)
        for i,seq in enumerate(safe):
            o=np.array([-2.85+i*1.18,-2.5,0]);self.show(grid(3,.28,o));self.play(Create(path(seq,GREEN,.28,o)),run_time=.4)
        self.note('Each route stays below the diagonal.',-3.9,GOLD)
        self.finish()
