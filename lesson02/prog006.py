print ("Exercice 2.6")
print ("------------")
print
result = "rien"
a = float ( input ("la cote sur 10 : "))
if a <= 10 :
    if a >= 9 :
        result = "excellent"
    elif a >= 8 :
        result = "très bien"
    elif a >= 6 :
        result = "bien"
    elif a >= 5 :
        result = "faible"
    elif a >= 3 :
        result = "médiocre"
    elif a >= 0 :
        result = "mauvais"
    else :
        print ("Affichez une cote > 0 !!")
else :
    print ("Entrez une cote < 10 !!!")
    
if result != "rien" :
    print ("pour votre cote ", a, " votre résultat est : ", result)