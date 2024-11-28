
# -------------------------------------------------------------------------- ping pong game by Ahmed Ghallab----------------------------------------------------------------------------------------

import turtle

# set up the screen
window = turtle.Screen()
window.title("Ping Pong Game By Ahmed Ghallab")
window.setup(width=800, height=600)
window.tracer(0)  # set delay for update drawings
window.bgcolor(.1, .1, .1)

# set up objects
ball = turtle.Turtle()
ball.shape("square")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.speed(0)
ball.penup()
ball.color("white")
ball.goto(x=0, y=0)
ball_dx, ball_dy = 1, 1
ball_speed = 0.14

# create line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.penup()
line.shapesize(stretch_wid=20, stretch_len=0.1)
line.goto(0, 0)

# player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("red")
player1.penup()
player1.goto(-350, 0)

# player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("blue")
player2.penup()
player2.goto(350, 0)

# score text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))
score.hideturtle()

p1_score, p2_score = 0, 0
player_speed = 20

# player movement
def player1_up():
    player1.sety(player1.ycor() + player_speed)

def player1_down():
    player1.sety(player1.ycor() - player_speed)

def player2_up():
    player2.sety(player2.ycor() + player_speed)

def player2_down():
    player2.sety(player2.ycor() - player_speed)


# keyboard binding
# keyboard binding
window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")

# game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball_speed * ball_dx)
    ball.sety(ball.ycor() + ball_speed * ball_dy)

    # ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1

    # collision with player 1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (player1.ycor() + 50) and ball.ycor() > (player1.ycor() - 50)):
        ball.setx(-340)
        ball_dx *= -1

    # collision with player 2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (player2.ycor() + 50) and ball.ycor() > (player2.ycor() - 50)):
        ball.setx(340)
        ball_dx *= -1

    # scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        p1_score += 1
        score.clear()
        score.write(f"Player 1: {p1_score} Player 2: {p2_score}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        p2_score += 1
        score.clear()
        score.write(f"Player 1: {p1_score} Player 2: {p2_score}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        score.clear()
        p2_score += 1
        ball_dx *=-1    

        if(ball.xcor() > 390):
            ball.goto(0,0)
            ball_dx *= -1
        if(ball.xcor() > -390):
            ball.goto(0,0)
            ball_dx *= -1
            
# -------------------------------------------------------------------------- ping pong game by Ahmed Ghallab----------------------------------------------------------------------------------------
