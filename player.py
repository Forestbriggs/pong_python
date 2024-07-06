from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.moving_up = True
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_len=1, stretch_wid=5)
        # self.setheading(90)
        self.penup()
        self.goto(350, 0)
        
    def up(self):
        if not self.moving_up:
            self.moving_up = True
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)
        
    def down(self):
        if self.moving_up:
            self.moving_up = False
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)