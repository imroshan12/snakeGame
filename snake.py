import turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_SHAPE = "circle"
class Snake:
    def __init__(self):
        self.snakeBody = []
        self.createSnake()
        self.head = self.snakeBody[0]

    def newSegment(self):
        newPart = turtle.Turtle(SNAKE_SHAPE)
        newPart.penup()
        lastX = self.snakeBody[-1].xcor()
        lastY = self.snakeBody[-1].ycor()
        newPart.goto(lastX, lastY)
        newPart.color("white")
        self.snakeBody.append(newPart)

    def createSnake(self):
        for i in range(3):
            newPart = turtle.Turtle(SNAKE_SHAPE)
            newPart.penup()
            newPart.goto(STARTING_POSITIONS[i])
            newPart.color("white")
            self.snakeBody.append(newPart)
    def move(self):
        for i in range(len(self.snakeBody) - 1, 0, -1):
            newX = self.snakeBody[i - 1].xcor()
            newY = self.snakeBody[i - 1].ycor()
            self.snakeBody[i].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

