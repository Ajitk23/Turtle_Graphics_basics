from turtle import Turtle, Screen

jinny = Turtle()
jinny.shape("turtle")
jinny.color("red", "yellow")


for _ in range(4):
    jinny.forward(100)
    jinny.right(90)



screen=Screen()
screen.exitonclick()