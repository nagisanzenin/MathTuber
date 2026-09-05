from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        outer=2.15;inner=1.45;ann=Annulus(inner_radius=inner,outer_radius=outer,fill_color=self.palette['primary'],fill_opacity=.65,stroke_color=self.palette['ink'],stroke_width=2).move_to(UP*1.1);self.add(ann,self.text('Compare a single horizontal slice.'))
        self.at('outer radius squared');self.show(self.text('outer radius² = R² − z²',-1.55,'primary','label'))
        self.at('Remove the hole');self.play(Circumscribe(Circle(radius=inner).move_to(UP*1.1),color=self.palette['secondary']),run_time=1);self.show(self.text('hole radius² = a²',-2.2,'secondary','label'))
        self.at('area pi times');eq=self.text('AREA = π(R² − z² − a²)',-3);self.show(eq)
        self.at('Replace R squared');self.play(Transform(eq,self.text('AREA = π(b² − z²)',-3,'primary')),run_time=1.5)
        self.at('radius has vanished');self.note('R HAS DISAPPEARED.',-4,'secondary')
        self.finish()
