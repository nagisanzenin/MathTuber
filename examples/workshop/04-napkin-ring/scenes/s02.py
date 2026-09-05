from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        c,regions,a=section(self);self.add(c,regions,self.text('The height ties the radii together.'))
        o=UP*.6;p=np.array([a,.6,0]);q=np.array([a,1.9,0]);tri=VGroup(Line(o,p,color=self.palette['secondary'],stroke_width=5),Line(p,q,color=self.palette['accent'],stroke_width=5),Line(o,q,color=self.palette['primary'],stroke_width=5))
        self.at('radius R');self.show(tri[2]);self.show(self.lettering('R',color='primary').move_to((o+q)/2+UL*.23))
        self.at('radius a');self.show(tri[0]);self.show(self.lettering('a',color='secondary').move_to((o+p)/2+DOWN*.3))
        self.at('height is b');self.show(tri[1]);self.show(self.lettering('b',color='ink').move_to((p+q)/2+RIGHT*.3))
        self.at('right triangle');self.show(RightAngle(tri[0],tri[1],length=.18,quadrant=(-1,1),color=self.palette['ink']))
        self.at('R squared minus');self.rule('R² − a² = b²',-2.6)
        self.at('bigger ball needs');self.note('LARGER BALL ↔ WIDER HOLE',-3.6)
        self.finish()
