from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.moving_up = True
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def go_up(self):
        if not self.moving_up:
            self.moving_up = True
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)
        
    def go_down(self):
        if self.moving_up:
            self.moving_up = False
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)