from scenes._shared.design import *
class Film(Stage):
    def construct(self):
        TEAL=self.palette['primary'];INK=self.palette['ink'];CORAL=self.palette['secondary'];step=.52;N=12;O=np.array([-2.86,-2.0,0]);stretch=ValueTracker(1)
        def point(c,r):return np.array([step*(c-(N-1)/2)*stretch.get_value(),-2+step*r,0])
        def base_threads():return VGroup(*[Line(point(c,-.4),point(c,N-.6),color='#B6A17D',stroke_width=36) for c in range(N)])
        def row_lines(r):
         group=VGroup(Line(point(-.4,r),point(N-.6,r),color=TEAL,stroke_width=34))
         for c in range(N):
          if (c-r)%4>=2:group.add(Line(point(c,r-.38),point(c,r+.38),color='#B6A17D',stroke_width=36))
         return group
        warp=base_threads();rows=VGroup(*[row_lines(r) for r in range(N)]);self.add(warp,rows)
        self.at('These diagonal');self.at('No thread travels');highlight=Line(point(0,4),point(N-1,4),color=CORAL,stroke_width=3);self.play(Create(highlight),run_time=1.4);self.at('The slant comes');self.play(FadeOut(highlight),run_time=.3)
        self.at('Keep the upright');self.play(FadeOut(rows),run_time=.8)
        self.at('Pass a crossing');one=row_lines(0);self.play(Create(one),run_time=2.5);label=self.label('over 2 · under 2',[0,-3.2,0],role='claim');self.play(FadeIn(label),run_time=.3)
        self.at('For the next row');two=row_lines(1);self.play(Create(two),run_time=2);self.at('Keep repeating');more=VGroup(*[row_lines(r) for r in range(2,N)]);self.play(LaggedStart(*[Create(row) for row in more],lag_ratio=.13),run_time=3)
        self.at('A visible patch');patches=VGroup(*[Rectangle(width=step*1.75,height=.27,stroke_color=CORAL,stroke_width=3).move_to(point(r+.5,r)) for r in range(7)]);self.play(LaggedStart(*[Create(x) for x in patches],lag_ratio=.15),run_time=2.5)
        self.at('Those patches');diagonal=DashedLine(point(.5,0),point(6.5,6),color=CORAL,stroke_width=3);self.play(Create(diagonal),run_time=1)
        self.at('The diagonal belongs');label=self.replace_label(label,self.label('a pattern, not a thread',[0,-3.2,0],role='claim'),.4)
        self.at('After four rows');self.play(FadeOut(patches),FadeOut(diagonal),run_time=.4);bounds=VGroup(*[SurroundingRectangle(row_lines(r),color=CORAL,buff=.13,stroke_width=3) for r in (0,4)]);self.play(Create(bounds),run_time=.8)
        self.at('There are four');label=self.replace_label(label,self.label('0 → 1 → 2 → 3 → 0',[0,-3.2,0],role='claim'),.4)
        self.at('With equally spaced');self.play(FadeOut(bounds),run_time=.3);diagonal=DashedLine(point(.5,0),point(7.5,7),color=CORAL,stroke_width=4);self.play(Create(diagonal),run_time=.8);label=self.replace_label(label,self.label('equal spacing: 45°',[0,-3.2,0],role='claim'),.4)
        self.at('Spread the upright');label=self.replace_label(label,self.label('same repeat · wider columns',[0,-3.2,0],role='claim'),.3);self.clear();self.add(label);O=np.array([-2.86,-2,0]);fabric=always_redraw(lambda:VGroup(base_threads(),*[row_lines(r) for r in range(N)]));diag=always_redraw(lambda:DashedLine(point(.5,0),point(7.5,7),color=CORAL,stroke_width=4));self.add(fabric,diag)
        # Keep the wider fabric centered by moving its origin along with the stretch.
        center=np.array([0,.86,0]);O=np.array([-2.86,-2,0]);q=ValueTracker(0)
        def update_origin(_):O[0]=-2.86*stretch.get_value()
        driver=Mobject();self.add(driver);self.play(stretch.animate.set_value(1.16),run_time=2)
        self.at('The crossing order stays');label=self.replace_label(label,self.label('same repeat · changed angle',[0,-3.2,0],role='claim'),.4)
        self.at('This is one');self.play(FadeOut(diag),run_time=.3);self.at('Sometimes a line');self.finish()
