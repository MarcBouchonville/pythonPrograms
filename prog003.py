print ("programme 2.3 - lecture de 4 nb entiers")
a = int ( input ("premier nombre : " ))
b = int ( input ("deuxieme nombre : " ))
c = int ( input ("troisieme nombre : " ))
d = int ( input ("quatrieme nombre : " ))

grand = 0
petit = 0

if a > b :
    grand = a
    petit = b
else :
    grand = b
    petit = a

if c > grand :
    grand = c
elif c < petit :
    petit = c
    
if d > grand :
    grand = d
elif d < petit :
    petit = d

print ("le plus grand nombre est : ", grand)
print ("le plus petit nombre est : ", petit)
print ("-------------")
