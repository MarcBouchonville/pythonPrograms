""" module multipli contenant la fonction table """

def table(nb, max=10):
    """ fonction affichnat la tbale de mutiplication par
        nombre de 1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print (i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

# test de la fonction
if __name__ == "__main__":
    table(4)
    os.system("pause")