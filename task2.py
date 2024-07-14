import turtle
import sys

window = turtle.Screen()
window.bgcolor("white")
snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.color("blue")



def koch_snowflake(length, level):
    if level == 0:
        snowflake.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, level - 1)
        snowflake.left(60)
        koch_snowflake(length, level - 1)
        snowflake.right(120)
        koch_snowflake(length, level - 1)
        snowflake.left(60)
        koch_snowflake(length, level - 1)



def draw_koch_snowflake(x, y, length, level):
    snowflake.penup()
    snowflake.goto(x, y)
    snowflake.pendown()
    snowflake.penup()
    snowflake.goto(x - length/2, y + length/3.0)
    snowflake.pendown()
    for _ in range(3):
        koch_snowflake(length, level)
        snowflake.right(120)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python3 task2.py <рівень_рекурсії>")
        sys.exit(1)

    level = int(sys.argv[1])
    length = 300.0 

    draw_koch_snowflake(-100, 0, length, level)

    snowflake.hideturtle()
    turtle.done()
