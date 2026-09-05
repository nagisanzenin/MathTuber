from scenes._shared.design import *

class Shot4(Stage):
    sid="s04"
    def construct(self):
        self.title('A LADDER WITH NO GAPS')
        g=VGroup(*[txt(str(18+c+4*r),34,[BLUE,GOLD,GREEN,PURPLE][c]).move_to([(c-1.5)*1.5,2.8-r*1.15,0]) for r in range(5) for c in range(4)])
        self.show(VGroup(*g[:4]))
        self.at('you get twenty two');self.show(g[4]);self.show(Arrow(g[0].get_bottom(),g[4].get_top(),color=BLUE,buff=.08))
        self.at('you get twenty three');self.show(g[5])
        self.at('twenty four and twenty five');self.show(VGroup(g[6],g[7]))
        self.at('Repeat');self.play(LaggedStart(*[FadeIn(x,shift=DOWN*.1) for x in g[8:]],lag_ratio=.09),run_time=2)
        self.at('every remainder');self.show(label('Each column repeats one remainder',-3.1,GOLD,29))
        self.at('using just four starting points');self.note('Finite seeds → infinite guarantee',-4,GREEN,)
        self.finish()
