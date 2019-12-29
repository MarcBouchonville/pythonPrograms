# accroissement d'etoiles par ligne

x = int(input("nombre de lignes d'étoiles : "))

for i in range(0, x):
    y=0
    i+=1
    print("")
    while y < i:
        y+=1
        print("*", end="")
print("")
print ("the end")