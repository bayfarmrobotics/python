import turtle
window = turtle.Screen()
window.bgcolor('lightblue')

alex = turtle.Turtle()
alex.shape('turtle')
alex.color('green')

uuu = turtle.Turtle()
uuu.shape('arrow')
uuu.color('darkblue')

size = 0.001
for _ in range(85):
    alex.stamp()
    size = size + 3
    alex.forward(size)
    alex.right(24)

    uuu.stamp()
    uuu.forward(size*2)
    uuu.right(48)

window.mainloop() 