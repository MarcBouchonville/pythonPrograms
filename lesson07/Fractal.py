# prog 7.4 : flocon de neige de Koch

from turtle import *

'''
    1) FONCTIONS
'''


def BR1(L):
    forward(L)
    left(60)
    forward(L)
    right(120)
    forward(L)
    left(60)
    forward(L)

def BR2(L):
    BR1(L)
    left(60)
    BR1(L)
    right(120)
    BR1(L)
    left(60)
    BR1(L)

def BR3(L):
    BR2(L)
    left(60)
    BR2(L)
    right(120)
    BR2(L)
    left(60)
    BR2(L)

def BR4(L):
    BR3(L)
    left(60)
    BR3(L)
    right(120)
    BR3(L)
    left(60)
    BR3(L)

'''
    2) PROGRAMME
'''

L=5
BR4(L)
right(120)
BR4(L)
right(120)
BR4(L)
