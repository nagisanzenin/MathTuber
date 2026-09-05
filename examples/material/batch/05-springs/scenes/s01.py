from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        force=ValueTracker(0);k=2.;rest=1.05;bottom0=1.1;left=-1.7;right=1.65;topL=bottom0+2*rest;topR=bottom0+rest
        self.add(self.line([left-.7,topL,0],[left+.7,topL,0],'ink',4),self.line([right-.9,topR,0],[right+.9,topR,0],'ink',4))
        def spring(x,top,bottom,color):
            pts=[[x,top,0],[x,top-.10,0]]
            for j in range(13):pts.append([x+(.16 if j%2 else -.16),top-.16-(top-bottom-.32)*j/12,0])
            pts += [[x,bottom+.10,0],[x,bottom,0]]
            return VMobject().set_points_as_corners(pts).set_stroke(self.palette[color],3)
        def arrangement():
            F=force.get_value();ext=F/k;mid=topL-rest-ext;bot=bottom0-2*ext;botR=bottom0-ext/2
            chain=VGroup(spring(left,topL,mid,'primary'),spring(left,mid,bot,'primary'),self.bead(.18,'primary').move_to([left,bot-.18,0]))
            pair=VGroup(spring(right-.4,topR,botR,'secondary'),spring(right+.4,topR,botR,'secondary'),self.line([right-.4,botR,0],[right+.4,botR,0],'ink',3),self.bead(.18,'secondary').move_to([right,botR-.18,0]))
            result=VGroup(chain,pair)
            if F>.001:
                for x,b in [(left,bot),(right,botR)]:result.add(Arrow([x,b-.4,0],[x,b-.4-.35*F,0],buff=0,stroke_width=3,max_tip_length_to_length_ratio=.3,color=self.palette['ink']))
            return result
        live=always_redraw(arrangement);self.add(live)
        self.at('The same two');self.play(force.animate.set_value(1),run_time=2);self.at('It depends');scope=self.label('identical springs • settled positions',[0,5.2,0],'muted','label').scale(.85);self.add(scope)
        names=VGroup(self.label('in a chain',[left,3.9,0],'primary','label'),self.label('side by side',[right,3.9,0],'secondary','label'));self.add(names)
        self.at('Imagine identical');self.at('In a chain, each spring');self.at('Both extensions');note=self.label('full pull through each',[0,-1.8,0],'primary','label');self.play(FadeIn(note),run_time=.5)
        self.at('Put the springs');self.play(FadeOut(note),run_time=.4);note=self.label('half the pull through each',[0,-1.8,0],'secondary','label');self.play(FadeIn(note),run_time=.4)
        self.at('They stretch');self.at('Each needs');self.at('So two springs');self.play(FadeOut(note),run_time=.4)
        zero=self.line([-2.7,bottom0,0],[2.7,bottom0,0],'muted',1);self.add(zero)
        def measures():
            F=force.get_value();return VGroup(self.line([left-.6,bottom0,0],[left-.6,bottom0-F,0],'primary',4),self.line([right+.8,bottom0,0],[right+.8,bottom0-F/4,0],'secondary',4))
        measure=always_redraw(measures);self.add(measure)
        eq=self.label('chain: 2 ×     beside: ½ ×',[0,-2.25,0],'ink','claim').scale(.8);self.play(FadeIn(eq),run_time=.5)
        self.at('The side');self.at('Between the two');ratio=self.label('same pull → 4 : 1 extension',[0,-3.2,0],'ink','label');self.play(FadeIn(ratio),run_time=.5)
        self.at('Now double');self.play(force.animate.set_value(2),run_time=2);self.at('Both total');self.at('We are comparing');self.at('The way');self.finish()
