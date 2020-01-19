# prog 6.4 - diviseurs - correct

def divise(n):
    divx=[1]
    for i in range(2, n):
        if n%i==0:
            divx.append(i)
    divx.append(n)
    return divx

na = int(input("Un nombre entier a : "))
diva = divise(na)
print (diva, '\n')
A = set(diva)

nb = int(input("Un nombre entier b : "))
divb = divise(nb)
print (divb, '\n')
B = set (divb)

print ("Les diviseurs communs de ", na, " et de", nb, " sont : ", A&B)
