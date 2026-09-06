from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        data=[[0,1,0,0,1,1],[1,1,0,1,0,0],[0,0,1,1,0,1],[1,0,1,0,1,0],[0,1,1,0,0,1],[1,0,0,1,1,1]]
        rows=VGroup(*[VGroup(*[txt(str(v),[-1.9+j*.65,4.2-i*.65,0]) for j,v in enumerate(row)]) for i,row in enumerate(data)])
        labels=VGroup(*[txt(str(i+1),[-2.9,4.2-i*.65,0]) for i in range(6)]);dots=txt('⋮          ⋱',[0,-.3,0]);title=txt('a proposed infinite list',[0,5.5,0],'claim');self.add(rows,labels,dots,title)
        self.at('Imagine a list');self.at('Each row');self.at('We can build');name=txt('new sequence',[0,-1.3,0]);self.play(FadeIn(name),run_time=.4)
        new=VGroup();boxes=VGroup()
        def flip(i):
         box=SurroundingRectangle(rows[i][i],color=CORAL,buff=.09);digit=txt(str(1-data[i][i]),[-1.9+i*.65,-2.2,0]);boxes.add(box);new.add(digit);self.play(Create(box),TransformFromCopy(rows[i][i],digit),run_time=.55)
        self.at('Read the first');flip(0)
        self.at('Read the second');flip(1)
        self.at('Continue diagonally')
        for i in range(2,6):flip(i)
        self.at('The new sequence');self.focus_outline(VGroup(rows[0][0],new[0]),run_time=.6)
        self.at('It differs from row two');self.focus_outline(VGroup(rows[1][1],new[1]),run_time=.6)
        self.at('For any numbered');proof=txt('row n: digit n is different',[0,-3.4,0],'claim');self.play(FadeIn(proof),run_time=.5)
        self.at('Only a finite');self.at('There is no list');title=self.replace_label(title,txt('infinite binary sequences',[0,5.5,0],'claim'))
        self.at('What if we add');self.play(FadeOut(boxes),FadeOut(proof),run_time=.4);shifted=[ [1-data[i][i] for i in range(6)] ]+data[:5];nextrows=VGroup(*[VGroup(*[txt(str(v),[-1.9+j*.65,4.2-i*.65,0]) for j,v in enumerate(row)]) for i,row in enumerate(shifted)]);self.play(FadeOut(rows),FadeIn(nextrows),FadeOut(new),run_time=.6)
        self.at('Apply the same');again=VGroup(*[txt(str(1-shifted[i][i]),[-1.9+i*.65,-2.2,0]) for i in range(6)]);mark=VGroup(*[SurroundingRectangle(nextrows[i][i],color=CORAL,buff=.09) for i in range(6)]);self.play(Create(mark),FadeIn(again),run_time=.8)
        self.at('The obstacle');self.finish()
