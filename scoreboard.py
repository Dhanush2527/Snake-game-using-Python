from turtle import Turtle
ALLIGN = 'center'
FONT = ('arial', 15, 'normal')
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score}   High score = {self.high_score}", False, align=ALLIGN, font=FONT)

    #def game_over(self):
        #self.goto(x=0, y=0)
        #self.write("GAME OVER", False, align=ALLIGN, font=FONT)


    def manage_score(self):
        self.score += 1
        self.update_scoreboard()