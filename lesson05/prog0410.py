# exercice 4.9 : var aleatoire X

from math import *

def gauss(bb, t) :
    S = bb
    n = int(input("Donnez le nombre d'intervalles : "))
    e = t/n
    x = e/2
    c = 1/sqrt(2*pi)
    for i in range(n) :
        y = exp(-x**2 / 2)
        S = S + y
        x = x + e
    S = c * S * e
    return S

print ("Caclcul des intervalles entre a et b")
a = float(input("Donnez la valeur de a : "))
b = float(input("Donnez la valeur de b : "))

if b == 0: rep = 0.5
if b > 0: rep = 0.5 + gauss(a, b)
if b < 0: rep = 0.5 - gauss(a, b)
print ("--------------- REPONSE ---------------")
print ("l'integrale vaut : ", rep)
