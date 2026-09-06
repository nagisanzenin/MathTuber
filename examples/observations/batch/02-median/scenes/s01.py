from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];q=ValueTracker(3);values=[1,2,4,6,9]
        def txt(s,p,role='claim',color='ink'):return self.label(s,p,color,role)
        def x(v):return -3.1+.45*v
        head=txt('one prediction · five observations',[0,5.1,0],'label');self.add(head)
        axis=NumberLine(x_range=[0,14,2],length=6.3,include_numbers=False,color=INK).move_to([.05,3.5,0]);numbers=VGroup(*[txt(str(v),[x(v),2.7,0],'label') for v in values]);dots=VGroup(*[Dot([x(v),3.5,0],radius=.07,color=INK) for v in values]);self.add(axis,numbers,dots)
        self.at('You need one');pointer=always_redraw(lambda:Arrow([x(q.get_value()),4.65,0],[x(q.get_value()),3.75,0],buff=0,color=CORAL,stroke_width=4));self.add(pointer)
        self.at('Suppose each');self.at('Where should');prediction=always_redraw(lambda:txt(f'prediction: {q.get_value():.0f}',[0,1.8,0],'label','secondary'));self.add(prediction)
        rows=VGroup();distance_labels=VGroup()
        for i,v in enumerate(values):
            y=.95-i*.66
            row=always_redraw(lambda v=v,y=y:VGroup(Line([x(v),y,0],[x(q.get_value())+.00001,y,0],color=TEAL,stroke_width=5),Dot([x(v),y,0],radius=.06,color=INK),Dot([x(q.get_value()),y,0],radius=.06,color=CORAL)))
            rows.add(row)
            distance_labels.add(always_redraw(lambda v=v,y=y:txt(f'{abs(v-q.get_value()):.0f}',[3.15,y,0],'label')))
        self.at('At three');self.add(rows,distance_labels);total=always_redraw(lambda:txt(f'total error = {sum(abs(v-q.get_value()) for v in values):.0f}',[0,-3.2,0]));self.add(total)
        self.at('Move to four');self.play(FadeOut(VGroup(prediction,total,distance_labels)),run_time=.2);self.play(q.animate.set_value(4),run_time=1.3);self.play(FadeIn(VGroup(prediction,total,distance_labels)),run_time=.3);self.at('Move to five');self.play(FadeOut(VGroup(prediction,total,distance_labels)),run_time=.2);self.play(q.animate.set_value(5),run_time=1.3);self.play(FadeIn(VGroup(prediction,total,distance_labels)),run_time=.3)
        self.at('But checking');self.at('pair the smallest');rows.clear_updaters();distance_labels.clear_updaters();total.clear_updaters();prediction.clear_updaters();pointer.clear_updaters();self.play(FadeOut(VGroup(rows,distance_labels,total,prediction,pointer)),run_time=.5)
        outer=Line([x(1),1.4,0],[x(9),1.4,0],color=TEAL,stroke_width=6);outerlabel=txt('1 to 9: at least 8',[0,.6,0],'label','primary');self.play(Create(outer),FadeIn(outerlabel),run_time=.7)
        self.at('Wherever the prediction');q.set_value(2);split=always_redraw(lambda:Dot([x(q.get_value()),1.4,0],color=CORAL,radius=.09));self.add(split);self.play(q.animate.set_value(7),run_time=2.5);split.clear_updaters();self.remove(split)
        self.at('Pair two with six');inner=Line([x(2),-.45,0],[x(6),-.45,0],color=TEAL,stroke_width=6);innerlabel=txt('2 to 6: at least 4',[0,-1.25,0],'label','primary');self.play(Create(inner),FadeIn(innerlabel),run_time=.7)
        self.at('Both pairs');self.at('The only unpaired');middle=SurroundingRectangle(numbers[2],color=CORAL,buff=.13);self.play(Create(middle),run_time=.5)
        self.at('Put the prediction there');opt=txt('8 + 4 + 0 = 12',[0,-2.8,0]);self.play(FadeIn(opt),run_time=.5)
        self.at('This pairing');note=txt('pair from the outside inward',[0,5.1,0],'label');self.play(FadeOut(head),FadeIn(note),run_time=.5)
        self.at('Each outside pair');self.at('The middle observation reaches');self.at('That is why');name=txt('median: minimum absolute error',[0,-3.65,0],'label');self.play(FadeIn(name),run_time=.4)
        self.at('Now move');self.play(FadeOut(VGroup(numbers[-1],outerlabel,opt)),run_time=.2);self.play(dots[-1].animate.move_to([x(14),3.5,0]),Transform(outer,Line([x(1),1.4,0],[x(14),1.4,0],color=TEAL,stroke_width=6)),run_time=1.4);new_end_label=txt('14',[x(14),2.7,0],'label');outerlabel=txt('1 to 14: at least 13',[0,.6,0],'label','primary');opt=txt('13 + 4 + 0 = 17',[0,-2.8,0]);self.play(FadeIn(VGroup(new_end_label,outerlabel,opt)),run_time=.4)
        self.at('The total error grows');self.at('In machine learning');self.at('A different loss');self.finish()
