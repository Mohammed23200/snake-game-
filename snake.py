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
        self.head=self.segments[0]


    def create_snake(self):
        for i in range(3):
            new_square = Turtle(shape="square")
            
            new_square.penup()
            new_square.color("white")
            new_square.goto(x=X_POSITION[i], y=0)
            self.segments.append(new_square)

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
    
    