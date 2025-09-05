import turtle
from draw_edge import draw_edge

def draw_polygon(sides, side_length, depth):
    """Draw the full polygon applying recursive edges."""
    for _ in range(sides):
        draw_edge(side_length, depth)
        turtle.right(360 / sides)

if __name__ == "__main__":
    print("draw_polygon function implemented ")
