# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\leito\Music\SistemaCamioneras_v2\View\inicioSistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color: #FFCC21;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbxUsers = QtWidgets.QComboBox(self.centralwidget)
        self.cbxUsers.setGeometry(QtCore.QRect(570, 400, 314, 56))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.cbxUsers.setFont(font)
        self.cbxUsers.setStyleSheet("background-color: #2C618B;\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.cbxUsers.setObjectName("cbxUsers")
        self.lblIngresoAlSistema = QtWidgets.QLabel(self.centralwidget)
        self.lblIngresoAlSistema.setGeometry(QtCore.QRect(502, 0, 361, 75))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblIngresoAlSistema.setFont(font)
        self.lblIngresoAlSistema.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.lblIngresoAlSistema.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIngresoAlSistema.setObjectName("lblIngresoAlSistema")
        self.imgSalidaDelSistema = QtWidgets.QLabel(self.centralwidget)
        self.imgSalidaDelSistema.setGeometry(QtCore.QRect(1300, 10, 50, 50))
        self.imgSalidaDelSistema.setStyleSheet("background-color: #2C618B;\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"border-left: 1px solid #01304A;\n"
"border-right: 1px solid #01304A;\n"
"border-bottom: 5px solid #01304A;\n"
"padding: 5px;")
        self.imgSalidaDelSistema.setText("")
        self.imgSalidaDelSistema.setScaledContents(True)
        self.imgSalidaDelSistema.setObjectName("imgSalidaDelSistema")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 480, 56, 56))
        self.label_2.setStyleSheet("background-color: #01304A;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.imgUser = QtWidgets.QLabel(self.centralwidget)
        self.imgUser.setGeometry(QtCore.QRect(513, 400, 56, 56))
        self.imgUser.setStyleSheet("border-radius:10px;\n"
"background-color: #01304A;\n"
"padding: 15px;")
        self.imgUser.setText("")
        self.imgUser.setScaledContents(True)
        self.imgUser.setObjectName("imgUser")
        self.btnSalirDelSistema = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalirDelSistema.setGeometry(QtCore.QRect(1300, 10, 50, 50))
        self.btnSalirDelSistema.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalirDelSistema.setStyleSheet("background-color: transparent;")
        self.btnSalirDelSistema.setText("")
        self.btnSalirDelSistema.setObjectName("btnSalirDelSistema")
        self.lbltexto = QtWidgets.QLabel(self.centralwidget)
        self.lbltexto.setGeometry(QtCore.QRect(470, 550, 461, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbltexto.setFont(font)
        self.lbltexto.setStyleSheet("background-color: transparent;\n"
"color: #242424;")
        self.lbltexto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbltexto.setObjectName("lbltexto")
        self.imgLogoBalinsa = QtWidgets.QLabel(self.centralwidget)
        self.imgLogoBalinsa.setGeometry(QtCore.QRect(530, 660, 320, 80))
        self.imgLogoBalinsa.setText("")
        self.imgLogoBalinsa.setScaledContents(True)
        self.imgLogoBalinsa.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLogoBalinsa.setObjectName("imgLogoBalinsa")
        self.imgIngresoAlSistema = QtWidgets.QLabel(self.centralwidget)
        self.imgIngresoAlSistema.setGeometry(QtCore.QRect(460, 0, 450, 75))
        self.imgIngresoAlSistema.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.imgIngresoAlSistema.setText("")
        self.imgIngresoAlSistema.setScaledContents(True)
        self.imgIngresoAlSistema.setAlignment(QtCore.Qt.AlignCenter)
        self.imgIngresoAlSistema.setObjectName("imgIngresoAlSistema")
        self.imgCirculoIngresoAlSistema = QtWidgets.QLabel(self.centralwidget)
        self.imgCirculoIngresoAlSistema.setGeometry(QtCore.QRect(593, 110, 180, 180))
        self.imgCirculoIngresoAlSistema.setStyleSheet("border-radius: 90px;")
        self.imgCirculoIngresoAlSistema.setText("")
        self.imgCirculoIngresoAlSistema.setScaledContents(True)
        self.imgCirculoIngresoAlSistema.setAlignment(QtCore.Qt.AlignCenter)
        self.imgCirculoIngresoAlSistema.setObjectName("imgCirculoIngresoAlSistema")
        self.imgPassword = QtWidgets.QLabel(self.centralwidget)
        self.imgPassword.setGeometry(QtCore.QRect(830, 480, 56, 56))
        self.imgPassword.setStyleSheet("border-radius:10px;\n"
"background-color: #01304A;\n"
"padding: 15px;")
        self.imgPassword.setText("")
        self.imgPassword.setScaledContents(True)
        self.imgPassword.setObjectName("imgPassword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 400, 56, 56))
        self.label.setStyleSheet("background-color: #01304A;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.contenedorInicioSesion = QtWidgets.QLabel(self.centralwidget)
        self.contenedorInicioSesion.setGeometry(QtCore.QRect(420, 210, 535, 395))
        self.contenedorInicioSesion.setStyleSheet("border-radius: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.contenedorInicioSesion.setText("")
        self.contenedorInicioSesion.setAlignment(QtCore.Qt.AlignCenter)
        self.contenedorInicioSesion.setObjectName("contenedorInicioSesion")
        self.btnAccederSistema = QtWidgets.QPushButton(self.centralwidget)
        self.btnAccederSistema.setGeometry(QtCore.QRect(580, 580, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAccederSistema.setFont(font)
        self.btnAccederSistema.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccederSistema.setStyleSheet("QPushButton {\n"
"    background-color: #01304A;\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    border-left: 1px solid #011F2F;\n"
"    border-right: 1px solid #011F2F;\n"
"    border-bottom: 5px solid #011F2F;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #023E5E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #062B3F;\n"
"}")
        self.btnAccederSistema.setObjectName("btnAccederSistema")
        self.lblSistemaParaPesajeVehicular = QtWidgets.QLabel(self.centralwidget)
        self.lblSistemaParaPesajeVehicular.setGeometry(QtCore.QRect(420, 300, 535, 80))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblSistemaParaPesajeVehicular.setFont(font)
        self.lblSistemaParaPesajeVehicular.setStyleSheet("background-color: transparent;\n"
"color: #242424;")
        self.lblSistemaParaPesajeVehicular.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSistemaParaPesajeVehicular.setObjectName("lblSistemaParaPesajeVehicular")
        self.txtUsers = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsers.setGeometry(QtCore.QRect(515, 480, 314, 56))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtUsers.setFont(font)
        self.txtUsers.setStyleSheet("background-color: #2C618B;\n"
"color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"padding-left: 10px;")
        self.txtUsers.setObjectName("txtUsers")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 730, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1020, 730, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.contenedorInicioSesion.raise_()
        self.imgSalidaDelSistema.raise_()
        self.label_2.raise_()
        self.btnSalirDelSistema.raise_()
        self.lbltexto.raise_()
        self.imgLogoBalinsa.raise_()
        self.imgIngresoAlSistema.raise_()
        self.label.raise_()
        self.btnAccederSistema.raise_()
        self.lblSistemaParaPesajeVehicular.raise_()
        self.txtUsers.raise_()
        self.imgCirculoIngresoAlSistema.raise_()
        self.cbxUsers.raise_()
        self.imgUser.raise_()
        self.imgPassword.raise_()
        self.lblIngresoAlSistema.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblIngresoAlSistema.setText(_translate("MainWindow", "Ingreso al Sistema"))
        self.lbltexto.setText(_translate("MainWindow", "SELECCIONA TU USUARIO Y ESCRIBE TU CONTRASEÑA"))
        self.btnAccederSistema.setText(_translate("MainWindow", "ACCEDER"))
        self.lblSistemaParaPesajeVehicular.setText(_translate("MainWindow", "SISTEMA PARA \n"
" PESAJE VEHICULAR"))
        self.txtUsers.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.label_3.setText(_translate("MainWindow", "© 2024 Desarrollado por Jhon Huertas"))
        self.label_4.setText(_translate("MainWindow", "© 2024 Diseñado por Leonardo Garcia Jimenez"))
