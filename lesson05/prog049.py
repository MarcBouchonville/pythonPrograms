# exercice 4.9 : var aleatoire X

from math import *

def gauss(t) :
    S = 0
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

print ("Caclcul des intervalles entre -infini et a")
a = float(input("Donnez la valeur de a : "))
if a == 0: rep = 0.5
if a > 0: rep = 0.5 + gauss(a)
if a < 0: rep = 0.5 - gauss(a)
print ("--------------- REPONSE ---------------")
print ("l'integrale vaut : ", rep)
