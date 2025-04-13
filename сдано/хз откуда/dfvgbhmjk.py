from turtle import *
tracer(0)
m=10
left(90)
rt(315)
for i in range (7):
    fd(12*m)
    rt(45)
    fd(6*m)
    rt(135)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*m,y*m)
        dot(4)
done()