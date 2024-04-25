import turtle
import argparse


def draw_koch_segment(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, depth - 1)
        t.left(60)
        draw_koch_segment(t, length, depth - 1)
        t.right(120)
        draw_koch_segment(t, length, depth - 1)
        t.left(60)
        draw_koch_segment(t, length, depth - 1)


def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        draw_koch_segment(t, length, depth)
        t.right(120)


def main():
    parser = argparse.ArgumentParser(description="Draw a Koch Snowflake fractal with specified recursion depth.")
    parser.add_argument("recursion_level", type=int, help="The recursion level of the Koch Snowflake")

    args = parser.parse_args()

    # Turtle setup
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Draw the Koch Snowflake
    draw_koch_snowflake(t, 300, args.recursion_level)

    # Finish up
    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    main()