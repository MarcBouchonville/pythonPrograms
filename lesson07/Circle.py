# prog 7.2 : cercles.py

from turtle import *

n=int(input('Donner le nombre de cercles : '))
i = 0
while i<n:
    circle(100)
    left(360/n)
    i+=1
