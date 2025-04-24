from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("#17202a")
screen.title("My Snake Game")
screen.tracer(0)
difficult = screen.textinput(title="Difficulty",prompt="With Hurdle of wall OR with out (y/n):")


snake = Snake()
food = Food()
scoreboard = Scoreboard()

if difficult == "y":
    snake.create_framework()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # show me changes  (response of tracer(0))
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        if food.shape() == "square":
            scoreboard.increase_score(5)
            snake.extend(5)
            food.refresh()
        else:
            scoreboard.increase_score(1)
            snake.extend(1)

        if scoreboard.big_score(scoreboard.score):
             food.spawn_big_meal()
        else:
             food.default_shape()
             food.refresh()
    # Detect if you want walls or not.
    if difficult == "y":
        if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
            game_is_on = False
            scoreboard.game_over()
    else:
        snake.pass_from_walls()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
