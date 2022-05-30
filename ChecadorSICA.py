import pruebaDB as DB
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        index = uic.loadUi("Nuevvo checador profes\Login.ui", self)
        index.Number_1.clicked.connect(self.IngresoNumeros_1)
        index.Number_2.clicked.connect(self.IngresoNumeros_2)
        index.Number_3.clicked.connect(self.IngresoNumeros_3)
        index.Aceptar.clicked.connect(self.Login)

        index.show()

    def IngresoNumeros_1(self):
        ingreso = self.ID.text()
        ingreso += '1'
        self.ID.setText(ingreso)

    def IngresoNumeros_2(self):
        ingreso = self.ID.text()
        ingreso += '2'
        self.ID.setText(ingreso)

    def IngresoNumeros_3(self):
        ingreso = self.ID.text()
        ingreso += '3'
        self.ID.setText(ingreso)
    
    def Login(self):
        pass
        # codigoBuscado = self.ID.text()
        # print(codigoBuscado)
        # if DB.database.select_user(codigoBuscado) == True:
        #     entrar = uic.loadUi(r"proy pytohn\Py con interfaz\ventana2login.ui", self)
        #     entrar.show()
    
app = QApplication(sys.argv)
UIWindow = principal()
app.exec_()