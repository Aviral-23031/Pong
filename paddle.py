from turtle import Turtle
MOVING_DISTANCE = 40
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.create_paddle(position)

    def create_paddle(self,position):
        self.shape("square")
        self.color("grey10")
        self.goto(position)
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def move_up(self):
        # self.setheading(UP)
        self.speed("fastest")
        # self.forward(MOVING_DISTANCE)
        if self.ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)


    def move_down(self):
        # self.setheading(DOWN)
        self.speed("fastest")
        # self.forward(MOVING_DISTANCE)
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)

