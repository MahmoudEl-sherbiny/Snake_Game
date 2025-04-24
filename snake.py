from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def create_framework(self):
        border = Turtle()
        border.speed(0)
        border.pensize(10)
        border.color("white")
        border.penup()
        border.goto(-305, 305)  # Adjust these coordinates to change the framework size
        border.pendown()
        for _ in range(2):
            border.forward(605)  # Adjust the length to change the framework size
            border.right(90)
            border.forward(605)
            border.right(90)

        border.hideturtle()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self, amount):
        for i in range(amount):
            self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def pass_from_walls(self):
        if self.head.ycor() > 295:
            self.head.goto(self.head.xcor(), -295)
        elif self.head.ycor() < -295:
            self.head.goto(self.head.xcor(), 295)
        elif self.head.xcor() > 295:
            self.head.goto(-295, self.head.ycor())
        elif self.head.xcor() < -295:
            self.head.goto(295, self.head.ycor())
