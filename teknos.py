import turtle
from turtle import *
from typing import ClassVar

print('hello')

s = getscreen()
t=  Turtle()


def fd(x):
    t.fd(x)
def e(x): 
    t.fd(x)

def bk(x):
    t.bk(x)
def h():
    t.bk(x)

def lt(x):
    t.lt(x)
def b(x):
    t.lt(x)

def rt(x):
    t.rt(x)
def j(x):
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
def hatterszin(s):
    turtle.bgcolor(s)

def title(s):
    turtle.title(s)

def pensize(x):
    t.pensize(x)
def tollvastagsag(x):
    t.pensize(x)

def fillcolor(szin):
    t.fillcolor(szin)
def toltoszin(szin):
    t.fillcolor(szin)

def pencolor(szin):
    t.pencolor(szin)
def tollszin(szin):
    t.pencolor(szin)

def begin_fill():
    t.begin_fill()

def end_fill():
    t.end_fill()

def koriv(i,r, sz):
    c = 2*3.14159/360
    for j in range(sz):
        fd(r*c) 
        lt(i)


def tracer(x,y):
    turtle.tracer(x, y)

def update():
    turtle.update()



def varj():
    input('nyomj egy entert a folytatáshoz')
def wait():
    input('nyomj egy entert a folytatáshoz')

def ht():
    turtle.ht()


class debug:
    def __init__(self, b=True):
        self.d = b

    def __enter__(self):
        if not self.d:
            tracer(0,0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.d:
            update()


class tollat:
    def __init__(self, hova):
        self.le = hova

    def __enter__(self):
        if not self.le:
            t.penup()
        else:
            t.pendown()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.le:
            t.pendown()
        else:
            t.penup()


class fordul:
    def __init__(self, mennyit):
        self.mennyit = mennyit

    def __enter__(self):
        t.lt(self.mennyit)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t.rt(self.mennyit)



class megy:
    def __init__(self, mennyit):
        self.mennyit = mennyit

    def __enter__(self):
        t.fd(self.mennyit)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t.bk(self.mennyit)
