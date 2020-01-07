def fct(mots):
    retour = ''
    retour = '*    '
    let=0
    for i in range (0, (len(mots)*2)) :
        if i%2 == 0 or i == 0 :
            #print (mots[let])
            retour = retour + mots[let]
            let+=1
        else :
            retour = retour + ' '
    retour = retour + '    *'
    return retour


mot = input('entrez vos mots : ')
lg = len(mot)
print ('* ' * (lg+4), '*')
retour = fct(mot)
print (retour)
print ('* ' * (lg+4), '*')