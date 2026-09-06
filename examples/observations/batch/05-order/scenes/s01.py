from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];COLORS={6:'secondary',2:'primary',1:'accent'}
        def txt(s,p,role='claim'):return self.label(s,p,role=role)
        def row(order,y):
            blocks=VGroup();marks=VGroup();elapsed=0;scale=.65
            for n in order:
                block=Rectangle(width=n*scale,height=.85,fill_color=self.palette[COLORS[n]],fill_opacity=.45,stroke_color=INK,stroke_width=2).move_to([-2.925+(elapsed+n/2)*scale,y,0]);label=txt(str(n),block.get_center(),'label');blocks.add(VGroup(block,label));elapsed+=n
                marks.add(txt(str(elapsed),[-2.925+elapsed*scale,y-.8,0],'label'))
            return blocks,marks
        cards=VGroup(*[VGroup(RoundedRectangle(width=1.6,height=1.2,corner_radius=.1,fill_color=self.palette[COLORS[n]],fill_opacity=.4,stroke_color=INK),txt(f'{n} min',[0,0,0],'label')).move_to([-2.1+i*2.1,2.7,0]) for i,n in enumerate([6,2,1])]);self.add(cards)
        self.at('Three jobs');self.play(cards[2].animate.shift(DOWN*.2),run_time=.8);self.at('All the work');total=txt('6 + 2 + 1 = 9 minutes',[0,.8,0]);self.play(FadeIn(total),run_time=.5)
        self.at('But the order');self.at('Run the longest');self.play(FadeOut(VGroup(cards,total)),run_time=.4);long,marks=row([6,2,1],3.1);self.play(FadeIn(long),run_time=.5)
        self.at('The jobs finish');self.play(LaggedStart(*[FadeIn(x) for x in marks],lag_ratio=.5),run_time=1.3);caption=txt('completion times',[0,4.8,0],'label');self.add(caption)
        self.at('Their completion');sum1=txt('6 + 8 + 9 = 23',[0,1.35,0]);self.play(FadeIn(sum1),run_time=.4)
        self.at('Now run');short,marks2=row([1,2,6],-.4);self.play(FadeIn(short),run_time=.6)
        self.at('They finish');self.play(LaggedStart(*[FadeIn(x) for x in marks2],lag_ratio=.5),run_time=1.2);sum2=txt('1 + 3 + 9 = 13',[0,-2.3,0]);self.play(FadeIn(sum2),run_time=.4)
        self.at('Why does');self.play(FadeOut(VGroup(long,marks,caption,sum1,short,marks2,sum2)),run_time=.5)
        self.at('Look at just');top,tm=row([6,2],2.8);bottom,bm=row([2,6],-.2);targets=[b.get_center().copy() for b in bottom];bottom[0].move_to(top[1].get_center()+DOWN*3);bottom[1].move_to(top[0].get_center()+DOWN*3);self.play(FadeIn(top),run_time=.5)
        self.at('The first finishes');self.play(FadeIn(tm),run_time=.5)
        self.at('Swap them');self.play(FadeIn(bottom),run_time=.4);self.play(bottom[0].animate(path_arc=PI/2).move_to(targets[0]),bottom[1].animate(path_arc=PI/2).move_to(targets[1]),run_time=1.4);self.play(FadeIn(bm),run_time=.4)
        self.at('Four minutes');equation=txt('(6 + 8) − (2 + 8) = 4',[0,-2.3,0]);self.play(FadeIn(equation),run_time=.5)
        self.at('In general');self.play(FadeOut(VGroup(top,tm,bottom,bm,equation)),run_time=.5);proof=VGroup(txt('times from the pair’s start',[0,5.2,0],'label'),txt('long a, then short b',[0,4,0],'label'),txt('a + (a+b)',[0,2.9,0]),txt('short b, then long a',[0,1.5,0],'label'),txt('b + (a+b)',[0,.4,0]),txt('saving = a − b',[0,-1.2,0]));self.play(FadeIn(proof),run_time=.6)
        self.at('Everything after');unchanged=txt('same final finish · same later jobs',[0,-2.7,0],'label');self.play(FadeIn(unchanged),run_time=.4)
        self.at('Remove every');self.at('That minimizes');self.play(FadeOut(VGroup(proof,unchanged)),run_time=.5);ordered,om=row([1,2,6],2.8);self.play(FadeIn(VGroup(ordered,om)),run_time=.5);label=txt('shortest processing time first',[0,.7,0]);self.play(FadeIn(label),run_time=.4)
        self.at('This assumes');conditions=txt('ready together · equal importance\none machine · no setup or dependencies',[0,-1.2,0],'label');self.play(FadeIn(conditions),run_time=.4)
        self.at('Deadlines and');self.at('The amount');self.at('We changed');self.finish()
