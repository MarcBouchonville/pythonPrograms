print ("horoscope chinois")
print ("-----------------")

"""
DECLARATION
anneeMot : annee de naissance (en str)
x : longueur de la var anneeMot
nr = dernière lettre de anneeMot (pour dét l'élément)
elementAnnee : l'élément (metal, feu, ...)
annee : data anneeMot convertie en num$ entier (int)
chiffre : résultat de la division de l'année par 12 et récupération du modulo (+9)
nrSigne : le numéro du SIGNE correspondant
signe : le SIGNE (en texte) correspondant
"""



anneeMot = input ("année : ")
x = len(anneeMot)
# nr = le dernier chiffre de la string anneeMot
# afin de trouver l'élément
nr = anneeMot[x-1]
nr = int (nr)

# Exécution alternative
# alternative à 2 branches (if/else)
if nr == 0 or nr == 1 :
    elementAnnee = "metal"
elif nr == 2 or nr == 3 :
    elementAnnee = "eau"
elif nr == 4 or nr == 5 :
    elementAnnee = "bois"
elif nr == 6 or nr == 7 :
    elementAnnee = "feu"
elif nr == 8 or nr == 9 :
    elementAnnee = "terre"



# conversion de la var 'année' en num$
annee = int(anneeMot)

# Vu les 12 signes de l'horoscope chinois
# calcul pour trouver le signe de notre année
chiffre = (annee%12)+9
if chiffre > 12 :
    chiffre = chiffre - 12

# nrSigne = le signe decouvert
nrSigne = chiffre

# Détermination du signe :
if nrSigne == 1 :
    signe = "Rat"
elif nrSigne == 2 :
    signe = "Buffle"
elif nrSigne == 3 :
    signe = "Tigre"
elif nrSigne == 4 :
    signe = "Liévre"
elif nrSigne == 5 :
    signe = "Dragon"
elif nrSigne == 6 :
    signe = "Serpent"
elif nrSigne == 7 :
    signe = "Cheval"
elif nrSigne == 8 :
    signe = "Chèvre"
elif nrSigne == 9 :
    signe = "Singe"
elif nrSigne == 10 :
    signe = "Coq"
elif nrSigne == 11 :
    signe = "Chien"
elif nrSigne == 12 :
    signe = "Cochon"





# pour affichage des data
print ("né en ", annee, "Vous etes, dans l'horoscope chinois :")
print("signe : ", signe)
print ("element = ", elementAnnee)
