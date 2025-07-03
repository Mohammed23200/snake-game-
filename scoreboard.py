from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score_board()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

