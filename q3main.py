import turtle
from draw_polygon import draw_polygon
from turtle_setup import setup_turtle

def main():
    # User inputs
    sides = int(input("Enter the number of sides: "))
    side_length = int(input("Enter the side length (pixels): "))
    depth = int(input("Enter recursion depth: "))

    # Setup and draw
    setup_turtle(side_length)
    draw_polygon(sides, side_length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
