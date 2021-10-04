from teknos import *
from szimmetrikus_tizszog_kozeppontbol import szimmetrikus_tizszog_kozeppontbol
from aszimmetrikus_tizszog import aszimmetrikus_tizszog
from rombusz import rombusz

def osszetett_elem(i,x):
    fd(x)
    lt(i*36)
    szimmetrikus_tizszog_kozeppontbol(x)

    aszimmetrikus_tizszog(i,x)

    for j in range(3):
        fd(x)
        rt(i*36)

    aszimmetrikus_tizszog(-i,x)
    
    lt(i*(180-36))
    fd(x)
    lt(i*72)
    fd(x)
    lt(i*36)
    szimmetrikus_tizszog_kozeppontbol(x)
    fd(x)
    lt(i*72)
    rombusz(i, 180-36, x, 'blue')
    rt(i*72)
    bk(x)
    rt(i*36)
    bk(x)
    rt(i*72)
    bk(x)
    rt(i*(180-36))
    fd(x)
    rt(i*36)
    fd(x)
    lt(i*72)
