import turtle

window = turtle.Screen()
window.bgcolor('red')

def draw_square(turtle, speed, size):
    turtle.speed(speed)
    for i in range(0,4):
        turtle.forward(size)
        turtle.right(90)

def draw_circle(turtle,size):
    turtle.shape('arrow')
    turtle.color('blue')
    turtle.circle(size)

def draw_triangle(turtle, speed, size):
    turtle.speed(speed)

    for i in range(0,3):
        turtle.forward(size)
        turtle.left(120)

def draw_circlesq(turtle, speed, size, step):
    for i in range(0, 360, 360//step):
        print(i)
        draw_square(turtle, 100, 50)
        turtle.right(360//step)

turt = turtle.Turtle()
draw_circlesq(turt, 5, 20, 6)

window.exitonclick()
