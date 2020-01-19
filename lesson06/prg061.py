# prog 6.1 : dictionnaire des capitales (28 pays)

'''
1) declaration
'''

dct={}

'''
2) initialisation
'''
dct['Allemagne'] = 'Berlin'
dct['Autriche'] = 'Vienne'
dct['Belgique'] = 'Bruxelles'
dct['Bulgarie'] = 'Sofia'
dct['Chypre'] = 'Nicosie'
dct['Croatie'] = 'Zagreb'
dct['Danemark'] = 'Copenhague'
dct['Espagne'] = 'Madrid'
dct['Estonie'] = 'Tallinn'
dct['Finlande'] = 'Helsinki'
dct['France'] = 'Paris'
dct['Grèce'] = 'Athènes'
dct['Hongrie'] = 'Budapest'
dct['Irlande'] = 'Dublin'
dct['Italie'] = 'Rome'
dct['Lettonie'] = 'Riga'
dct['Lituanie'] = 'Vilnius'
dct['Luxembourg'] = 'Luxembourg'
dct['Malte'] = 'La Valette'
dct['Pays-Bas'] = 'Amsterdam'
dct['Pologne'] = 'Varsovie'
dct['Portugal'] = 'Lisbonne'
dct['République tchèque'] = 'Prague'
dct['Roumanie'] = 'Bucarest'
dct['Royaume-Uni'] = 'Londres'
dct['Slovaquie'] = 'Bratislava'
dct['Slovénie'] = 'Ljubljana'
dct['Suède'] = 'Stockholm'

'''
3) programmation
'''
print ("----------------")
pays = input("Nom du pays dont vous voulez connaître la capitale : ")
resultat = dct.get(pays, 'coucou')
rech = pays in dct
if rech == True:
    print (pays, " : capitale = ", dct[pays])
else:
    print ("Le pays ", pays, "n'est pas mentionné dans la liste !")
    for i in dct:
        print (i, dct[i])
