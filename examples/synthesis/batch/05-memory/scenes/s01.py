from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        row=VGroup(*[Circle(radius=.24,stroke_color=INK,fill_color=CORAL,fill_opacity=.5).move_to([-2+i*.8,3.8,0]) for i in range(5)]);title=txt('independent attempts · p = 1/4',[0,5.3,0],'claim');self.add(row,title)
        self.at('Five failures have passed');self.at('Suppose every');self.at('One more');nexts=VGroup(*[Circle(radius=.24,stroke_color=TEAL).move_to([-.4+i*.8,2.3,0]) for i in range(2)]);self.play(FadeIn(nexts[0]),run_time=.5);calc=txt('one more failure: 3/4',[0,.8,0]);self.play(FadeIn(calc),run_time=.4)
        self.at('Two more failures have chance');self.play(FadeIn(nexts[1]),run_time=.4);calc=self.replace_label(calc,txt('two more failures: 9/16',[0,.8,0]))
        self.at('Let T');self.at('The chance T');formula=txt('P(T > n) = (3/4)ⁿ',[0,-.7,0],'claim');self.play(FadeIn(formula),run_time=.5)
        self.at('Given five');calc=self.replace_label(calc,txt('(3/4)⁷ / (3/4)⁵',[0,.8,0],'claim'))
        self.at('The first five');self.play(FadeOut(row),run_time=.5);calc=self.replace_label(calc,txt('(3/4)² = 9/16',[0,.8,0],'claim'))
        self.at('It describes');self.at('Now draw');self.play(FadeOut(VGroup(nexts,title,calc,formula)),run_time=.4);title=txt('without replacement',[0,5.3,0],'claim');tokens=VGroup(*[Circle(radius=.38,fill_color=TEAL if i==0 else CORAL,fill_opacity=.6,stroke_color=INK).move_to([-1.8+i*1.2,3.3,0]) for i in range(4)]);self.add(title,tokens);legend=txt('teal: success · coral: failure',[0,1.8,0]);self.add(legend)
        self.at('After two');self.play(FadeOut(tokens[2:]),run_time=.6);calc=txt('next success: 1/2',[0,.3,0],'claim');self.play(FadeIn(calc),run_time=.5)
        self.at('Removing failures');self.finish()
