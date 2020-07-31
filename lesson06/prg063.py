# 6.3 Tableau des notes de musique

'''
1) declaration
'''

tableau={}

'''
2) initialisation
'''

tableau = {'do':['32,70', '65,41', '130,81', '261,63', '523,25', '1046,50', '2093,00', '4186,01'],
         'ré':['36,71', '73,42', '146,83', '293,66', '587,33', '1174,66', '2349,32', '4698,64'],
         'mi':['41,20', '82,41', '164,81', '329,63', '659,26', '1318,51', '2637,02', '5274,04'],
         'fa':['43,65', '87,31', '174,61', '349,21', '698,46', '1396,91', '2793,83', '5587,65'],
         'sol':['49,00', '98,00', '196,00', '392,00', '783,99', '1567,98', '3135,96', '6271,93'],
         'la':['55,00', '110,00', '220,00', '440,00', '880,00', '1760,00', '3520,00', '7040,00'],
         'si':['61,74', '123,47', '246,94', '493,88', '987,77', '1975,53', '3951,07', '7902,13']}


'''
3) programmation
'''

print ('')
note = input("précisez la note : ")
if note in tableau:
    octave = int(input("l'octave voulue : "))
    if octave in range(8):
        print("frequence : ", tableau[note][octave], "Hz")
    else:
        print ("octave entre 0 et 7 !!")
else:
    print("note non conforme !")
print ("")