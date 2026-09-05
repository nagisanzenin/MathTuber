from scenes._shared.design import *

class Shot3(Stage):
    sid="s03"
    def construct(self):
        self.title('FOUR SEEDS ARE ENOUGH')
        rows=[order_row(18,[7,7,4],2.5),order_row(19,[7,4,4,4],1.1),order_row(20,[4]*5,-.3),order_row(21,[7]*3,-1.7)]
        self.at('Eighteen is');self.show(rows[0])
        self.at('Nineteen is');self.show(rows[1])
        self.at('Twenty is');self.show(rows[2])
        self.at('Twenty one is');self.show(rows[3])
        self.at('Four consecutive numbers');self.play(LaggedStart(*[Indicate(r[0],color=GREEN) for r in rows],lag_ratio=.2),run_time=1.4)
        self.at('add another box of four');self.note('Every success can produce +4.',-3.4,GREEN)
        self.finish()
