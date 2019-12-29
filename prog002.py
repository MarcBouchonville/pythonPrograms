a = int ( input ("premier nombre : "))
b = int ( input ("second nombre : "))

msg1 = a, " est multiple de ", b
msg2 = b, " est multiple de ", a

if a % b == 0 :
    print (msg1)
elif b % a == 0 :
    print (msg2)
else :
    print (a, "n'est pas multiple de ", b)
    print (b, "n'est pas multiple de ", a)