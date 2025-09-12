from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_data.txt","r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {str(self.score)} High Score : {self.high_score}", align = 'center', font = ('Arial',14,'bold'))

    def reset_score(self):
        if self.score > self.high_score:
             self.high_score = self.score
        with open("score_data.txt","w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()


