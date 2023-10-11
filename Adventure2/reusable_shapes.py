import turtle

def drawShape(sides, length):
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)

def moveTurtle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def drawSquare(length):
    drawShape(4, length)


def drawTriangle(length):
    drawShape(3, length)


def drawCircle(length):
    drawShape(360, length)



turtle.fillcolor("red")
turtle.begin_fill()
drawCircle(4)
turtle.end_fill()

moveTurtle(0,0)

turtle.fillcolor("orange")
turtle.begin_fill()
drawCircle(3)
turtle.end_fill()

moveTurtle(0,0)
turtle.fillcolor("yellow")
turtle.begin_fill()        
drawCircle(2)
turtle.end_fill()

moveTurtle(0,0)
turtle.fillcolor("green")
turtle.begin_fill()        
drawCircle(1)
turtle.end_fill()

moveTurtle(0,0)
turtle.fillcolor("blue")
turtle.begin_fill()        
drawCircle(0.5)
turtle.end_fill()




turtle.done()

