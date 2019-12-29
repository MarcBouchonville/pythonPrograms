print ("programme 2.7")
print ("-------------")
print ("jeu de Pierre (P) - Feuille (F) - Ciseau (C)")
print
print ("joueur 1 :")
choix01 = input ("choix du premier joueur : ")
print ("joueur 2 :")
choix02 = input ("choix du deuxieme joueur : ")

if choix01 == choix02 :
    print ("egalite !!")
else :
    if choix01 == "F" :
        if choix02 == "P" :
            print ("la feuille enveloppe la pierre")
            print ("joueur1 = gagnant")
        elif choix02 == "C" :
            print ("les ciseaux coupent la feuille")
            print ("joueur2 = gagnant")
    elif choix01 == "P" :
        if choix02 == "C" :
            print ("la pierre casse les ciseaux")
            print ("joueur1 = gagnant")
        elif choix02 == "F" :
            print ("la feuille enveloppe la pierre")
            print ("joueur2 = gagnant")
    elif choix01 == "C" :
        if choix02 == "F" :
            print ("la feuille enveloppe la pierre")
            print ("joueur2 = gagnant")
        elif choix02 == "P" :
            print ("la pierre casse les ciseaux")
            print ("joueur2 = gagnant")