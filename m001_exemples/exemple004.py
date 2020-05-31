# importation à faire pour la réalisation d'une interface graphique
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 1ere étape : création d'une application Qt avec QApplication
# afin d'avoir un fonctionnement correct avec IDLE ou Spyder
# on vérifie s'il existe déjà une instance de QApplication
app = QApplication.instance()
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = QWidget()

# ajout d'un titre à la fenetre
fen.setWindowTitle('Hello')

# la fenetre est rendue visible
fen.show()

# execution de l'application, l'execution permet de gérer les evenements
app.exec_()

# execution des evenement commence à partir de ce point
