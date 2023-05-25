from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox
import numpy as np
def verif(ch):
    test = True
    for i in range(len(ch)):
        if not(65 <= ord(ch[i].upper()) <= 90):
            test= False
    return test

def puissance(x,y):
    p = 1
    for i in range(y):
        p *= x
    return p

def crypter(ch,t):
    p,q,e = 17,19,5
    c = ""
    s = 1
    for i in range(len(ch)):
        t[s] = (puissance((ord(ch[i].upper()) - 64),e) % (p*q))
        c += str(t[s]) +"-"
        s += 1
    return c[:-1]
def play():
    ch = root.mer.text()

    if not(verif(ch)):
        root.code.setText('veuillez saisir une chaine purement alphabétique')
    else:
        c = crypter(ch,t)
        root.code.setText('code du message crypté : '+c)

def close():
    root.destroy()
def clear():
    root.code.clear()
    root.mer.clear()

t = np.array([int]*999)
app = QApplication([])
root = loadUi('converter.ui')
root.crypter.clicked.connect(play)
root.Quitter.clicked.connect(close)
root.Annuler.clicked.connect(clear)
root.show()
app.exec_()