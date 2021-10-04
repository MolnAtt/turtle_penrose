import turtle
from turtle import *
from typing import ClassVar

print('hello')

s = getscreen()
t=  Turtle()

def fd(x):
    t.fd(x)

def bk(x):
    t.bk(x)

def lt(x):
    t.lt(x)

def rt(x):
    t.rt(x)

def goto(x,y):
    t.goto(x,y)

def home():
    t.home()

def circle(x):
    t.circle(x)

def dot(x):
    t.dot(x)

def bgcolor(s):
    turtle.bgcolor(s)

def title(s):
    turtle.title(s)

def pensize(x):
    t.pensize(x)

def fillcolor(szin):
    t.fillcolor(szin)

def pencolor(szin):
    t.pencolor(szin)

def pensize(x):
    t.pensize(x)

def begin_fill():
    t.begin_fill()

def end_fill():
    t.end_fill()



def tracer(x,y):
    turtle.tracer(x, y)

def update():
    turtle.update()


def wait():
    input('nyomj egy entert hogy bezáródjon az ablak')

def ht():
    turtle.ht()


class debug:
    def __init__(self, b=True):
        self.d = b

    def __enter__(self):
        if self.d:
            tracer(0,0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.d:
            update()