# exercice 4.1 - distance de 2 points

from math import sqrt

def calculDist (x1, y1, x2, y2) :
    d = sqrt (((x2 - x1)**2) + ((y2 - y1)**2))
    return d


print ("Calcul de la distance entre 2 points dans le plan")
print ("premier point :")
a1 = float(input("abcisse du point 1 : "))
b1 = float(input("ordonnée du point 1 : "))

print ("second point :")
a2 = float(input("abcisse du point 1 : "))
b2 = float(input("ordonnée du point 1 : "))

reponse = calculDist(a1, b1, a2, b2)

print ("la distance de ces 2 points est = ", reponse)
print ("--------------------------------------------")
