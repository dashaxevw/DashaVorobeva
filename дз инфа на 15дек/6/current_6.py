from turtle import *
tracer(0)
m=20
left(90)
for i in range(2):
    fd(5+m)
    lt(90)
    backward(13*m)
    lt(90)
up()
backward(10*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(11*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*m,y*m)
        dot(4)
done()