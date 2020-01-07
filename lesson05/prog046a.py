# prog 4.6 - resoudre equation sqrt(x) = cos(x)

# tri dichotomique entre 0 et 2*pi

from math import sqrt, cos, pi

def fct(x) :
    y=sqrt(x) - cos(x)
    return y


limite = 0.0000000001
a=0
b=2*pi

while (b-a)>limite :
    moyenne = (a+b)/2
    if fct(a) * fct(moyenne) <= 0:
        b=moyenne
    else :
        a=moyenne

print("equation sqrt(x) = cos(x) ==> x = ", moyenne)
