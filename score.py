from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = (int(data.read()))
        self.penup()
        self.color("white")
        self.goto(0, 270)

        self.write(f"score:{self.score}   high score{self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}   highscore:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("game over!", align=ALIGNMENT, font=FONT)
