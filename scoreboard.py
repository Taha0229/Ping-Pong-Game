import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        # self.increase = 10

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 70, "normal"))

    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()
        # self.increase += 5

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()
        # self.increase += 5


