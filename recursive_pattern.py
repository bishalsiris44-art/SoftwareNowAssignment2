import turtle
# Import the turtle module to draw graphics on the screen

# Recursive function to draw a modified edge

def draw_edge(length, depth):
    """
    This recursive function draws a single edge of the pattern.
    -If depth is 0, it simply draws a straight line.
    - If depth is greater than 0, the edge is divided into 
    three equal parts and the middle part is replaced 
    by the two sides of an inward equilateral triangle.
    """

    #Base case: when recursion depth reaches 0

    if depth == 0:
        turtle.forward(length)
    else:
        # Reduce the length of the segment to one-third
        length /= 3

        # First segment
        draw_edge(length, depth - 1)

        # Indentation inward
        turtle.right(60)
        draw_edge(length, depth - 1)

        turtle.left(120)
        draw_edge(length, depth - 1)

        turtle.right(60)
        draw_edge(length, depth - 1)


# Main program

def main():
    # This function handles user input, turtle setup, and drawing the complete polygon using recursion.


    # User input
    sides = int(input("Enter the number of sides: ")) #Number of polygon sides
    side_length = int(input("Enter the side length: ")) # Length of each sides
    depth = int(input("Enter the recursion depth: ")) # Level of recursion

    # Turtle setup
    turtle.speed(0) # set maximum darwing speed
    turtle.hideturtle() # Hide the turtol cursor
    turtle.penup() #Lift the pen to move without drawing
    turtle.goto(-side_length / 2, side_length / 2) #Position turtle
    turtle.pendown() #Start drawing

    # Draw the polygon
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(side_length, depth)
        turtle.right(angle)

    turtle.done()



# Program entry point
if __name__ == "__main__":
    main()