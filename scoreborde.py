from turtle import Turtle
class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.higher_score=0
        self.update_score()
    def add_score(self):
        self.count+=1
        self.clear()
        self.update_score()
    def update_score(self):
        self.goto(-130,260)
        self.write(f"score : {self.count}", align='center', font=('Arial', 24, 'normal'))
        with open("data.txt") as file:
            self.higher_score = int(file.read())
        self.goto(130,260)
        self.write(f"high score : {self.higher_score}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        if self.count>self.higher_score:
            self.higher_score=self.count
            with open("data.txt","w") as file:
                file.write(str(self.higher_score))
        self.goto(0,0)
        self.write("Game Over", align='center', font=('Arial', 24, 'normal'))
