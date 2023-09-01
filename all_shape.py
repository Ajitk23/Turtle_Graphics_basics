import turtle as t
import random

hurry = t.Turtle()


colors = ["light sea green", "lime", "spring green", "green yellow", "red", "spring green", "wheat"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle= 360/num_sides
        hurry.forward(100)
        hurry.right(angle)
        
        
    
for shape_side_n in range(3, 11):
    hurry.shape("turtle")
    hurry.color(random.choice(colors))
    draw_shape(shape_side_n)