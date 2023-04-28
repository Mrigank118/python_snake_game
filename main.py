from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.down , "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.Up, "Up")
# Creating a Snake Body

segments = []

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        snake.extend()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    #detect collision with tail

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10 :
            game_is_on = False
            score.game_over()




screen.exitonclick()