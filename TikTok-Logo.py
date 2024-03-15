from turtle import *

width(20)
bgcolor("black")

c = ["#db0f3c", "#50ebe7", "white"]
p = [(0,0),(-5,13),(-5,5)]
for (a,b), c in zip(p,c):
	up()
	goto(a,b)
	down()
	color (c)
	left(180)
	circle(50, 270)
	fd(120)
	lt(180)
	circle (50,90)
	
done()