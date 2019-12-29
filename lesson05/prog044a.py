# exercice 4.4 : craps

"""
    DEFINITION

compte = le nième lancement de dés
total = total des dés
2 dés = deA et deB
score = le total obtenu

consignes:
- lance() = fct retournant la somme du total des dés (random)
- gagne() = proc écrivant "vous avez gagné"
- perdu() = proc écrivant "vous avez perdu"

"""

from random import *

# fonctions - procédures

def lance() :
    deA = random(1 ,6)
    deB = random(1, 6)
    total = deA + deB
    return total

def gagne() :
    print ("vous avez gagne")

def perdu() :
    print ("vous avez perdu")

#---------------
# programme principal

compte = 1

resultat = lance()
if resultat = 7 :
    gagne()
else if resultat = 11 :
    gagne()
else if resultat in range (2, 4) :
    perdu()

#./..
