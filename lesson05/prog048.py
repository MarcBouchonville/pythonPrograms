# resolution d'equations - methode CRAMER

def det(a1, b1, c1, a2, b2, c2):
    x = {}
    y = {}
    diviseur = ((a1 * b2) - (a2 * b1))
    if diviseur != 0 :
        x = ((c1 * b2) - (c2 * b1)) / diviseur
        y = ((a1 * c2) - (a2 * c1)) / diviseur
    else :
        x = "division par zero"
        y = "division par zero"
    """
        point = [x, y]
        print ("x = ", point[x])
        print ("y = ", point[y])
    """
    return x, y

print ("rentrez les valeurs pour la premiere equation : ")
print ("a1*x + b1*y = c1")
vala1 = float(input ("a1 = "))
valb1 = float(input ("b1 = "))
valc1 = float(input ("c1 = "))
print ("-------------------")

print ("rentrez les valeurs pour la econde equation : ")
print ("a2*x + b2*y = c2")
vala2 = float(input ("a2 = "))
valb2 = float(input ("b2 = "))
valc2 = float(input ("c2 = "))
print ("--------------------")
# tableau[x, y] = det(vala1, valb1, valc1, vala2, valb2, valc2)
valx, valy = det(vala1, valb1, valc1, vala2, valb2, valc2)

print ("x = ", valx)
print ("y = ", valy)
print ("----- FIN -----")
