from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from users
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and promp for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color= input("Enter canvas color (white or black):")

# Create a canvas with user input
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quite to quite.")
    # Ask for rectangle input and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle:"))
        rec_y = int(input("Enter y of the rectangle:"))
        rec_width = int(input("Enter width of the rectangle:"))
        rec_height = int(input("Enter height of the rectangle:"))
        red = int(input("Level of red color:"))
        green = int(input("Level of green: "))
        blue = int(input("Level of blue: "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square user input if user entered "square
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square:"))
        sqr_y = int(input("Enter y of the square:"))
        sqr_width = int(input("Enter width of the square:"))
        sqr_height = int(input("Enter height of the square:"))
        red = int(input("Level of red color:"))
        green = int(input("Level of green: "))
        blue = int(input("Level of blue: "))
        s1 = Rectangle(x=sqr_x, y=sqr_y, height=sqr_height, width=sqr_width, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == "quite":
        break

canvas.make('canvas.png')

