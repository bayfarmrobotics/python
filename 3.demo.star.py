import turtle
window = turtle.Screen()
window.bgcolor("darkblue")
window.title("!")

turtl =turtle.Turtle ()
turtl.color("yellow")
turtl.pensize(5)

turtl.left(144)

for _ in range(5):
    turtl.forward(300)
    turtl.right(144)

window.mainloop()