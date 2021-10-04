from teknos import *
import time

from math import sqrt, sin, radians

def sind(x):
    return sin(radians(x))

fel = False
le = True

def keret(i,a,ro,r):
    with tollat(fel):
        fd(ro)
        rt(i*90)
    fd(a/2)
    rt(i*150)
    
    with tollat(fel):
        fd(r)
        rt(i*120)

def hatszogszilank(i, hatszog_korulirt_korenek_sugara):
    hatszog_magassaga=hatszog_korulirt_korenek_sugara*sqrt(3)/2

    with tollat(fel):
        fd(hatszog_magassaga)
    rt(i*90)
    fd(hatszog_korulirt_korenek_sugara/2)
    rt(i*60)
    fd(hatszog_korulirt_korenek_sugara/2)
    rt(i*90)
    with tollat(fel):
        fd(hatszog_magassaga)
    rt(i*120)

def felkorfele(i,kissugar,ro):
    with tollat(fel):
        fd(ro)
    
    rt(i*90)
    fd(kissugar)
    lt(90)
    t.circle(kissugar, extent = -i*90)
    lt(90)
    with tollat(fel):
        fd(kissugar)
    rt(i*90)
    lt(i*90)
    with tollat(fel):
        bk(ro)

def trapezfele(i,trapsugar, traptav):
    rt(i*60)
    with tollat(fel):
        fd(trapsugar)
    lt(i*90)
    fd(traptav)
    rt(i*60)
    fd(traptav)
    rt(i*120)
    fd(1.5*traptav)
    rt(i*90)
    with tollat(fel):
        fd(traptav*sqrt(3)/2+trapsugar)
    rt(i*120)


def hatodalakzat(i,a):
    ro = a*sqrt(3)/6
    r = 2*ro
    keret(i,a,ro,r)
    hatszogszilank(i, a/10)
    felkorfele(i,a/10,ro)
    trapezfele(i,r/3, r/7)

def otagucsillag(hova, R):
    with tollat(fel):
        rt(60)
        fd(hova)
        rt(144)
        fd(R)
        lt(180-18)

    x = R*sind(36)/sind(18)
    for j in range(5):
        fd(x)
        lt(180-36)

    with tollat(fel):
        rt(180-18)
        bk(R)
        lt(144)
        bk(hova)
        lt(60)

def pocmugi(a):
    ro = a*sqrt(3)/6
    r = 2*ro
    with debug(False):
        for j in range(3):
            rt(120)
            for i in [-1,1]:
                hatodalakzat(i,a)
            otagucsillag(0.7*r, 0.1*r)

bgcolor('black')
pencolor('white')
pensize(1)

lt(180)
pocmugi(300)


wait()