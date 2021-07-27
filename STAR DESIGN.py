from turtle import *
import turtle
col = ('yellow', 'red', 'orange', 'blue', 'white')
t = turtle.turtle()
screen = turtle.screen()
screen.bgcolor('black')
t.speen(30)


for i in range (150):
    i.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
