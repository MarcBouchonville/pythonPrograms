# correction 4.3

def triangle (n) :
    s=0
    i=0
    while s<n :
        s = s + i
        i = i + 1
    if s == n :
        tri = "est angulaire"
    else :
        tri = "n'est PAS angulaire"
    return tri

x = int(input("nombre entier : "))
res = triangle (x)
print (x, res)
