import turtle
screen = turtle.Screen()
t = turtle.Turtle()
class letters():	
		def a(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(45)
			x.fd(50)
			x.lt(-90)
			x.fd(50)
			x.back(15)
			x.setheading(180)
			x.fd(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def b(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(0)
			x.circle(10,180)
			x.setheading(0)
			x.circle(10,180)
			x.rt(270)
			x.fd(40)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def c(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(180)
			x.circle(-20,180)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def d(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(0)
			x.circle(20,180)
			x.rt(270)
			x.fd(40)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def e(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(90)
			x.fd(50)
			x.rt(90)
			x.fd(25)
			x.back(25)
			x.lt(270)
			x.fd(25)
			x.lt(90)
			x.fd(20)
			x.back(20)
			x.rt(90)
			x.fd(25)
			x.lt(90)
			x.fd(25)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def f(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(0)
			x.fd(25)
			x.back(25)
			x.rt(90)
			x.fd(50)
			x.back(25)
			x.lt(90)
			x.fd(20)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def g(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(180)
			x.circle(20,180)
			x.lt(90)
			x.fd(30)
			x.lt(90)
			x.fd(30)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def h(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(90)
			x.fd(50)
			x.back(25)
			x.lt(90)
			x.fd(25)
			x.rt(90)
			x.fd(25)
			x.back(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def i(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(90)
			x.fd(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def j(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(-90)
			x.fd(40)
			x.circle(-12.5,180)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def k(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(-90)
			x.fd(50)
			x.back(25)
			x.lt(45)
			x.fd(30)
			x.back(30)
			x.lt(90)
			x.fd(30)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def l(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(-90)
			x.fd(50)
			x.lt(90)
			x.fd(30)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def m(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(0)
			x.fd(50)
			x.back(50)
			x.lt(45)
			x.fd(20)
			x.lt(90)
			x.fd(20)
			x.lt(45)
			x.fd(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def n(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(0)
			x.fd(50)
			x.back(50)
			x.lt(45)
			x.fd(65)
			x.lt(315)
			x.fd(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def o(x):
			xx = x.xcor();yy = x.ycor()
			x.circle(20,360)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def p(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(0)
			x.fd(50)
			x.back(10)
			x.circle(20,180)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def q(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(-90)
			x.circle(20,270)
			x.rt(90)
			x.fd(10)
			x.back(20)
			x.penup();x.setx(xx+75);x.sety(y);x.pendown()
		def r(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(90)
			x.circle(10,180)
			x.rt(45)
			x.fd(30)
			x.back(30)
			x.rt(45)
			x.fd(25)
			x.back(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def s(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(90)
			x.circle(10,180)
			x.circle(10,-180)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def t(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(90)
			x.fd(25)
			x.back(50)
			x.fd(25)
			x.rt(90)
			x.fd(75)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def u(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(-90)
			x.circle(20,180)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def v(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(45)
			x.fd(20)
			x.lt(90)
			x.fd(20)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def w(x):
			xx = x.xcor();yy = x.ycor()
			x.setheadingr(45)
			x.fd(50)
			x.lt(45)
			x.fd(50)
			x.rt(45)
			x.fd(50)
			x.lt(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def x(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(45)
			x.fd(50)
			x.back(25)
			x.rt(90)
			x.fd(50)
			x.back(x)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def y(x):
			xx = x.xcor();yy = x.ycor()
			x.setheading(45)
			x.fd(20)
			x.lt(90)
			x.fd(20)
			x.back(20)
			x.rt(45)
			x.fd(35)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		def z(x):
			xx = x.xcor();yy = x.ycor()
			x.setheadingr(90)
			x.fd(50)
			x.rt(135)
			x.fd(55)
			x.lt(135)
			x.fd(50)
			x.penup();x.setx(xx+75);x.sety(yy);x.pendown()
		
		
		
		'''
		games that use python
		battlefield 20eve online with stackless python
		
		frets on fire
		'''
# we can use Turtle.to write text or write it out by hand
#turtle.write("Hello world" ,font=("Arial",32,"normal"))

#t.letter(letters.a(t.t))
t.speed(0)
#letters.a(t.t)
letters.a(t)
letters.b(t)
letters.c(t)
letters.d(t)
letters.e(t)
letters.f(t)
letters.g(t)
letters.i(t)
letters.j(t)
letters.k(t)
letters.l(t)
letters.m(t)
