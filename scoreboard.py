from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, 270)
        self.pencolor("white")
        self.ht()
        self.count = 0
        self.update()

    def update(self):
        self.write(f"Score: {self.count}", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.count += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over! ", align=ALIGNMENT, font=FONT)


