import turtle

# The turtle starts at the default center (0, 0)
print(f"Initial X position: {turtle.xcor()}")
print(f"Initial Y position: {turtle.ycor()}")

# Draw a dot right where it starts
turtle.dot(10, "blue")

# Draw lines to the edges so you can visualize the center
turtle.speed(3)
turtle.penup()
turtle.goto(turtle.window_width() / 2, 0)
turtle.pendown()
turtle.goto(turtle.window_width() / -2, 0)
turtle.penup()
turtle.goto(0, turtle.window_height() / 2)
turtle.pendown()
turtle.goto(0, turtle.window_height() / -2)

print(turtle.window_height())
print(turtle.window_width())

turtle.exitonclick()