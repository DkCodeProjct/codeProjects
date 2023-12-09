import turtle
import random

#make screen
wn = turtle.Screen()
wn.title(">>_DK.GAMES_<<")
wn.bgcolor("black")
wn.setup(width=600,height=400)

#code box
box = turtle.Turtle()
box.shape('square')
box.color("blue")
box.shapesize(stretch_wid=1,stretch_len=5)
box.penup()
box.goto(0, -250)

score = 0

#moving func
def move_left():
    x = box.xcor()
    x -= 20
    box.setx(x)

def move_right():
    x = box.xcor()
    x += 20
    box.setx(x)

#keyBord binding
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")

#code circle
circle = turtle.Turtle()
circle.shape("circle")
circle.color("red")
circle.penup()
circle.speed(0)
circle.goto(random.randint(-290,290),250)

#mainGameLoop
while True:
    y = circle.ycor()
    y -= 2
    circle.sety(y)
    
    #failing cirle
    if (circle.ycor() < box.ycor() + 20 
        and circle.ycor() > box.ycor() - 20
        and circle.xcor() < box.xcor() + 50
        and circle.xcor() > box.xcor() - 50
):
        print("GameOver// Your score",score)
        break
    
    if circle.ycor() < -300:
        circle.goto(random.randint(-290,290),250)
        score += 1
        print("score",score)

wn.mainloop()
