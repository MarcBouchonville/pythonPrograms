# ex 4.3 - les nombres triangulaires
# i = le nb de lignes

from math import *
from etoiles import stars


# fonction interne - calcul du nb de points
def triangle (t):
    rep = (t * (t + 1)) / 2
    return rep

nb = int(1)

while nb <= 5 :
    nbPts = int(triangle (nb))
    # affichage
    stars (nb)
    print ("T", nb, " = ", nbPts)
    nb+=1
    print ("----------")
