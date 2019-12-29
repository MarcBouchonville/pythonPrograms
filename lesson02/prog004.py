print ("exercice 2.4")
a = float ( input ("premier nombre : "))
b = float ( input ("second nombre : "))
signe = input ("signe à utiliser : ")
if signe == "+" :
    reponse = a + b
    print ("la reponse est : ", reponse)
elif signe == "-" :
    reponse = a - b
    print ("la reponse est : ", reponse)
elif signe == "*" :
    reponse = a * b
    print ("la reponse est : ", reponse)
elif signe == "/" :
    reponse = a / b
    print ("la reponse est : ", reponse)
else :
    print ("Vous n'avez pas entré un signe correct !")