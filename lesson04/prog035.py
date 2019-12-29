# exercice 3.5 : prenom à l'envers

prenom = input("votre prénom : ")

i = len(prenom)
print ("nb de lettres : ", i)
for j in range (i-1, -1, -1):
    print(prenom[j] + "*",end="")
    j-=1
print("")
print("the end")