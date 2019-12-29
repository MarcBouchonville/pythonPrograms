# 3.10 intégrale
# programme pr

from math import *
S = 0
n = int(input("Donnez le nombre d'intervalles : "))
e = 1 / n
x = e / 2
for i in range(n):
    y = sqrt(1 - (x**2))
    S = S + y
    x = x + e
    print("valeur de S x 4 = ", 4*S)
S = S * e
print ("l'intervalle vaut : ", S)
print ("la valeur approchée de pi est ", 4*S)
