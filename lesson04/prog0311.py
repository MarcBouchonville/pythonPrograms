# 3.11 Heron

from math import *

# entree du nb dont on calcule la racine carree
a = float(input("Donnez un nombre reel : "))

# limite fixée jusqu'à 10 (exp-10) pour le calcul de la racine carree
eps = 10**-10
x=0
y=1
while fabs(x - y)>eps :
    x = y
    y = (x + a/x) / 2
    print(y)
