!#"C:\Fichiers copies\MarcNew\Prog informatiques\10_Internet\01_Programmation\Python\55_PyCharm\pythonPrograms\Modules"
# -*- coding :Latin -1 -*
import os   # On importe le module os qui dispose de variables
            # et de fonctions utiles pour dialoguer avec votre
            # syst ème d'exploitation

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ")  # On attend que l'utilisateur fournisse l'année qu'il désire tester
annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")

os.system("pause")
