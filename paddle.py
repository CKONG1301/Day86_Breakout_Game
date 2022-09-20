from turtle import Turtle

# turtle default size is 20x20
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # Create a paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=6)
        self.penup()
        self.goto(position)

    def right(self):
        new_x = self.xcor() + 30
        if new_x > 340:
            new_x = 340
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 30
        if new_x < -340:
            new_x = -340
        self.goto(new_x, self.ycor())
        
