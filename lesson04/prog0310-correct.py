from math import sqrt, pi, isclose, fabs

x = int(input("entrez 1 : "))
I = sqrt(1-x**2)

y = int(input("entrez 0 : "))
J = sqrt(1-y**2)

if isclose(pi, fabs((I-J)*4), abs_tol=0.9):
    print("ok")
else:
    print("non ok")
    #print(I)
    #print(J)

print((I-J)*4)
