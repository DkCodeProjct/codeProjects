import turtle
import math
import time


scrn = turtle.Screen()
scrn.bgcolor('black')

line = turtle.Turtle()
line.speed(0)
line.color('red')
line.hideturtle()

xA, yA = 0, 0
lineLenght = 100
angle = 0
angularVelocity = 0
fraction = 0.98

def drawLine():
    line.clear()
    line.penup()
    line.goto(xA, yA)
    line.pendown()

    xB = xA + lineLenght * math.cos(math.radians(angle))
    yB = yA + lineLenght * math.sin(math.radians(angle))

    line.goto(xB, yB)


def rotate():
    global angle, angularVelocity

    while abs(angularVelocity) > 0.01:
        angle += angularVelocity
        angularVelocity *= fraction
        drawLine()
        time.sleep(0.02)
    angularVelocity = 0


def rotateRight():
    global angularVelocity  
    angularVelocity = -10
    rotate()

def rotateLeft():
    global angularVelocity
    angularVelocity = 10
    rotate()

drawLine()

scrn.listen()
scrn.onkey(rotateRight, 'Right')
scrn.onkey(rotateLeft, 'Left')
scrn.listen()

drawLine()

turtle.done()