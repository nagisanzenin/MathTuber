from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        positions=[np.array([x,3,0]) for x in [-2.2,0,2.2]];angle=ValueTracker(PI/4)
        def panel(i,theta):
            p=positions[i];v=np.array([math.sin(theta),math.cos(theta),0]);return VGroup(Circle(radius=.8,fill_color=self.palette['surface'],fill_opacity=.7,stroke_color=self.palette['muted'],stroke_width=2).move_to(p),self.line(p-v*.65,p+v*.65,'primary',5))
        first=panel(0,0);last=panel(2,PI/2);middle=always_redraw(lambda:panel(1,angle.get_value()))
        self.add(first,last,self.label('successive filters · front views',[0,5.4,0],'ink','detail'))
        def meter(i,value):
            x=positions[i][0];bottom=1.35;h=.9*value
            return VGroup(Rectangle(width=.32,height=.9,stroke_color=self.palette['muted'],stroke_width=1).move_to([x,bottom+.45,0]),Rectangle(width=.32,height=max(.001,h),stroke_width=0,fill_color=self.palette['accent'],fill_opacity=1 if value>0 else 0).move_to([x,bottom+h/2,0]))
        m1=meter(0,1);m3=meter(2,0);self.add(m1,m3)
        self.at('Place another filter');self.play(FadeIn(middle),run_time=.9);self.remove(m3);m2=always_redraw(lambda:meter(1,math.cos(angle.get_value())**2));m3=always_redraw(lambda:meter(2,(math.cos(angle.get_value())*math.sin(angle.get_value()))**2));self.add(m2,m3)
        self.at('Nothing has created');self.focus_outline(m3,run_time=.8)
        self.at('Their lines mark');self.focus_outline(middle,run_time=.8)
        self.at('After the first filter the light');self.focus_outline(first,run_time=.8)
        self.at('Call its intensity');one=self.label('1',[-2.2,.8,0],'ink','label');self.play(FadeIn(one),run_time=.4)
        self.at('The last filter transmits');self.focus_outline(last,run_time=.8)
        o=np.array([-.8,-1.7,0]);v=np.array([0,1.7,0]);e=np.array([1,1,0])/math.sqrt(2);p=np.dot(v,e)*e;q=np.array([p[0],0,0])
        vertical=Arrow(o,o+v,buff=0,color=self.palette['primary'],stroke_width=5);horizontal=self.line(o,o+RIGHT*2,'muted',2);zero=Dot(o,radius=.08,color=self.palette['secondary']);fieldlabel=self.label('field components',[0,-2.5,0],'ink','detail')
        self.at('A vertical vibration');self.play(GrowArrow(vertical),Create(horizontal),FadeIn(fieldlabel),run_time=1)
        self.at('So without the middle');self.play(FadeOut(middle),FadeOut(m2),FadeOut(m3),run_time=.5);zero_meter=meter(2,0);self.add(zero_meter,zero);zerolabel=self.label('0',[2.2,.8,0],'ink','label');self.add(zerolabel)
        self.at('Now look at the slanted');self.remove(zero,zero_meter,zerolabel);self.add(middle,m2,m3);diagonal=self.line(o-e*.3,o+e*2.2,'muted',2);self.play(Create(diagonal),run_time=.6)
        self.at('An ideal filter keeps');drop1=DashedLine(o+v,o+p,dash_length=.09,stroke_width=2,color=self.palette['muted']);self.play(Create(drop1),run_time=.8)
        self.at('The vertical field has');arrow1=Arrow(o,o+p,buff=0,color=self.palette['accent'],stroke_width=5);self.play(GrowArrow(arrow1),run_time=.8)
        self.at('The diagonal field has');drop2=DashedLine(o+p,o+q,dash_length=.09,stroke_width=2,color=self.palette['muted']);arrow2=Arrow(o,o+q,buff=0,color=self.palette['secondary'],stroke_width=5);self.play(Create(drop2),GrowArrow(arrow2),run_time=.9)
        self.at('At forty five degrees each projection');degree=self.label('45°',[0,4.15,0],'ink','label');self.play(FadeIn(degree),run_time=.5)
        self.at('Intensity is proportional');relation=self.label('intensity ∝ field²',[0,-3.15,0],'ink','label');self.play(FadeIn(relation),run_time=.5)
        self.at('One becomes one half');halves=VGroup(self.label('1/2',[0,.8,0],'ink','label'),self.label('1/4',[2.2,.8,0],'ink','label'));self.play(FadeIn(halves),run_time=.6)
        self.at('Turn the middle axis');self.play(*[FadeOut(x) for x in [vertical,horizontal,diagonal,drop1,drop2,arrow1,arrow2,fieldlabel,relation,degree,halves]],run_time=.7);self.play(angle.animate.set_value(0),run_time=1.5)
        self.at('The final light fades');self.play(angle.animate.set_value(PI/2),run_time=1.6)
        self.at('The largest output');self.play(angle.animate.set_value(PI/4),run_time=1.5);self.add(degree,halves)
        self.at('Real filters absorb');note=self.label('ideal filters',[0,-1.8,0],'muted','detail');self.play(FadeIn(note),run_time=.5)
        self.at('Sometimes a path appears');self.play(FadeOut(note),run_time=.5);self.finish()
