from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        ax=Axes(x_range=[0,4,1],y_range=[0,4,1],x_length=5,y_length=4,axis_config={'color':INK,'include_tip':False}).move_to([0,2,0]);curve=ax.plot(lambda x:(x-2)**2,color=TEAL);title=txt('target: 2',[0,5.3,0],'claim');self.add(ax,curve,title)
        ends=VGroup(Dot(ax.c2p(1,1),color=CORAL),Dot(ax.c2p(3,1),color=CORAL));labels=txt('predictions: 1       3',[0,-.7,0]);self.add(ends,labels)
        self.at('Two models');self.at('Their squared errors');avg=Dot(ax.c2p(2,0),color=GOLD);calc=txt('average prediction: 2 · loss: 0',[0,-1.8,0]);self.play(FadeIn(avg),FadeIn(calc),run_time=.6)
        self.at('Draw squared');self.at('Join the two');chord=Line(ax.c2p(1,1),ax.c2p(3,1),color=CORAL);mid=Dot(ax.c2p(2,1),color=CORAL);self.play(Create(chord),FadeIn(mid),run_time=.6)
        self.at('The curve below');gap=Line(ax.c2p(2,0),ax.c2p(2,1),color=GOLD,stroke_width=6);self.play(Create(gap),run_time=.6)
        self.at('For any two predictions');self.play(FadeOut(calc),run_time=.2);calc=txt('average loss − loss of average\n= (prediction difference)² / 4',[0,-2,0],'claim');self.play(FadeIn(calc),run_time=.5)
        self.at('The correct answer cancels');self.at('This is a two');self.at('It explains');self.at('It compares')
        self.at('Now let');self.play(FadeOut(VGroup(calc,title,gap,chord,mid,avg,ends)),run_time=.3);self.play(Transform(curve,ax.plot(lambda x:(x-1)**2,x_range=[0,3],color=TEAL)),run_time=.7);title=txt('target: 1',[0,5.3,0],'claim');ends=VGroup(Dot(ax.c2p(1,0),color=CORAL),Dot(ax.c2p(3,4),color=CORAL));self.play(FadeIn(title),FadeIn(ends),run_time=.4)
        self.at('The first model');avg=Dot(ax.c2p(2,1),color=GOLD);self.play(FadeIn(avg),run_time=.4)
        self.at('It still beats');calc=txt('best loss: 0 · loss of average: 1\naverage model loss: 2',[0,-2,0]);self.play(FadeIn(calc),run_time=.5);self.finish()
