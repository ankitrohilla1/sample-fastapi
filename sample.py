
import turtle

#M
t = turtle.Turtle()
# t.bgcolor("black")
t.penup()
# draw straight line
t.goto(-100, 250)  # centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("red")
t.right(90)
t.forward(150)
t.goto(-100, 250)
t.goto(-50, 180)
t.goto(-5, 250)
t.goto(-5, 100)


#Y
t = turtle.Turtle()
t.penup()
t.goto(50,250)
t.pendown()
t.pensize(10)
t.pencolor("yellow")
t.right(65)
t.forward(90)
t.left(130)
t.forward(90)
t.penup()
t.goto(88, 170)
t.left(25)
t.pendown()
t.backward(80)



#C
t = turtle.Turtle()
t.penup()
t.goto(-200,-20)
t.pendown()
t.pensize(10)
t.pencolor("cyan")
t.right(180)
t.circle(50,180)


#U
t.penup()
t.goto(-150,-20)
t.pendown()
t.pencolor("green")
t.right(90)
t.forward(50)
t.circle(50,180,100)
t.forward(50)


#T
t = turtle.Turtle()
t.penup()
t.goto(-25,-20)
t.pendown()
t.pensize(10)
t.pencolor("pink")
t.forward(100)
t.goto(30,-20)
t.right(90)
t.forward(100)


#U
t = turtle.Turtle()
t.penup()
t.goto(100,-20)
t.pendown()
t.pensize(10)
t.pencolor("orange")
t.right(90)
t.forward(50)
t.circle(50,180,100)
t.forward(50)
# #




pen = turtle.Turtle()
pen.penup()
pen.goto(40,-200)
pen.pendown()


#heart
pen.fillcolor('red')
pen.begin_fill()
pen.left(140)
pen.forward(300)

for i in range(200):
    pen.right(1)
    pen.forward(2.1)

pen.left(135)

for i in range(200):
    pen.right(1)
    pen.forward(2.1)

pen.forward(280)
pen.end_fill()


#write in heart
pen.up()
pen.setpos(-100, 30)
pen.down()
pen.color('white')
pen.write("JASVEER", font=(
    "Palatino Linotype", 34, "bold"))



#left
u = turtle.Turtle()
u.showturtle()
u.up()
u.setpos(-520, 220)
u.down()
u.color('blue')
u.write("MERA SWEETUU SA", font=(
    "Harrington", 20, "bold"), move=True)


#right
u = turtle.Turtle()
u.showturtle()
u.up()
u.setpos(300, 220)
u.down()
u.color('blue')
u.write("MERA PYARAA SA", font=(
    "Harrington", 20, "bold"), move=True)
window:object = turtle.Screen()
window.exitonclick()