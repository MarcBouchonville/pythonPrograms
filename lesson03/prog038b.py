# ex. 3.8 emprunt

"""
    DECLARATION
"""
"""
V = montant emprunté
i = taux périodique (annuel ou mensuel)
n = nombre de versements (annuel ou mensuel)
a = montant de chaque remboursement (annuel ou mensuel)

formule donnée :
a = i * V * (1 / (1 - ((1 + i)**-n))))

"""

"""
    INITIALISATION
"""

V = 20000.0
i = 0.1
n = 4

periode = 1
"""
    PROGRAMMATION
"""

a = i * V * ( 1 / ( 1 - ((1 + i)**-n) ) )

V = int(input("montant emprunté (indiquez 20.000 eur) : "))
i = float(input("taux périodique (indiquez 10 %) : "))
i = i/100
n = int(input("nombre de versements annuels souhaités (indiquez 4) : "))

print ("TABLEAU D'AMORTISSEMENT")
print ("***********************")
print ("")
print ("vous devrez payer à chaque période, un montant de ", round(a, 2), " EUR")
print ("")
print ("Période   Intérêts   Amortissement   Solde restant dû")

""" intérêts
I = i * V

    amortissements
A = a - I

    Solde restant dû
V = V - A
"""

while round(V, 1) > 0.0 :
    I = i * V
    A = a - I
    V = V - A
    nn = 4
    mm = 1
    for xx in range (nn):
        Val = [[periode], [round(I,2)], [round(A, 2)], [round(V, 2)]]
        print (Val)
    periode += 1




