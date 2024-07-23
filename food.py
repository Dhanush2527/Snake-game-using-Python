from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')


    def rearrange_food(self):
        go_x = random.randint(-288, 280)
        go_y = random.randint(-280, 280)
        self.goto(go_x, go_y)


