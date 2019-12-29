print ("Annee bisextile")
ann = int ( input ("Entrez une année : "))
if ann % 400 == 0 :
    print (" l'annee ", ann, "est une annee bisextile")
elif ann % 4 == 0 :
    if ann % 100 != 0 :
        print (" l'annee ", ann, "est une annee bisextile")
    else :
        print ("l'annee ", ann, " n'est PAS une annee bisextile")
else :
    print ("l'annee ", ann, " n'est PAS une annee bisextile")
