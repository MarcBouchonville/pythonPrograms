# exercice 4.5 - ecrire le mot entré - entouré d'etoiles

# nb lettres * 2 + 8
def ligne(n):
    trace = ""
    for i in range(0, n) :
        if (i%2 == 0) :
            trace = trace + "*"
        else : trace = trace + " "
    return trace

def printMot(m) :
    x=0
    long = len(m) * 2
    for i in range (0, len(m)) :
        if i(i%2 == 0) :
            print (m[x], end='')
            x+=1
        else : print (" ", end='')

def debut(mots):
    for i in range(0, len(mots)+8) :
        i+=1
        lettre = 0
        long = len(mots)*2+5
        if (i == 1) :
            trace = trace + "*"
        elif i in range (1, 5) :
            trace = trace + " "
        elif i >= 5 && i < len(long) :
            ./......... to do ...


def fin():
    for i in range(1, 5) :
        i+=1
        if (i%2 == 0) :
            print ("*", end='')
        else : print (" ", end='')

mot = input("chaine de caracteres : ")
print ("nb de lettres : ", len(mot))
len(mot)
long = int(len(mot)) + 8
ligner = ligne(long)
print (ligner)
