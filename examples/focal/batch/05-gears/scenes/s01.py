from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        def gear(n,r,color,phase=0):
            module=2*r/n;base=r*math.cos(20*DEGREES);root=r-1.25*module;outer=r+module
            involute=lambda rad:math.sqrt(max(0,(rad/base)**2-1))-math.acos(min(1,base/rad))
            half=lambda rad:PI/(2*n)+involute(r)-involute(max(base,rad))
            pts=[]
            for k in range(n):
                mid=k*TAU/n+phase
                polar=lambda rad,a:np.array([rad*math.cos(a),rad*math.sin(a),0])
                pts.append(polar(root,mid-PI/n))
                pts.append(polar(root,mid-half(base)))
                for rad in np.linspace(max(root,base),outer,7):pts.append(polar(rad,mid-half(rad)))
                for a in np.linspace(mid-half(outer),mid+half(outer),5):pts.append(polar(outer,a))
                for rad in np.linspace(outer,max(root,base),7):pts.append(polar(rad,mid+half(rad)))
                pts.append(polar(root,mid+half(base)));pts.append(polar(root,mid+PI/n))
            face=Polygon(*pts,color=self.palette['ink'],stroke_width=1.5,fill_color=self.palette[color],fill_opacity=.22)
            return VGroup(face,Circle(radius=r*.65,color=self.palette['muted'],stroke_width=1),Circle(radius=.13,color=self.palette['ink'],fill_color=self.palette['background'],fill_opacity=1),self.line([0,0,0],[0,r*.78,0],color,5))
        small=gear(16,.9,'primary').shift(LEFT*1.8);large=gear(32,1.8,'secondary',PI/32).shift(RIGHT*.9)
        subject=VGroup(small,large).scale(.75).shift(UP*1.5);self.add(subject)
        self.at('Two gears can');self.play(Rotate(small,TAU,about_point=small.get_center()),Rotate(large,-PI,about_point=large.get_center()),run_time=3,rate_func=linear)
        self.at('The smaller one completes');self.at('Come closer');self.stage_focus(subject,UP*.8,width=6.5,height=6.2,run_time=1.6)
        cs=small.get_center().copy();cl=large.get_center().copy()
        scope=self.label('ideal ratio • schematic teeth',[0,5.15,0],'muted','label').scale(.85);self.add(scope)
        self.at('These gears have');self.at('One has sixteen');labels=VGroup(self.label('16 teeth',cs+DOWN*1.7,'primary','label'),self.label('32 teeth',cl+DOWN*2.5,'secondary','label'));self.play(FadeIn(labels),run_time=.6)
        self.at('A full turn');self.play(Rotate(small,TAU,about_point=cs),Rotate(large,-PI,about_point=cl),run_time=3,rate_func=linear)
        self.at('That advances');relation=self.label('1 small turn → ½ large turn',[0,-3.2,0],'ink','claim').scale(.83);self.play(FadeIn(relation),run_time=.5)
        self.at('Another sixteen');self.play(Rotate(small,TAU,about_point=cs),Rotate(large,-PI,about_point=cl),run_time=2.5,rate_func=linear)
        self.at('The two gears');self.at('Their angular');self.play(FadeOut(relation),run_time=.3);eq=self.label('teeth × turns per second = constant',[0,-3.2,0],'ink','claim').scale(.76);self.play(FadeIn(eq),run_time=.5)
        self.at('Twice as many');self.at('The drawn teeth');self.at('Now let');self.focus_outline(large,run_time=.7)
        self.at('One large turn');self.play(Rotate(large,-TAU,about_point=cl),Rotate(small,2*TAU,about_point=cs),run_time=3,rate_func=linear)
        self.at('The relationship');self.at('A quiet mechanical');clock=self.process_clock(rate=.5);a=small.copy();b=large.copy();moving=always_redraw(lambda:VGroup(a.copy().rotate(clock.value,about_point=cs),b.copy().rotate(-clock.value/2,about_point=cl)));self.remove(small,large);self.add(moving);self.finish()
