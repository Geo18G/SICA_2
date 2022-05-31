from PyQt5.QtWidgets import *
from PyQt5 import uic

class ingreso_numeros(QMainWindow):
    
    def __init__(self):
        super(ingreso_numeros, self).__init__()
    
    def Ingreso_1(self):
        ingreso = self.ID.text()
        ingreso += '1'
        self.ID.setText(ingreso)

CL = ingreso_numeros()
