# prog 047 - methode NEWTON de resolution d'equation

from math import *

def f_0(X) :
    Y=sqrt(X)-cos(X)
    return Y

def f_1(X) :
    Y=1/(2*sqrt(X))+sin(X)
    return Y

def Newton(A) :
    X=A-(f_0(A)/f_1(A))
    return X

eps=1.0e-10
a=2
y=f_0(a)
while fabs(y)>eps:
    a=Newton(a)
    y=f_0(a)

print ("la solution de cette equation est : x = ", a)