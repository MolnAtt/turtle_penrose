from teknos import *
from rombusz import rombusz

def aszimmetrikus_tizszog(i,x):
    rombusz(i, 72, x, 'gray')
    for j in range(1):
        fd(x)
        rt(i*36)
    rombusz(i, 36, x, 'blue')
    for j in range(2):
        fd(x)
        rt(i*36)
    rombusz(i, 72, x, 'gray')
    rt(i*72)
    rombusz(i, 36, x, 'blue')
    lt(i*72)
    for j in range(1):
        fd(x)
        rt(i*36)
    rombusz(i, 36, x, 'blue')
    for j in range(2):
        fd(x)
        rt(i*36)
    rombusz(i, 108, x, 'gray')
    for j in range(1):
        fd(x)
        rt(i*36)
    rombusz(i, 36, x, 'blue')
    rt(i*36)
    rombusz(i, 36, x, 'blue')
    lt(i*36)
    for j in range(2):
        fd(x)
        rt(i*36)
    rombusz(i, 108, x, 'gray')
    for j in range(1):
        fd(x)
        rt(i*36)
    rt(i*72)
    fd(x)
    lt(i*36)
    rombusz(i, 72, x, 'gray')
    rt(i*36)
    bk(x)
    lt(i*72)
