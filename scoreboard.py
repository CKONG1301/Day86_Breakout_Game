from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.score = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, -200)
        self.write(f'Balls: {self.score}', align="center", font=('Arial', 30, "normal"))

    def decrease_score(self):
        self.score -= 1
        self.update_scoreboard()

    def gameover(self):
        self.clear()
        self.goto(0, -150)
        self.write('GAME OVER', align="center", font=('Arial', 80, "normal"))

    def win(self):
        self.clear()
        self.goto(0, -150)
        self.write('YOU WIN!', align="center", font=('Arial', 80, "normal"))