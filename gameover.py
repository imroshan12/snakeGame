from turtle import Turtle
from time import sleep
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 20, "bold"))
# self.color("yellow")