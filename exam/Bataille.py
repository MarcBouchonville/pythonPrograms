# ex.3 : Bataille.py

'''
    Bataille001.py : 
'''

'''
  *************************************
  *          1) FONCTIONS             *
  *************************************
'''

# selection carte

def selectCard ():
    result = False
    while result == False:
        nb = randint(1, 32)
        if dico[nb][2] == True:
            result = True
            dico[nb][2] = False
    return nb


def renouveler ():
    for i in range (1, 32):
        if dico[i][2] == False:
            dico[i][2] = True
    return

'''
  *************************************
  *          2) PROGRAMME             *
  *************************************
'''

'''
    2.1) DECLARATION
'''

from random import *
dico={}


'''
    2.2) INITIALISATION
'''

dico={1: [7, '7 de coeur', True],
      2: [8, '8 de coeur', True],
      3: [9, '9 de coeur', True],
      4: [10, '10 de coeur', True],
      5: [11, 'Valet de coeur', True],
      6: [12, 'Dame de coeur', True],
      7: [13, 'Roi de coeur', True],
      8: [14, 'AS de coeur', True],
      9: [7, '7 de trefle', True],
      10: [8, '8 de trefle', True],
      11: [9, '9 de trefle', True],
      12: [10, '10 de trefle', True],
      13: [11, 'Valet de trefle', True],
      14: [12, 'Dame de trefle', True],
      15: [13, 'Roi de trefle', True],
      16: [14, 'AS de trefle', True],
      17: [7, '7 de carreau', True],
      18: [8, '8 de carreau', True],
      19: [9, '9 de carreau', True],
      20: [10, '10 de carreau', True],
      21: [11, 'Valet de carreau', True],
      22: [12, 'Dame de carreau', True],
      23: [13, 'Roi de carreau', True],
      24: [14, 'AS de carreau', True],
      25: [7, '7 de pique', True],
      26: [8, '8 de pique', True],
      27: [9, '9 de pique', True],
      28: [10, '10 de pique', True],
      29: [11, 'Valet de pique', True],
      30: [12, 'Dame de pique', True],
      31: [13, 'Roi de pique', True],
      32: [14, 'AS de pique', True]}

'''
    2.3) PROGRAMMATION
'''

resultat = "Bataille !"


while resultat == "Bataille !":
    A=selectCard()
    B=selectCard()

    print("le joueur A a tiré la carte ", dico[A][1])
    print("le joueur B a tiré la carte ", dico[B][1])
    print("")

    if dico[A][0] > dico[B][0]:
        print("le joueur A a gagné")
        resultat="FIN"
    elif dico[A][0] < dico[B][0]:
        print("le joueur B a gagné")
        resultat="FIN"
    else:
        print ("Bataille !")
        print ("on retire une carte")
        print ("")

# reinitialisation du tableau dico :
renouveler()
