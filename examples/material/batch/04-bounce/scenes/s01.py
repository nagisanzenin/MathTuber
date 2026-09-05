from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        floor=-1.6;r=.43;H=4.3;g=5.;e=.5
        self.add(self.line([-2.8,floor-r,0],[2.8,floor-r,0],'ink',4));clock=self.process_clock(rate=.7)
        def height(t,restitution):
            drop=math.sqrt(2*H/g);v=math.sqrt(2*g*H)
            if t<drop:return H-.5*g*t*t
            dt=t-drop;flight=2*restitution*v/g
            if dt>flight:return 0
            return max(0,restitution*v*dt-.5*g*dt*dt)
        ball=self.bead(r,'primary');ball.add_updater(lambda m:m.move_to([0,floor+height(clock.value,e),0]));self.add(ball)
        self.at('A falling');self.at('Its bounce');scope=self.label('one vertical bounce • no air drag',[0,5.2,0],'muted','label').scale(.85);self.add(scope)
        self.at('Ignore air');self.at('Suppose the upward');clock.pause();ball.clear_updaters();self.play(ball.animate.move_to([0,floor+H,0]),run_time=.6)
        top=self.line([-2.2,floor+H-r,0],[2.2,floor+H-r,0],'muted',2);quarter=self.line([-2.2,floor+H/4-r,0],[2.2,floor+H/4-r,0],'primary',2);labels=VGroup(self.label('release height',[1.5,floor+H-r+.3,0],'muted','label').scale(.8),self.label('¼ height',[1.5,floor+H/4-r+.3,0],'primary','label'));self.add(top,quarter,labels)
        self.at('That does');self.at('Speed gained');self.at('Going back');self.at('Half the speed');clock=self.process_clock(rate=.7);ball.add_updater(lambda m:m.move_to([0,floor+height(clock.value,e),0]))
        self.at('This speed ratio');eq=self.label('height ratio = speed ratio²',[0,-3,0],'ink','claim').scale(.86);self.play(FadeIn(eq),run_time=.5)
        self.at('In this simple');self.at('Energy also');self.at('Try a speed');clock.pause();ball.clear_updaters();self.play(FadeOut(quarter),FadeOut(labels),ball.animate.move_to([0,floor+H,0]),run_time=.6);e=.75
        newlevel=self.line([-2.2,floor+H*e*e-r,0],[2.2,floor+H*e*e-r,0],'secondary',2);newlabel=self.label('9/16 height',[1.5,floor+H*e*e-r+.3,0],'secondary','label');self.add(newlevel,newlabel);clock=self.process_clock(rate=.7);ball.add_updater(lambda m:m.move_to([0,floor+height(clock.value,e),0]))
        self.at('The returned');self.at('Real bounce');self.at('A small rise');self.finish()
