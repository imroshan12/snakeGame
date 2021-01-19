from turtle import Turtle, Screen
from time import sleep

SCOREBOARD_POSITION = (0, 275)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(SCOREBOARD_POSITION)
        self.score = 0
        self.writeScore()

    def writeScore(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 12, "bold"))

    def update(self):
        self.score += 1
        self.clear()
        self.writeScore()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align="center", font=("Arial", 20, "bold"))
    #     self.color("red")

# score = ScoreBoard()
# for i in range(10):
#     score.update()
# Screen().setup(600,600)
# Screen().exitonclick()