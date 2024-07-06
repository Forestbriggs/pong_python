from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_2_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.player_1_score, align=ALIGNMENT, font=FONT) 

        
    def player_1_point(self):
        self.player_1_score += 1
        self.update_scoreboard()
        
    def player_2_point(self):
        self.player_2_score += 1
        self.update_scoreboard()