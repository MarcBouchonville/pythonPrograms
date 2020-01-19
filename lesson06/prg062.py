# 6.2 recherche de plaque


'''
1) declaration
'''

client={}

'''
2) initialisation
'''

client = {'1-GTH-542':['Menfroid', 'Gerard', '0478 65 33 00'],
          '1-PHE-623':['Lergrave', 'Oussama', '0476 75 35 82'],
          '1-TGB-318':['Touille', 'Sacha', '0473 11 25 17'],
          '1-KLV-496':['Orlefrit', 'Jade', '0475 28 10 31'],
          '1-FHJ-572':['Covere', 'Harry', '0477 36 63 12'],
          '1-GVD-547':['Stike', 'Sophie', '0479 88 16 90']}

'''
3) programmation
'''

print ('')
plaque = input("Numéro d'immatriculation du client : ")
print ("")
if plaque not in client:
    print ("Plaque NON trouvée dans la liste !")
else:
    print("Nom : ", client[plaque][0])
    print("Prenom : ", client[plaque][1])
    print("Téléphone : ", client[plaque][2])
