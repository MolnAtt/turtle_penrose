from teknos import *
import time

from math import sqrt, sin, radians

fel = False
le = True


hatterszin('black')
tollszin('white')
tollvastagsag(1)

b(90)

def alap1(r):
    kor(r)
    with tollat(fel):
        o(0.25*r)
    kor(.8*r)


def alap3(r):
    alap1(r)

def alap2(r):
    kor(r)

def karkoto(sz, r):
    pass


def kor(r):
    koriv(1, r, 360)


def o(x):
    with fordul(-90):
        e(x)



with debug(False):
    alap1(50)
    with tollat(fel):
        pass



wait()