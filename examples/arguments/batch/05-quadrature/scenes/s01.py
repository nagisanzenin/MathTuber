from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        ax=Axes(x_range=[0,2,1],y_range=[0,4,1],x_length=5,y_length=4,axis_config={'color':INK,'include_tip':False}).move_to([0,2,0]);curve=ax.plot(lambda x:x*x,color=TEAL);area=ax.get_area(curve,x_range=[0,2],color=TEAL,opacity=.2);title=txt('y = x²',[0,5.4,0],'claim');self.add(ax,area,curve,title)
        self.at('Three height');self.at('Take x squared');points=VGroup(*[Dot(ax.c2p(x,x*x),color=CORAL) for x in [0,1,2]]);heights=txt('heights: 0    1    4',[0,-.7,0]);self.play(FadeIn(points),FadeIn(heights),run_time=.5)
        self.at('A straight line');trap=Polygon(ax.c2p(0,0),ax.c2p(2,0),ax.c2p(2,4),fill_color=CORAL,fill_opacity=.2,stroke_color=CORAL);calc=txt('trapezoid area = 4',[0,-1.9,0],'claim');self.play(FadeIn(trap),FadeIn(calc),run_time=.7)
        self.at('A rectangle');rect=Polygon(ax.c2p(0,0),ax.c2p(2,0),ax.c2p(2,1),ax.c2p(0,1),fill_color=GOLD,fill_opacity=.3,stroke_color=GOLD);self.play(FadeOut(trap),FadeIn(rect),run_time=.5);calc=self.replace_label(calc,txt('midpoint area = 2',[0,-1.9,0],'claim'))
        self.at('For a quadratic');self.play(FadeOut(rect),run_time=.3);calc=self.replace_label(calc,txt('(2/3) × 2 + (1/3) × 4',[0,-1.9,0],'claim'))
        self.at('That gives');calc=self.replace_label(calc,txt('area = 8/3',[0,-1.9,0],'claim'))
        self.at('In terms');rule=txt('(width / 6) × (left + 4 middle + right)',[0,-3.2,0]);self.play(FadeIn(rule),run_time=.5)
        self.at('The middle receives');self.focus_outline(points[1],run_time=.6)
        self.at('Why can that');self.play(FadeOut(rule),run_time=.3);basis=txt('constant + linear + quadratic',[0,-3.2,0]);self.play(FadeIn(basis),run_time=.5)
        self.at('These weights');self.at('Try x to');self.play(FadeOut(VGroup(area,curve,points,heights,calc,basis,title)),run_time=.4);newcurve=ax.plot(lambda x:x**4/4,color=TEAL);self.play(Create(newcurve),run_time=.7);title=txt('y = x⁴ · vertical scale ÷ 4',[0,5.4,0]);heights=txt('heights: 0    1    16',[0,-.7,0]);self.play(FadeIn(title),FadeIn(heights),run_time=.4)
        self.at('The three heights now');calc=txt('Simpson: 20/3\nexact: 32/5',[0,-2,0],'claim');self.play(FadeIn(calc),run_time=.5)
        self.at('The values differ');self.finish()
