import turtle

def draw_edge(length, depth):
    """Recursively draw one edge with Koch-like indentation."""
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)
        turtle.left(120)
        draw_edge(length, depth - 1)
        turtle.right(60)
        draw_edge(length, depth - 1)

if __name__ == "__main__":
    print("draw_edge function implemented ")
