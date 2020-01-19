''' pour l'ex 2. Parfait.py
1) parfait001.py : comment determiner un nb s'il est parfait
'''

n = int(input("entrez un nombre : "))
liste = []
for i in range(1, n):
    if n%i == 0:
        #print (i, " / ", n)
        liste.append(i)
        print ("liste : ", liste)

print ("tableau : ", liste)
S=0
for i in range (len(liste)):
    S = S+liste[i]
print("la somme des nombres = ", S)
if S == n:
    print (n, " est un nombre parfait")
else:
    print (n, " N'est PAS un nombre parfait")
