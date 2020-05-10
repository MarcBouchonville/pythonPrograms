#!\C:\Users\Utilisateur\AppData\Local\Programs\Python\Python37 pythonw
'''
    d'abord un shebang (#!) suivi du chemin de l'interpreteur PYTHON
'''
# -*- coding:Latin-1 -*-
'''
    pseudo commentaire, devant être inclus à la 1ere ou 2eme ligne, indiquant
    le type de caractères : ici les chr$ accentués ASCII étendu.
'''
x=1
if x==1:
    t = True

if t==True:
    f = open("C:\\Fichiers copies\\MarcNew\\Prog informatiques\\10_Internet\\01_Programmation\\Python\\50_EPFC-Cours\\05_Theorie\\m001_exemples\\test.txt", "a")
    f.write("\nNow the file has more content!")
    f.close()
else:
    print ("PAS vrai !")

#open and read the file after the appending:
f = open("C:\\Fichiers copies\\MarcNew\\Prog informatiques\\10_Internet\\01_Programmation\\Python\\50_EPFC-Cours\\05_Theorie\\m001_exemples\\test.txt", "r")
print(f.read())
