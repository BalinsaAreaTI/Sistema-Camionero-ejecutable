# Importación de Librerias
import serial
import sys
import time
import threading
import re
import ast
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidgetItem, QWidget, QHBoxLayout, QApplication, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap, QMovie, QColor, QFont

# Importación de los Layout
from View.Ui_inicioSistema import Ui_MainWindow
import sistemaCamioneras

# Importación de Base de Datos
from Base_de_Datos.database_conexion import Conectar # El archivo database_conexion.py

# ===============================
# Creación de la Clase Principal
# ===============================

class Inicio(QMainWindow):
    
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.moduloInicioSistemas = sistemaCamioneras.Inicio()
        
        self.conexion = Conectar()
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Resources/icono.png"))
        self.setWindowTitle('Sistema de Pesaje || Balinsa')
        
        self.ui.imgIngresoAlSistema.setPixmap(QPixmap("Resources/parteSuperiorInicioSesion.png"))
        self.ui.imgCirculoIngresoAlSistema.setPixmap(QPixmap("Resources/circuloInicioSesion.png"))
        self.ui.imgSalidaDelSistema.setPixmap(QPixmap("Resources/salidaSistema.png"))
        self.ui.imgLogoBalinsa.setPixmap(QPixmap("Resources/logoBalinsa.png"))
        self.ui.imgUser.setPixmap(QPixmap("Resources/icon1.png"))
        self.ui.imgPassword.setPixmap(QPixmap("Resources/icon2.png"))
        self.ui.btnSalirDelSistema.clicked.connect(self.fn_btnSalirDelSistema)
        self.ui.btnAccederSistema.clicked.connect(self.fn_btnValidarUsuario)
        
        self.db_consulta_usuarios = self.conexion.db_consulta_usuarios()
        self.ui.cbxUsers.clear()
        for usuario in self.db_consulta_usuarios:
            self.ui.cbxUsers.addItem(usuario[1])
            
        self.ui.txtUsers.setFocus(True)
        
    def fn_btnValidarUsuario(self):
        usuario = self.ui.cbxUsers.currentText().strip()
        password = self.ui.txtUsers.text().strip()
        
        resultado = self.conexion.db_verificarUsuario(usuario,password)
        
        if resultado is not None and len(resultado) > 0:
            if not self.moduloInicioSistemas:
                self.moduloInicioSistemas = sistemaCamioneras.Inicio()
            elif not self.moduloInicioSistemas.isVisible():
                self.moduloInicioSistemas.show()
            else:
                self.moduloInicioSistemas.showNormal()
                self.moduloInicioSistemas.activateWindow()
                
            self.close()
        else:
            thread = threading.Thread(target=self.fn_alertaCredenciales)
            thread.start()
    
    def fn_alertaCredenciales(self):   
        self.ui.lbltexto.setText("CREDENCIALES INCORRECTAS")
        self.ui.lbltexto.setStyleSheet("color: #FF0000;background-color: transparent;")
        time.sleep(3)
        self.ui.lbltexto.setText("SELECCIONA TU USUARIO Y ESCRIBE TU CONTRASEÑA")
        self.ui.lbltexto.setStyleSheet("color: #242424;background-color: transparent;")
        
    def fn_btnSalirDelSistema(self):
        self.close()

    def keyReleaseEvent(self, event):
        if (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return):
            self.fn_btnValidarUsuario()

# Llamamos a la Clase Principal para que Inicie el Sistema
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    gui = Inicio()
    gui.show()
    sys.exit(app.exec_())
    
# DISEÑADO Y DESARROLLADO POR SANTOS VILCHEZ EDINSON PASCUAL
# LA UNIÓN - PIURA - PERU ; 2024