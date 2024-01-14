from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x = 0 , y = 270)
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1 
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x = 0 , y = 0)
        self.write("GAME OVER" , align= "center" , font= ("Arial" , 22 , "normal"))


    def update_scoreboard(self):
        self.write(f"score : {self.score}" , align= "center" , font= ("Arial" , 22 , "normal"))
        
    