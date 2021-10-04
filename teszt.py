from teknos import *
import time

from aszimmetrikus_tizszog import aszimmetrikus_tizszog
from korivelem import korivelem
from osszetett_elem import osszetett_elem
from rombusz import rombusz
from szimmetrikus_tizszog_kozeppontbol import szimmetrikus_tizszog_kozeppontbol


x = 40

bgcolor('black')
pencolor('black')
pensize(1)
ht()

lt(90)
bk(200)
lt(90)

t = True
f = False


with debug(t):
    korivelem(1,x,10)

wait()