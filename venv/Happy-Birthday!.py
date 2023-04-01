#A lovely birthday message from ChatGPT :)

import turtle

# create turtle
t = turtle.Turtle()

# set turtle speed
t.speed(0)

# set up cake
def draw_cake():
    # draw base
    t.penup()
    t.goto(-150, -50)
    t.pendown()
    t.begin_fill()
    t.color("#F5DEB3")
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()

    # draw frosting
    t.penup()
    t.goto(-100, 150)
    t.pendown()
    t.begin_fill()
    t.color("#F5F5F5")
    t.circle(100)
    t.end_fill()

    # draw candles
    t.penup()
    t.goto(-100, 200)
    t.pendown()
    t.color("yellow")
    for i in range(4):
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(40)
        t.right(180)
        t.forward(40)
        t.right(90)
    t.penup()
    t.goto(-100, 250)
    t.pendown()
    t.color("red")
    for i in range(4):
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(40)
        t.right(180)
        t.forward(40)
        t.right(90)

# set up message
def draw_message():
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.color("blue")
    t.write("Happy 40th Birthday Wolfgang!", align="center", font=("Arial", 24, "bold"))

# set up animation
def flicker(candle):
    candle.pensize(3)
    for i in range(10):
        candle.color("yellow")
        candle.fd(2)
        candle.color("red")
        candle.fd(2)

# draw cake and message
draw_cake()
draw_message()

# light candles
candle1 = turtle.Turtle()
candle1.speed(0)
candle1.penup()
candle1.goto(-25, 290)
candle1.pendown()
flicker(candle1)

candle2 = turtle.Turtle()
candle2.speed(0)
candle2.penup()
candle2.goto(25, 290)
candle2.pendown()
flicker(candle2)

# start animation
while True:
    for angle in range(0, 360, 10):
        candle1.setheading(angle)
        candle2.setheading(angle)