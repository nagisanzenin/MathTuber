from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        self.title('A PAIRING YOU CAN UNDO')
        origin=np.array([-2.4,-1.3,0]);u=1.12;self.show(grid(3,u,origin,wide=4));pre=path('URR',GREEN,u,origin);pts=vertices('URRRRU',u,origin);suffix=VMobject(color=BLUE,stroke_width=6).set_points_as_corners(pts[3:]);self.show(VGroup(pre,suffix))
        self.at('one more right step');marker=Dot(pts[3],radius=.14,color=GOLD);self.show(marker);status=label('First time: right = up + 1',-2.8,GREEN,30);self.show(status)
        self.at('Reflect that beginning back');back=path('RUU',RED,u,origin);old=vertices('RUURRU',u,origin);self.play(Transform(pre,back),Transform(suffix,VMobject(color=BLUE,stroke_width=6).set_points_as_corners(old[3:])),marker.animate.move_to(old[3]),Transform(status,label('Recovered crossing: up = right + 1',-2.8,RED,28)),run_time=1.8)
        self.at('a one to one pairing');self.note('Bad routes ↔ 4-right / 2-up routes',-4,GOLD)
        self.finish()
