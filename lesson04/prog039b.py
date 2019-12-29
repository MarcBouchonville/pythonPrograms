# exercice 3.9 - 10 coups pour deviner un chiffre

from random import *

x = int(random() * 1000)
print("valeur à trouver = ", x)
donnee = type(x)
# print ("type de data = ", donnee)

resultat = "perdu"

cpt=1

if donnee == int :
    print ("ok")
    while cpt < 11 :
        print ("votre test : ", cpt, " sur 10")
        chiffre = int(input("votre chiffre : "))
        valeur = type(chiffre)
        if valeur == int :
            # print ("type de donnee : ok")
            if chiffre < x :
                print ("chiffre ", chiffre, " = trop PETIT !")
                cpt +=1
            elif chiffre > x :
                print ("chiffre ", chiffre, " = trop GRAND !")
                cpt +=1
            elif chiffre == x :
                print ("Vous avez trouvé le bon chiffre en ", cpt, " coups. C'est gagné")
                resultat = "gagné"
                cpt = int(11)
        else :
            print ("Vous avez perdu !")
            print ("vous devez taper un chiffre entier !!!")
            cpt = 11

    print ("-------")
    if resultat == "perdu" :
        print ("Vous n'avez pas trouvé ! Le chiffre à trouver était : ", x)                                                           
    
else:
    print ("Vous avez perdu !")
    print ("vous devez taper un chiffre entier !!!")
    cpt = 11
    resultat = "perdu"



