# prog 7.3 : spirale

from turtle import *

n=int(input('Donner le nombre de demi-tours'))
r = 10

for i in range(1, n+1):
    R = i*r
    circle(R, 180)
