from time import sleep
from turtle import Screen, down, update, ycor
from bot import Bot
from paddle import Paddle
from player import Player
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('#1F1F1F')
screen.title('Pong')
screen.tracer(0)

# player = Player()
# bot = Bot()
player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player_1.go_up, 'Up')
screen.onkey(player_1.go_down, 'Down')
screen.onkey(player_2.go_up, 'w')
screen.onkey(player_2.go_down, 's')

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect if ball hit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with player_1 or player_2
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or \
        ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect if player_1 misses
    if ball.xcor() > 380:
        scoreboard.player_2_point()
        ball.reset()
        
    # Detect if player_2 misses
    if ball.xcor() < -380:
        scoreboard.player_1_point()
        ball.reset()

screen.exitonclick()