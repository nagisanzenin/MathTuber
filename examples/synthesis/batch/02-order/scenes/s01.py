from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];CORAL=self.palette['secondary'];GOLD=self.palette['accent'];INK=self.palette['ink']
        def txt(s,p,role='label'):return self.label(s,p,'ink',role)
        
        ax=Axes(x_range=[-3,3,1],y_range=[-1,3,1],x_length=5.5,y_length=4,axis_config={'color':INK,'include_tip':False}).move_to([0,2,0]);self.add(ax);point=Dot(ax.c2p(1,1),color=TEAL);title=txt('stretch → rotate',[0,5.3,0],'claim');self.add(point,title);label=txt('(1, 1)',[0,-.8,0],'claim');self.add(label)
        def move(v):
         nonlocal label
         self.play(FadeOut(label),run_time=.15);self.play(point.animate.move_to(ax.c2p(*v)),run_time=.8);label=txt(str(tuple(v)),[0,-.8,0],'claim');self.play(FadeIn(label),run_time=.2)
        self.at('Stretch sideways then turn');self.at('Start with');self.at('Stretch first');move((2,1));self.at('Now rotate');move((-1,2));ghost=Dot(ax.c2p(-1,2),color=CORAL);self.add(ghost)
        self.at('Reset to');self.play(FadeOut(title),run_time=.2);title=txt('rotate → stretch',[0,5.3,0],'claim');self.add(title);move((1,1))
        self.at('Rotate first');move((-1,1));self.at('Then stretch');move((-2,1));other=txt('coral: stretch first',[0,-1.9,0]);self.play(FadeIn(other),run_time=.4)
        self.at('Matrices record');rule=txt('rightmost operation acts first',[0,-2.9,0]);self.play(FadeIn(rule),run_time=.5)
        self.at('Rotation after');other=self.replace_label(other,txt('R S ≠ S R',[0,-1.9,0],'claim'))
        self.at('Now stretch both');self.play(FadeOut(VGroup(title,label,other,rule,ghost)),run_time=.3);title=txt('uniform scale ×2',[0,5.3,0],'claim');self.add(title);self.play(point.animate.move_to(ax.c2p(1,1)),run_time=.4)
        self.at('Doubling every');p2=point.copy().set_color(CORAL);self.add(p2);self.play(point.animate.move_to(ax.c2p(2,2)),p2.animate.move_to(ax.c2p(-1,1)),run_time=.8);self.play(point.animate.move_to(ax.c2p(-2,2)),p2.animate.move_to(ax.c2p(-2,2)),run_time=.8);label=txt('both: (−2, 2) · R(2I) = (2I)R',[0,-1.3,0]);self.play(FadeIn(label),run_time=.5)
        self.at('Some transformations');self.finish()
