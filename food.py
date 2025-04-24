from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.default_shape()
        self.penup()
        self.speed()
        self.refresh()

    def default_shape(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        #self.default_shape()

    def spawn_big_meal(self):
        self.shape("square")  # Big meal is a square
        self.color("gold")
        self.refresh()

