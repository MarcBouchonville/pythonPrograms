# ex  : triangle.py

def etoiles(p):
    star = ''
    for i in range(1, p+1):
        star = star + ' '
    return star

def nb(a):
    liste = ""
    for i in range (1, a*2):
        if i%2 != 0:
            liste = liste + str(a)
        else :
            liste = liste + ' '
    return liste


n = int(input ('Donnez le nombre de lignes entre 2 et 9 : '))

if n >=2 and n <=9:
    partie1=''
    partie2=''
    for x in range (1, n+1):
        partie1 = etoiles(n-x)
        partie2 = nb(x)
        print (partie1, partie2, partie1)
else:
    print("Ce nombre n'est pas entre 2 et 9")
