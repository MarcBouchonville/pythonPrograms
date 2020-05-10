#!\C:\Users\Utilisateur\AppData\Local\Programs\Python\Python37 pythonw
'''
    d'abord un shebang (#!) suivi du chemin de l'interpreteur PYTHON
'''
# -*- coding:Latin-1 -*-
'''
    pseudo commentaire, devant être inclus à la 1ere ou 2eme ligne, indiquant
    le type de caractères : ici les chr$ accentués ASCII étendu.
'''

# test : prog de pierre, papier, ciseaux


import random
import time

pierre = 1
papier = 2
ciseaux = 3

noms = { pierre: "Pierre", papier: "Papier", ciseaux: "Ciseaux" }
regles = { pierre: ciseaux, papier: pierre, ciseaux: papier }

joueur_score = 0
ordinateur_score = 0

def start():
    print("Jouons au pierre - papier - ciseaux !")
    while jeu():
        pass
    scores()

def jeu():
    joueur = bouge()
    ordinateur = random.randint(1, 3)
    resultat(joueur, ordinateur)
    return joue_encore()

def bouge():
    while True:
        joueur = input("pierre = 1\nPapier = 2\nCiseaux = 3\nChoix : ")
        try:
            joueur = int(joueur)
            if joueur in (1,2,3):
                return joueur
        except ValueError:
            pass
        print ("Choix uniquement entre 1 - 2 - 3 !")

def resultat(joueur, ordinateur):
    print ("1...")
    time.sleep(1)
    print ("2...")
    time.sleep(1)
    print ("3...")
    time.sleep(0.5)
    print ("l'ordinateur a choisi {0} !".format(noms[ordinateur]))
    global joueur_score, ordinateur_score
    if joueur == ordinateur:
        print ("bataille !")
    else:
        if regles[joueur] == ordinateur:
            print ("tu as gagné !")
            joueur_score+=1
        else:
            print ("tu as perdu !")
            ordinateur_score+=1

def joue_encore():
    reponse = input("Veux-tu encore jouer (o/n) ? : ")
    if reponse in ("o", "oui"):
        return reponse
    else:
        print ("Merci et à bientôt")


def scores():
    global joueur_score, ordinateur_score
    print ("RESULTATS")
    print ("joueur : ", joueur_score)
    print ("PC : ", ordinateur_score)


if __name__ == '__main__':
    print("début")
    start()
