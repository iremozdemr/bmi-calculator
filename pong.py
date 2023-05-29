import turtle

wn = turtle.Screen()
wn.title("pong by irem")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_a_score = 0
paddle_b_score = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(1,1)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player a: " + str(paddle_a_score) + " player b: " + str(paddle_b_score),align="center",font=("Courier",24,"normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(quit,"q")

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.goto(0,0)
        #ball.setx(390)
        ball.dx *= -1
    if ball.xcor()<-390:
        ball.goto(0,0)
        #ball.setx(-390)
        ball.dx *= -1

    if paddle_a.ycor()-50<ball.ycor()<paddle_a.ycor()+50:
        if paddle_a.xcor()+20 == ball.xcor():
            ball.dx *= -1
            paddle_a_score+=1
    
    if paddle_b.ycor()-50<ball.ycor()<paddle_b.ycor()+50:
        if paddle_b.xcor()-20 == ball.xcor():
            ball.dx *= -1
            paddle_b_score+=1
    
    if ball.xcor()>380:
        ball.dx *= -1
        paddle_a_score+=1
    
    if ball.xcor()<-380:
        ball.dx *= -1
        paddle_b_score+=1

    pen.clear()
    pen.write("player a: " + str(paddle_a_score) + " player b: " + str(paddle_b_score),align="center",font=("Courier",24,"normal"))