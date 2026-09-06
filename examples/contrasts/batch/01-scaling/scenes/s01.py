from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        INK=self.palette['ink'];TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent']
        def txt(s,p,role='label',color='ink'):return self.label(s,p,color,role)
        origin=np.array([-1.7,.5,0]);a=origin+RIGHT*2;b=origin+UP*3
        axes=VGroup(Line(origin+LEFT*.4,origin+RIGHT*4,color=INK),Line(origin+DOWN*.4,origin+UP*3.6,color=INK))
        points=VGroup(Dot(origin,color=INK,radius=.12),Dot(a,color=TEAL,radius=.15),Dot(b,color=CORAL,radius=.15))
        labels=VGroup(txt('query',origin+DOWN*.55),txt('A',a+DOWN*.5),txt('B',b+RIGHT*.45))
        self.add(axes,points,labels)
        self.at('Can changing');self.play(Indicate(points[0],color=GOLD),run_time=.7)
        self.at('Here is a tiny');da=Line(origin,a,color=TEAL,stroke_width=5);db=Line(origin,b,color=CORAL,stroke_width=5);self.play(Create(da),Create(db),run_time=1)
        self.at('The query');values=VGroup(txt('2',origin+RIGHT+UP*.4),txt('3',origin+UP*1.5+LEFT*.4));self.play(FadeIn(values),run_time=.5)
        self.at('Using these raw');decision=txt('raw distance → A',[0,-1.5,0],'claim');self.play(FadeIn(decision),Indicate(points[1],color=GOLD),run_time=.7)
        self.at('Now write');self.remove(decision);header=txt('first feature: unit ÷ 100',[0,5,0],'claim');self.play(FadeIn(header),run_time=.5)
        self.at('Two becomes');values[0].become(txt('200',origin+RIGHT+UP*.4));scalehint=txt('same plot; horizontal labels converted',[0,-.55,0]);self.play(FadeIn(scalehint),run_time=.5)
        self.at('Nothing about');self.at('But raw');decision=txt('raw distance → B',[0,-1.5,0],'claim');self.add(decision);self.play(Indicate(points[2],color=GOLD),run_time=.7)
        self.at('Distance adds');self.play(FadeOut(VGroup(axes,points,labels,values,da,db,scalehint,header)),run_time=.6);formula=txt('distance² = dx² + dy²',[0,4.6,0],'claim');self.play(FadeIn(formula),run_time=.5)
        self.at('Before the conversion');self.remove(decision);table=VGroup(txt('A: 2² + 0² = 4',[0,3,0],'claim'),txt('B: 0² + 3² = 9',[0,1.8,0],'claim'));self.play(FadeIn(table),run_time=.6)
        self.at('Afterward');self.add(decision);table[0].become(txt('A: 200² + 0² = 40,000',[0,3,0],'claim'));self.play(Indicate(table[0],color=GOLD),run_time=.6)
        self.at('The first feature has gained');self.at('We can choose');self.play(FadeOut(VGroup(formula,table,decision)),run_time=.6);rule=txt('difference ÷ reference scale',[0,4.6,0],'claim');self.play(FadeIn(rule),run_time=.5)
        self.at('Divide each');normalized=txt('distance²\n= (dx/sx)² + (dy/sy)²',[0,3.2,0],'claim');self.play(FadeIn(normalized),run_time=.5)
        self.at('Initially');scales=txt('sx = 1       sy = 1',[0,1.8,0],'claim');self.play(FadeIn(scales),run_time=.5)
        self.at('When the first');scales=self.replace_label(scales,txt('sx = 100       sy = 1',[0,1.8,0],'claim'));conversion=txt('dx × 100       sx × 100',[0,.3,0]);self.play(FadeIn(conversion),run_time=.5)
        self.at('Two hundred divided');ratio=txt('200 / 100 = 2',[0,-1.1,0],'claim');self.play(FadeIn(ratio),run_time=.6)
        self.at('The dimensionless');self.play(FadeOut(VGroup(rule,normalized,scales,conversion,ratio)),run_time=.6);self.add(axes,points,labels,da,db);values=VGroup(txt('2',origin+RIGHT+UP*.4),txt('3',origin+UP*1.5+LEFT*.4));self.add(values);heading=txt('dimensionless comparison',[0,5,0],'claim');decision=txt('scaled distance → A',[0,-1.5,0],'claim');self.play(FadeIn(heading),FadeIn(decision),Indicate(points[1],color=GOLD),run_time=.7)
        self.at('A consistent');self.at('The reference');self.play(FadeOut(VGroup(axes,points,labels,da,db,values,heading,decision)),run_time=.6);ending=VGroup(txt('units change',[0,4,0],'claim'),txt('reference scales change with them',[0,2.5,0]),txt('comparison stays the same',[0,1,0],'claim'));self.play(FadeIn(ending),run_time=.6)
        self.at('Learning useful');self.at('Before asking');self.finish()
