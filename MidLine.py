from turtle import Turtle

class MidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_line()

    def draw_line(self):
        self.shape("square")
        self.color("black")
        self.penup()
        self.goto(0, -315)
        self.resizemode("user")
        self.shapesize(stretch_wid=0.2, stretch_len=2)
        self.setheading(90)


        while self.ycor()<300:
            self.stamp()
            self.penup()
            self.forward(60)

