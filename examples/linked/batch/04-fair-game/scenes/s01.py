from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        x=ValueTracker(2);basey=1.5;step=.88;xx=lambda k:-2.64+step*k;board=VGroup(*[VGroup(self.tile(.73,.73,'surface'),self.label(str(k),ORIGIN,'ink','detail')).move_to([xx(k),basey,0]) for k in range(7)]);token=always_redraw(lambda:Dot([xx(x.get_value()),basey+.56,0],radius=.15,color=self.palette['secondary']));self.add(board,token);self.say('Fair coin. Unequal odds?')
        self.at('Heads adds one');self.play(x.animate.set_value(3),run_time=.7)
        self.at('Tails takes one');self.play(x.animate.set_value(2),run_time=.7)
        self.at('Reach six tokens');self.play(Indicate(board[6]),run_time=.8)
        self.at('Reach zero');self.play(Indicate(board[0]),run_time=.7)
        self.at('give each position a height');o=np.array([-2.64,-2.7,0]);axes=VGroup(self.line(o,o+RIGHT*5.28,'muted',2),self.line(o,o+UP*2.9,'muted',2));self.play(Create(axes),run_time=.6);self.add(self.label('winning chance',[0,-3.3,0],'ink','detail'));dots=VGroup(*[Dot([xx(k),-2.7+k*.42,0],radius=.085,color=self.palette['primary']) for k in range(7)]);ends=VGroup(dots[0],dots[6]);self.play(FadeIn(ends),run_time=.6)
        self.at('Zero tokens means');self.add(self.label('0',[xx(0)-.2,-2.95,0],'ink','detail'))
        self.at('Six tokens means');self.add(self.label('1',[xx(6)+.22,-.0,0],'ink','detail'))
        self.at('What height belongs');unknown=VGroup(*[self.label('?', [xx(k),-1.35,0],'muted') for k in range(1,6)]);self.play(FadeIn(unknown),run_time=.5);self.say('Find the missing heights.')
        self.at('one step left or one step right');arrows=VGroup(Arrow([xx(2),2.4,0],[xx(1),2.4,0],buff=.12,color=self.palette['ink']),Arrow([xx(2),2.4,0],[xx(3),2.4,0],buff=.12,color=self.palette['ink']));self.play(Create(arrows),run_time=.8);oddslabel=self.label('½ each',[xx(2),3.0,0],'ink','detail');self.add(oddslabel)
        self.at('average of those two neighbors');self.say('Current chance = average of neighbors')
        self.at('Each middle dot');self.play(FadeOut(unknown),FadeIn(dots[1:6]),run_time=.8);neighbor=self.line(dots[1].get_center(),dots[3].get_center(),'secondary',6);self.play(Create(neighbor),Indicate(dots[2]),run_time=1)
        self.at('equal steps all the way');line=self.line(dots[0].get_center(),dots[6].get_center(),'primary',3);self.play(Create(line),FadeOut(neighbor),run_time=1);self.say('Equal averages force equal steps.')
        self.at('Starting at two');mark=always_redraw(lambda:Dot([xx(x.get_value()),-2.7+x.get_value()*.42,0],radius=.14,color=self.palette['secondary']));link=always_redraw(lambda:DashedLine([xx(x.get_value()),basey,0],[xx(x.get_value()),-2.7+x.get_value()*.42,0],color=self.palette['secondary']));self.add(mark,link);self.say('2 out of 6 → ⅓ chance')
        self.at('Move the start to three');self.remove(arrows,oddslabel);self.play(x.animate.set_value(3),run_time=1.5);self.say('3 out of 6 → ½ chance')
        self.at('Start at five');self.play(x.animate.set_value(5),run_time=1.5);self.say('5 out of 6 → ⅚ chance');self.finish()
