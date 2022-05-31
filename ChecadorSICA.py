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
        index.Number_4.clicked.connect(self.IngresoNumeros_4)
        index.Number_5.clicked.connect(self.IngresoNumeros_5)
        index.Number_6.clicked.connect(self.IngresoNumeros_6)
        index.Number_7.clicked.connect(self.IngresoNumeros_7)
        index.Number_8.clicked.connect(self.IngresoNumeros_8)
        index.Number_9.clicked.connect(self.IngresoNumeros_9)
        index.Number_0.clicked.connect(self.IngresoNumeros_0)
        codigo = index.ID.text()
        index.Aceptar.clicked.connect(perfil.obtener_codigo(codigo))
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

    def IngresoNumeros_4(self):
        ingreso = self.ID.text()
        ingreso += '4'
        self.ID.setText(ingreso)

    def IngresoNumeros_5(self):
        ingreso = self.ID.text()
        ingreso += '5'
        self.ID.setText(ingreso)

    def IngresoNumeros_6(self):
        ingreso = self.ID.text()
        ingreso += '6'
        self.ID.setText(ingreso)

    def IngresoNumeros_7(self):
        ingreso = self.ID.text()
        ingreso += '7'
        self.ID.setText(ingreso)

    def IngresoNumeros_8(self):
        ingreso = self.ID.text()
        ingreso += '8'
        self.ID.setText(ingreso)

    def IngresoNumeros_9(self):
        ingreso = self.ID.text()
        ingreso += '9'
        self.ID.setText(ingreso)

    def IngresoNumeros_0(self):
        ingreso = self.ID.text()
        ingreso += '0'
        self.ID.setText(ingreso)

    def Login(self):
        codigoBuscado = self.ID.text()
        print(codigoBuscado)
        if DB.database.select_user(codigoBuscado) == True:
            entrar = uic.loadUi(r"Nuevvo checador profes\Frame_login.ui", self)
            entrar.nombres.setText('Nombre perro')
            entrar.show()
    
class perfil(QMainWindow):
    def __init__(self):
        super(perfil, self).__init__()
        #entrar = uic.loadUi(r"Nuevvo checador profes\Frame_login.ui", self)
        # codigoBuscado = principal.obtener_codigo()
        # print(codigoBuscado)
        # if DB.database.select_user(codigoBuscado) == True:
        #     entrar.nombres.setText("Nombres nuevos")
        #     entrar.show()
    def obtener_codigo(codigo):
        print(codigo)


app = QApplication(sys.argv)
UIWindow = principal()
app.exec_()