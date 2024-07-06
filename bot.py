from time import sleep
from player import Player

class Bot(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moving_up = True
        self.speed('normal')
        self.goto(-370, 0)
        
    def move(self):
        if self.moving_up:
            if self.ycor() < 250:
                self.goto(self.xcor(), self.ycor() + 20)
            else:
                self.moving_up = False
                self.goto(self.xcor(), self.ycor() - 20)
        else:
            if self.ycor() > -250:
                self.goto(self.xcor(), self.ycor() - 20)
            else:
                self.moving_up = True
                self.forward(20)