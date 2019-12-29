# exercice 4.2 - 3 points non alignés
""" calcul : perimetre a b c
    dist a -> b
    dist b -> c
    dist c -> a
"""

from math import sqrt

def calculDist (x1, y1, x2, y2) :
    d = sqrt (((x2 - x1)**2) + ((y2 - y1)**2))
    return d


print ("Calcul de la distance entre 2 points dans le plan")
print ("premier point :")
a1 = float(input("abcisse du point 1 : "))
b1 = float(input("ordonnee du point 1 : "))

print ("deuxieme point :")
a2 = float(input("abcisse du point 2 : "))
b2 = float(input("ordonnee du point 2 : "))

print ("troisieme point :")
a3 = float(input("abcisse du point 3 : "))
b3 = float(input("ordonnee du point 3 : "))




distance1 = calculDist(a1, b1, a2, b2)
distance2 = calculDist(a2, b2, a3, b3)
distance3 = calculDist(a3, b3, a1, b1)

perimetre = distance1 + distance2 + distance3

print ("le perimetre du triangle formé par ces 3 points est = ", perimetre)
print ("--------------------------------------------")
