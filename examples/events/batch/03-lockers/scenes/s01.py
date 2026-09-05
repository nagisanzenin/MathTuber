from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        def door(i,opened=False):
            pos=np.array([((i-1)%4-1.5)*1.45,3-((i-1)//4)*1.5,0]);box=RoundedRectangle(width=1.12,height=1.18,corner_radius=.08,fill_color=self.palette['accent' if opened else 'primary'],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=2).move_to(pos);leaf=Rectangle(width=.16 if opened else .90,height=1.02,fill_color=self.palette['primary'],fill_opacity=1,stroke_color=self.palette['ink'],stroke_width=1).move_to(pos+LEFT*(.42 if opened else 0));knob=Dot(pos+RIGHT*(-.42 if opened else .30),radius=.035,color=self.palette['background']);return VGroup(box,leaf,knob,self.label(str(i),pos+UP*.82,'ink','detail'))
        doors=VGroup(*[door(i) for i in range(1,17)]);self.add(doors);self.say('Which doors stay open?');state=[False]*16
        def toggle(k,duration):
            changes=[]
            for i in range(k,17,k):
                state[i-1]=not state[i-1];changes.append(Transform(doors[i-1],door(i,state[i-1])))
            self.play(*changes,run_time=duration)
        self.at('first pass');toggle(1,.6)
        self.at('On the second');toggle(2,.6)
        self.at('On the third');toggle(3,.6)
        self.at('You might notice a pattern');self.wait(.1)
        for k in range(4,17):toggle(k,.18)
        self.at('Here is the result');self.say('1, 4, 9, 16')
        self.at('Watch door twelve');self.play(doors.animate.scale(.32).move_to([2.15,-2.7,0]),run_time=.6);focus=door(12).scale(2.0).move_to([0,1.4,0]);self.add(focus);self.say('Who visits door 12?')
        self.at('passes one, two');factors=[1,2,3,4,6,12];tokens=VGroup(*[self.tile(.76,.65,'surface',str(i)).move_to([-2.5+j, -.8,0]) for j,i in enumerate(factors)]);[t[-1].set_color(self.palette['ink']) for t in tokens];self.play(LaggedStart(*[FadeIn(t) for t in tokens],lag_ratio=.3),run_time=2)
        self.at('Now pair those divisors');self.play(FadeOut(focus),run_time=.4);positions={1:(-1.2,2.5),12:(1.2,2.5),2:(-1.2,1.2),6:(1.2,1.2),3:(-1.2,-.1),4:(1.2,-.1)};self.play(*[token.animate.move_to([*positions[i],0]) for token,i in zip(tokens,factors)],run_time=1);multipliers=VGroup(*[self.label('×',[0,y,0]) for y in [2.5,1.2,-.1]]);self.add(multipliers)
        self.at('They cancel');self.play(*[Indicate(t) for t in tokens],run_time=.6);self.say('3 pairs → 6 toggles → closed')
        self.at('Door sixteen looks');self.play(FadeOut(tokens),FadeOut(multipliers),run_time=.5);self.say('Door 16: find the missing partner');pairs=VGroup(*[self.label(t,[0,y,0],'primary','claim') for t,y in [('1 × 16',2.5),('2 × 8',1.2),('4 × 4',-.1)]]);self.play(LaggedStart(*[FadeIn(t) for t in pairs],lag_ratio=.5),run_time=1.5)
        self.at('only one pass four');self.play(Indicate(pairs[2]),run_time=.7);self.say('Pass 4 happens only once.')
        self.at('The door stays open');self.play(FadeOut(pairs),run_time=.5);result=door(16,True).scale(2.2).move_to([0,1,0]);self.add(result);self.say('5 toggles → open')
        self.at('Now extend the hallway');self.play(FadeOut(result),FadeOut(doors),run_time=.5);self.say('100 doors. How many stay open?');self.add(self.label('1², 2², 3², …, 10²',[0,1.5,0],'primary','claim'))
        self.at('Exactly ten open doors');self.add(self.label('10 open doors',[0,0,0],'secondary','claim'));self.finish()
