# 3.6 calculer la valeur de pi

"""
    DECLARATIONS
    INITIALISATION
"""

denom = 3
cpt = 0
rep01 = 1

"""
    PROGRAMMATION
"""

while 1/denom >= 10**-6 :
    cpt+=1
    if cpt % 2 == 0 :
        rep01 = rep01 + (1 / denom)
    else :
        rep01 = rep01 - (1 / denom)
    denom = denom + 2

# à la fin, on a (+/-) pi/4
reponse = rep01 * 4
print ("pi = ", reponse)
