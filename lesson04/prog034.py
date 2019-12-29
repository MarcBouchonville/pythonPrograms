# ex. 3.4 légende hindoue

total = 0
nrCase = 1
nbGrain = 1

while nrCase <= 64:
    print ("case nr ", nrCase, " = ", nbGrain, "grains")
    total = total + nbGrain
    nrCase+=1
    nbGrain = nbGrain * 2

print("")
print ("au total, il y a ", nbGrain, "grains")
print ("the end")