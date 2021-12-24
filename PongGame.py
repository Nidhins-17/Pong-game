import turtle as t

playerAscore = 0
playerBscore = 0

# creating a window
window = t.Screen()
window.title("Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)


# creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# creating right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# creating ball
ball = t.Turtle()
ball.speed(100)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0.2
ballydirection = 0.2

# creating pen
pen = t.Turtle()
pen.speed(9)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))

# functionalities for the paddles


def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    if y >= 300:
        leftpaddle.sety(300)
    else:
        leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y = y-90
    if y <= -300:
        leftpaddle.sety(-300)
    else:
        leftpaddle.sety(y)


def rightpaddleup():
    y = rightpaddle.ycor()
    y = y+90
    if y >= 300:
        rightpaddle.sety(300)
    else:
        rightpaddle.sety(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y = y-90
    if y <= -300:
        rightpaddle.sety(-300)
    else:
        rightpaddle.sety(y)


# assigning keys for the movement of the paddles
window.listen()
window.onkeypress(leftpaddleup, 'a')
window.onkeypress(leftpaddledown, 'z')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# response of ball to the boundaries
while True:
    window.update()
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection*-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection*-1
    if ball.xcor() > 390:
        ballxdirection = ballxdirection*-1
        playerAscore = playerAscore+1
        pen.clear()
        pen.write("player A:{} player B:{}".format(playerAscore,
                  playerBscore), align='center', font=('Arial', 24, 'normal'))
    if(ball.xcor()) < -390:
        ballxdirection = ballxdirection*-1
        playerBscore = playerBscore+1
        pen.clear()
        pen.write("player A:{} player B:{}".format(playerAscore,
                  playerBscore), align='center', font=('Arial', 24, 'normal'))

# handling the collisions of ball and the paddle
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor()+40 and ball.ycor() > rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection = ballxdirection*-1
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor()+40 and ball.ycor() > leftpaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection = ballxdirection*-1

# winner in the match
    if playerAscore >= 1:
        ballxdirection = 0
        ballydirection = 0
        ball.goto(0, 0)
        pen.clear()
        pen.write('player A has won the match!!!',
                  align='center', font=('Arial', 24, 'normal'))

    if playerBscore >= 1:
        ballxdirection = 0
        ballydirection = 0
        ball.goto(0, 0)
        pen.clear()
        pen.write('player B has won the match!!!',
                  align='center', font=('Arial', 24, 'normal'))
