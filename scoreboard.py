from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.color("white")
        self.update_score_board()
    def update_score_board(self):
        self.write(f"score: {self.score}",align="center",font=('Arial',24,'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score_board()
