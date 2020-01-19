# pro 7.1 - polygone

from turtle import *
from math import *

'''
    1) FONCTIONS
'''

def triangle (a, b, c, R):
    forward(c)
    left(b)
    forward(R)
    left(2*a)
    forward(R)
    left(b)
    forward(c)
    return



'''
    2) PROGRAMME
'''

n = int(input('Donner le nombre de côtés : '))
R = 100
c = 2*R*sin(pi/n)
a=90*(n-2)/n
b=90*(n+2)/n
g=360/n
i=0
while i < n:
    triangle(a, b, c, R)
    left(g)
    i+=1
