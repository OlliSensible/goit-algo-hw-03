import turtle

def draw_colored_line(length, color, width):
    turtle.pencolor(color)
    turtle.pensize(width)
    if length < 5:
        turtle.forward(length)
    else:
        new_length = length / 3.0
        draw_colored_line(new_length, color, width)
        turtle.left(60)
        draw_colored_line(new_length, color, width)
        turtle.right(120)
        draw_colored_line(new_length, color, width)
        turtle.left(60)
        draw_colored_line(new_length, color, width)

def koch_snowflake(level, length, color, width):
    for _ in range(3):
        draw_colored_line(length, color, width)
        turtle.right(120)
    turtle.hideturtle()

try:
    level = int(input("Введіть рівень рекурсії (додатне ціле число): "))
    if level < 0:
        raise ValueError()
    if not isinstance(level, int):
        raise ValueError()
except ValueError:
    print("Будь ласка, введіть додатне ціле число.")
    exit()
    

turtle.bgcolor("#192a32") 
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.shape("turtle") 

koch_snowflake(level, 400, "pink", 2) 

turtle.done()