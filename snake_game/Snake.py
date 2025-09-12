from turtle import Turtle
class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for positions in self.starting_position:
            s = Turtle()
            s.penup()
            s.shape("square")
            s.color("white")
            s.goto(positions)
            self.squares.append(s)

    def check_edges(self):
        x = self.squares[0].xcor()
        y = self.squares[0].ycor()
        return x > 290 or x < -290 or y > 290 or y < -290

    def check_tail(self):
        for segment in self.squares[6:]:
            if self.squares[0].distance(segment) < 15:
                return True


    def move(self):
        if self.check_edges() or self.check_tail():
            for segment in self.squares:
                segment.goto((1000,1000))
            return True
            # cursor = Turtle()
            # cursor.hideturtle()
            # cursor.color("White")
            # cursor.write("GAME OVER", font=("Arial", 20, "bold"), align="center")
            # return True

        for seg_num in range(len(self.squares) - 1, 0, -1):
            self.squares[seg_num].goto(self.squares[seg_num - 1].pos())
        self.squares[0].forward(20)
        return None

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(self.squares[len(self.squares) - 1].pos())
        self.squares.append(new_segment)

    def snake_up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)

    def snake_down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)

    def snake_left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)

    def snake_right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)