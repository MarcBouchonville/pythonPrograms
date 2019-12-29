# 3.3 affichage en sapin

def stars (x) :
	d = x
	for i in range(0, x+1):
		y=0
		i+=1
		#print("")
		print(' ' * d, end="")
		if (i%2 == 0):
			print("x ")
		else :
			d-=1
			while y < i:
				y+=1
				print("* ", end="")
	print("")
