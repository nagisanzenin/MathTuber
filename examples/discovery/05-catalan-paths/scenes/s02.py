from scenes._shared.design import *

class Shot2(Stage):
    sid="s02"
    def construct(self):
        self.title('REFLECT THE FIRST CROSSING')
        origin=np.array([-2.4,-1.3,0]);u=1.12;g=grid(3,u,origin,wide=4);self.show(g);seq='RUURRU';pts=vertices(seq,u,origin);pre=path('RUU',RED,u,origin);suffix=VMobject(color=BLUE,stroke_width=6).set_points_as_corners(pts[3:]);self.play(Create(pre),Create(suffix),run_time=1.8)
        self.at('one more up step');marker=Dot(pts[3],radius=.14,color=GOLD);self.show(marker);status=label('First crossing: 2 up, 1 right',-2.8,RED,30);self.show(status)
        self.at('Reflect just the beginning');newpre=path('URR',GREEN,u,origin);newpts=vertices('URRRRU',u,origin);newsuffix=VMobject(color=BLUE,stroke_width=6).set_points_as_corners(newpts[3:]);self.play(Transform(pre,newpre),Transform(suffix,newsuffix),marker.animate.move_to(newpts[3]),Transform(status,label('Reflected: 2 right, 1 up',-2.8,GREEN,30)),run_time=1.7)
        self.at('Leave the remaining moves unchanged');newpts=vertices('URRRRU',u,origin);newsuffix=VMobject(color=BLUE,stroke_width=6).set_points_as_corners(newpts[3:]);self.play(Indicate(suffix,color=BLUE),run_time=1.0)
        self.at('four right steps and two up');self.note('3 right / 3 up → 4 right / 2 up',-4,GREEN)
        self.finish()
