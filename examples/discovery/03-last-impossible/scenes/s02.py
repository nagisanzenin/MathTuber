from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        self.title('RULE OUT EVERY POSSIBILITY')
        rows=VGroup(*[txt(s,34,c).move_to(UP*(2.5-i*1.3)) for i,(s,c) in enumerate([('0 sevens → 17 left',BLUE),('1 seven  → 10 left',BLUE),('2 sevens → 3 left',BLUE),('3 sevens → too many',RED)])])
        self.at('With no seven box');self.show(rows[0])
        self.at('With one seven box');self.show(rows[1])
        self.at('With two seven boxes');self.show(rows[2])
        self.at('Neither ten nor three');self.show(label('17, 10, 3: none divisible by 4',-2.8,RED,30))
        self.at('Three seven boxes');self.show(rows[3])
        self.at('exhausted every possibility');self.note('17 cannot be made.',-4,GOLD)
        self.finish()
