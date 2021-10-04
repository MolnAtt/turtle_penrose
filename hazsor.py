from teknos import *
import time

from math import sqrt, sin, radians

fel = False
le = True


hatterszin('black')
tollszin('white')
tollvastagsag(1)

b(90)

def tegla(a,b):
    for d in range(2):
        e(a)
        j(90)
        e(b)
        j(90)


def o(x):
    with fordul(-90):
        e(x)

def haromszog(a):
    with fordul(-30):
        for sz in range(3):
            e(a)
            j(120) 


def valasztohaz(x,k):
    for sz in range(2):
        tegla(2*x,x)
        o(x)
    tegla(4*x, 4*x)
    with megy(4*x):
        haromszog(4*x)
    if (k):
        o(x)
        e(2*x)
        koriv(-1, x, 180)
        e(2*x)
        b(180)
        o(x)
    else:
        o(4*x)
    for sz in range(2):
        tegla(2*x,x)
        o(x)

def haz(x):
    valasztohaz(x, False)

def kapushaz(x):
    valasztohaz(x, True)

def hazsor(db, x):
    villogo = False
    for sz in range(db):
        valasztohaz(x, villogo)
        villogo = not villogo


with debug(False):
    with tollat(fel):
        o(-500)
    hazsor(4,30)




wait()