from turtle import Turtle,Screen

X_POSITION = [12, 0, -12]
MOVE_DISTANCE = 20
UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((X_POSITION[i], 0))  # Pass position tuple

    def move(self):
        for square_num in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[square_num - 1].xcor()
            newY = self.segments[square_num - 1].ycor()
            self.segments[square_num].goto(x=newX, y=newY)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        # Add new segment at the last segment's position
        self.add_segment(self.segments[-1].position())