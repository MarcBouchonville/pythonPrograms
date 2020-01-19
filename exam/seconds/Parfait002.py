# ex 2. Parfait.py

'''
    1) FONCTIONS
'''

# determiner la liste des diviseurs d'un nb
def listing(nb):
    liste = []
    for i in range(1, nb):
        if nb%i == 0:
            #print (i, " / ", n)
            liste.append(i)
            #print ("liste : ", liste)
    return liste

# determiner si le nb est parfait
def detParfait(tab, nn):
    result = ""
    # print ("tableau : ", tab, " et ", nn)
    S=0
    listing = ""
    for i in range (len(tab)):
        S = S+tab[i]
        if listing == "":
            listing=str(tab[i])
        else:
            listing=listing + " + " + str(tab[i])
    # print(listing, " = ", S)
    if S == nn:
        print(listing, " = ", S)
        print (nn, " est un nombre parfait")
        result = "ok"
        print ("- - - - - - - - - - - - - - - - - - -")
    else:
        # print (nn, " N'est PAS un nombre parfait")
        result = "no"
    # print ("- - - - - - - - - - - - - - - - - - -")
    return result

'''
    2) PROGRAMME
'''

'''
    2.1) DECLARATION - INITIALISATION
'''

lst1=[]     # liste comprenant les diviseurs d'un nb
rep1 = ""
lst2=[]     # liste reprenant uniquement les nb parfaits

'''
    2.2) PROGRAMMATION
'''

n = int(input("entrez un nombre : "))

for x in range (1, n+1):
    lst1 = listing(x)
    rep1 = detParfait(lst1, x)
    if rep1 == "ok":
        lst2.append(x)
    rep=""
    lst1=[]

print("------------------------------------------------")
print ("THE END")
print("------------------------------------------------")
print ("les nombres parfaits entre 1 et ", n, "sont :")
print (lst2)
    



