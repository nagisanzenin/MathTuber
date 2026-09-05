from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        def ant(x,y,color):
            body=VGroup(*[Ellipse(width=.18,height=.23,fill_color=self.palette[color],fill_opacity=1,stroke_width=0).move_to([x+dx,y,0]) for dx in [-.14,0,.14]])
            legs=VGroup(*[self.line([x+dx,y,0],[x+dx+side*.1,y+side*.22,0],'ink',2) for dx in [-.12,0,.12] for side in [-1,1]])
            badge=self.label('A' if color=='primary' else 'B',[x,y+.5,0],'ink','detail')
            return VGroup(legs,body,badge).scale(1.35)
        a=ant(-1.5,1.5,'primary');b=ant(1.5,1.5,'secondary');self.add(self.line([-3,1.2,0],[3,1.2,0],'surface',18),a,b)
        self.play(a.animate.shift(RIGHT*1.28),b.animate.shift(LEFT*1.28),run_time=.7);self.play(a.animate.shift(LEFT*1.28),b.animate.shift(RIGHT*1.28),run_time=.7);self.say('Do collisions delay escape?')
        self.at('Our ants are points');self.play(FadeOut(a),FadeOut(b),run_time=.4);starts=[1,3,4,7,9];dirs=[1,1,-1,-1,1];xx=lambda x:-3+.6*x;ants=VGroup(*[Dot([xx(x),1.35,0],radius=.10,color=self.palette['primary']) for x in starts]);arrows=VGroup(*[Arrow([xx(x),2.05,0],[xx(x)+.4*v,2.05,0],buff=0,color=self.palette['ink'],stroke_width=3) for x,v in zip(starts,dirs)]);self.add(ants,arrows,self.label('10 m stick • speed 1 m/s',[0,.55,0],'ink','detail'))
        self.at('Before tracking');self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.caption],run_time=.5);self.say('Same positions. Different identities.')
        for y,label in [(2,'bounce'),(-1,'ghost crossing')]:self.add(self.line([-3,y-.35,0],[3,y-.35,0],'surface',15),self.label(label,[-1.9,y+.8,0],'ink','detail'))
        a=ant(-2,2,'primary');b=ant(2,2,'secondary');ga=ant(-2,-1,'primary');gb=ant(2,-1,'secondary');self.add(a,b,ga,gb)
        self.at('In the real model');self.play(a.animate.move_to([0,2,0]),b.animate.move_to([0,2,0]),run_time=1);self.play(a.animate.move_to([-2,2,0]),b.animate.move_to([2,2,0]),run_time=1)
        self.at('Now imagine ghosts');self.play(ga.animate.move_to([2,-1,0]),gb.animate.move_to([-2,-1,0]),run_time=2)
        self.at('occupied positions are identical');links=VGroup(*[DashedLine([x,1.7,0],[x,-.7,0],color=self.palette['muted']) for x in [-2,2]]);self.play(Create(links),run_time=.7)
        self.at('At the collision');self.remove(links);self.play(a.animate.move_to([0,2,0]),b.animate.move_to([0,2,0]),ga.animate.move_to([0,-1,0]),gb.animate.move_to([0,-1,0]),run_time=.8);ga[2].become(self.label('B',ga[2].get_center(),'ink','detail'));gb[2].become(self.label('A',gb[2].get_center(),'ink','detail'));self.play(ga[1].animate.set_color(self.palette['secondary']),gb[1].animate.set_color(self.palette['primary']),run_time=.5);self.play(a.animate.move_to([-2,2,0]),b.animate.move_to([2,2,0]),ga.animate.move_to([2,-1,0]),gb.animate.move_to([-2,-1,0]),run_time=1)
        self.at('Replace every collision');self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.caption],run_time=.5);self.say('Ignore identity. Keep every path.')
        travel=ValueTracker(0)
        for i,(x,v,t) in enumerate(zip(starts,dirs,[9,7,4,7,1])):
            y=3-i*1.2;self.add(self.line([-3,y,0],[3,y,0],'surface',8),Circle(radius=.075,stroke_color=self.palette['primary'],stroke_width=2,fill_opacity=0).move_to([xx(x),y,0]),Arrow([xx(x),y,0],[xx(10 if v>0 else 0),y,0],buff=.04,color=self.palette['primary'],stroke_width=4),self.label(str(t)+' s',[2.7 if v<0 else -2.7,y+.32,0],'ink','detail'))
        movers=always_redraw(lambda:VGroup(*[Dot([xx(x+v*travel.get_value()),3-i*1.2,0],radius=.13,color=self.palette['secondary']) for i,(x,v,t) in enumerate(zip(starts,dirs,[9,7,4,7,1])) if travel.get_value()<t]))
        self.add(movers,self.label('ring = start • dot = moving ant',[0,-3.2,0],'ink','detail'))
        self.at('This ant starts');self.play(travel.animate.set_value(9),run_time=9,rate_func=linear)
        self.at('last departure is nine');self.say('Last departure: 9 seconds')
        self.at('adding a real pause');self.say('What if collisions take time?',color='secondary')
        self.at('No. The immediate');self.say('Pauses break the trick.');self.finish()
