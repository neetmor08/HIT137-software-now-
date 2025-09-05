import turtle

def setup_turtle(side_length):
    """Setup turtle position and speed for drawing."""
    turtle.speed(0)  # fastest
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-side_length, side_length/2)  # starting position
    turtle.pendown()

if __name__ == "__main__":
    print("setup_turtle helper implemented ")
