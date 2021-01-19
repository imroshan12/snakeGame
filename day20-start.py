import turtle, random, time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
from gameover import GameOver


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.15)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.newSegment()
        food.refresh()
        scoreBoard.update()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        GameOver()
        gameIsOn = False

    for segement in snake.snakeBody:
        if segement == snake.head:
            pass
        elif snake.head.distance(segement) < 10:
            gameIsOn = False
            GameOver()










screen.exitonclick()
