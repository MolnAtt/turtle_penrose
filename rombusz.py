from teknos import *

def rombusz(i, a, x, szin):
    fillcolor(szin)
    begin_fill()
    for j in range(2):
        fd(x)
        rt(i*a)
        fd(x)
        rt(i*(180-a))
    end_fill()
    fillcolor('black')
