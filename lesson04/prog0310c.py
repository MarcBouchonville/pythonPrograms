# ex. 3.10 calcul d'intégrale

import math

x=0

# valeur entre 0 et 1 :

# for (1=0 ; i<=1 ; i=i+0.1) ==>

for i in range (0, 11, 1) :
    #print ("valeur de i : ", i)
    x = x + math.sqrt(1 - ((i/10)**2))
    print ("valeur de x * 4 : ", x*4)

print ("aire de ce cette partie = ", x)
print ("nombre pi = ", x*4)
