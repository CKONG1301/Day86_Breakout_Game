import random
from turtle import Turtle

color_list = ['blue', 'brown', 'yellow', 'orange', 'white', 'red']


class Bricks(Turtle):
    def __init__(self):
        self.bricks = []
        self.size = 4
        self.add_brick((-360, 280), self.size)
        self.head = self.bricks[0]

    def add_brick(self, position, size):
        new_brick = Turtle('square')
        color1 = random.choice(color_list)
        new_brick.color(color1)
        new_brick.begin_fill()
        new_brick.size = size
        new_brick.shapesize(stretch_wid=2, stretch_len=size)
        new_brick.end_fill()
        new_brick.penup()
        new_brick.goto(position)
        self.bricks.append(new_brick)
    
    def extend(self, size):
        new_x = self.bricks[-1].xcor() + self.bricks[-1].size * 10 + size * 10 + 10
        new_y = self.bricks[-1].ycor()
        if new_x > 400:
            if size == 4:
                size = 3
                new_x = self.bricks[-1].xcor() + self.bricks[-1].size * 10 + size * 10 + 10
            else:
                new_y = self.bricks[-1].ycor() - 45
                new_x = size * 5 - 400
        if new_y >= 190:
            self.add_brick((new_x, new_y), size)
        return new_y >= 190
        