# ex 3.7 table de multiplication de 1 à 10

"""
    DECLARATION
    INITIALISATION
"""



"""
    PROGRAMMATION
"""

for cpt in range (1, 11) :
    for x in range (1, 11) :
        rep = x * cpt
        if rep < 10 :
            print (rep, ' ' * 5, end="")
        else :
            print (rep, ' ' * 4, end="")
        x += 1
    print ("")
    cpt += 1
