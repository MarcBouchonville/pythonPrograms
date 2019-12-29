# exercice 3.3 bis
x = int(input("votre nb de lignes d'étoiles : "))
d = x

for i in range (1, x*2):
    if (i%2 != 0):
        print (" " * d + '*' * i)
        d-=1
    i+=1
    