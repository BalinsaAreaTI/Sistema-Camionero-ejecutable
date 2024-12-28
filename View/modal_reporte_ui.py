# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\leito\Music\SistemaCamioneras_v2\View\modal_reporte.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modal_reporte(object):
    def setupUi(self, modal_reporte):
        modal_reporte.setObjectName("modal_reporte")
        modal_reporte.setWindowModality(QtCore.Qt.NonModal)
        modal_reporte.resize(1366, 768)
        modal_reporte.setMinimumSize(QtCore.QSize(1366, 768))
        modal_reporte.setMaximumSize(QtCore.QSize(1400, 700))
        modal_reporte.setStyleSheet("#modal_reporte{\n"
"    background-color: #FFCC21;\n"
"}")
        self.imgLogoBalinsa = QtWidgets.QLabel(modal_reporte)
        self.imgLogoBalinsa.setGeometry(QtCore.QRect(1020, 605, 320, 80))
        self.imgLogoBalinsa.setText("")
        self.imgLogoBalinsa.setScaledContents(True)
        self.imgLogoBalinsa.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLogoBalinsa.setObjectName("imgLogoBalinsa")
        self.calendarWidgetDesde = QtWidgets.QCalendarWidget(modal_reporte)
        self.calendarWidgetDesde.setGeometry(QtCore.QRect(50, 80, 312, 183))
        self.calendarWidgetDesde.setStyleSheet("")
        self.calendarWidgetDesde.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidgetDesde.setObjectName("calendarWidgetDesde")
        self.imgCalendarioDesde = QtWidgets.QLabel(modal_reporte)
        self.imgCalendarioDesde.setGeometry(QtCore.QRect(320, 40, 45, 40))
        self.imgCalendarioDesde.setStyleSheet(" background-color: #01304A;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;")
        self.imgCalendarioDesde.setText("")
        self.imgCalendarioDesde.setScaledContents(True)
        self.imgCalendarioDesde.setObjectName("imgCalendarioDesde")
        self.dateEditConsultarDesde = QtWidgets.QDateEdit(modal_reporte)
        self.dateEditConsultarDesde.setEnabled(False)
        self.dateEditConsultarDesde.setGeometry(QtCore.QRect(110, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditConsultarDesde.setFont(font)
        self.dateEditConsultarDesde.setStyleSheet("border: 2px solid #ddd;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"padding-left: 10px;")
        self.dateEditConsultarDesde.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 5, 20), QtCore.QTime(5, 0, 0)))
        self.dateEditConsultarDesde.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEditConsultarDesde.setTimeSpec(QtCore.Qt.UTC)
        self.dateEditConsultarDesde.setObjectName("dateEditConsultarDesde")
        self.btnCalendarioDesde = QtWidgets.QPushButton(modal_reporte)
        self.btnCalendarioDesde.setGeometry(QtCore.QRect(320, 40, 45, 40))
        self.btnCalendarioDesde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalendarioDesde.setStyleSheet("background-color:transparent;")
        self.btnCalendarioDesde.setText("")
        self.btnCalendarioDesde.setObjectName("btnCalendarioDesde")
        self.frame = QtWidgets.QFrame(modal_reporte)
        self.frame.setGeometry(QtCore.QRect(0, 810, 1440, 40))
        self.frame.setStyleSheet("background-color: #333;\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblFechaHora = QtWidgets.QLabel(self.frame)
        self.lblFechaHora.setGeometry(QtCore.QRect(15, 0, 1000, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblFechaHora.setFont(font)
        self.lblFechaHora.setObjectName("lblFechaHora")
        self.frame_2 = QtWidgets.QFrame(modal_reporte)
        self.frame_2.setGeometry(QtCore.QRect(30, 190, 1300, 400))
        self.frame_2.setStyleSheet("border: 2px solid #ddd;\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tblDetallePesadas = QtWidgets.QTableWidget(self.frame_2)
        self.tblDetallePesadas.setGeometry(QtCore.QRect(0, 2, 1296, 396))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(10)
        self.tblDetallePesadas.setFont(font)
        self.tblDetallePesadas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border:2px solid black;\n"
"border-left:0;\n"
"border-right:0;\n"
"border-top:0;\n"
"\n"
"")
        self.tblDetallePesadas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblDetallePesadas.setTabKeyNavigation(True)
        self.tblDetallePesadas.setProperty("showDropIndicator", False)
        self.tblDetallePesadas.setDragDropOverwriteMode(True)
        self.tblDetallePesadas.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblDetallePesadas.setObjectName("tblDetallePesadas")
        self.tblDetallePesadas.setColumnCount(14)
        self.tblDetallePesadas.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetallePesadas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblDetallePesadas.setHorizontalHeaderItem(13, item)
        self.tblDetallePesadas.horizontalHeader().setStretchLastSection(True)
        self.tblDetallePesadas.verticalHeader().setVisible(False)
        self.tblDetallePesadas.verticalHeader().setCascadingSectionResizes(False)
        self.tblDetallePesadas.verticalHeader().setHighlightSections(False)
        self.tblDetallePesadas.verticalHeader().setSortIndicatorShown(False)
        self.tblDetallePesadas.verticalHeader().setStretchLastSection(False)
        self.imgCalendarioHasta = QtWidgets.QLabel(modal_reporte)
        self.imgCalendarioHasta.setGeometry(QtCore.QRect(320, 110, 45, 40))
        self.imgCalendarioHasta.setStyleSheet(" background-color: #01304A;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;")
        self.imgCalendarioHasta.setText("")
        self.imgCalendarioHasta.setScaledContents(True)
        self.imgCalendarioHasta.setObjectName("imgCalendarioHasta")
        self.btnCalendarioHasta = QtWidgets.QPushButton(modal_reporte)
        self.btnCalendarioHasta.setGeometry(QtCore.QRect(320, 110, 45, 40))
        self.btnCalendarioHasta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalendarioHasta.setStyleSheet("background-color:transparent;")
        self.btnCalendarioHasta.setText("")
        self.btnCalendarioHasta.setObjectName("btnCalendarioHasta")
        self.dateEditConsultarHasta = QtWidgets.QDateEdit(modal_reporte)
        self.dateEditConsultarHasta.setEnabled(False)
        self.dateEditConsultarHasta.setGeometry(QtCore.QRect(110, 110, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditConsultarHasta.setFont(font)
        self.dateEditConsultarHasta.setStyleSheet("border: 2px solid #ddd;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"padding-left: 10px;")
        self.dateEditConsultarHasta.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 5, 20), QtCore.QTime(5, 0, 0)))
        self.dateEditConsultarHasta.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEditConsultarHasta.setTimeSpec(QtCore.Qt.UTC)
        self.dateEditConsultarHasta.setObjectName("dateEditConsultarHasta")
        self.lblNroTicket = QtWidgets.QLabel(modal_reporte)
        self.lblNroTicket.setGeometry(QtCore.QRect(30, 40, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblNroTicket.setFont(font)
        self.lblNroTicket.setObjectName("lblNroTicket")
        self.lblNroTicket_2 = QtWidgets.QLabel(modal_reporte)
        self.lblNroTicket_2.setGeometry(QtCore.QRect(30, 110, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblNroTicket_2.setFont(font)
        self.lblNroTicket_2.setObjectName("lblNroTicket_2")
        self.calendarWidgetHasta = QtWidgets.QCalendarWidget(modal_reporte)
        self.calendarWidgetHasta.setGeometry(QtCore.QRect(50, 150, 312, 183))
        self.calendarWidgetHasta.setStyleSheet("")
        self.calendarWidgetHasta.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidgetHasta.setObjectName("calendarWidgetHasta")
        self.frame.raise_()
        self.lblNroTicket.raise_()
        self.lblNroTicket_2.raise_()
        self.frame_2.raise_()
        self.dateEditConsultarHasta.raise_()
        self.imgCalendarioHasta.raise_()
        self.dateEditConsultarDesde.raise_()
        self.imgLogoBalinsa.raise_()
        self.calendarWidgetDesde.raise_()
        self.imgCalendarioDesde.raise_()
        self.btnCalendarioDesde.raise_()
        self.btnCalendarioHasta.raise_()
        self.calendarWidgetHasta.raise_()

        self.retranslateUi(modal_reporte)
        QtCore.QMetaObject.connectSlotsByName(modal_reporte)

    def retranslateUi(self, modal_reporte):
        _translate = QtCore.QCoreApplication.translate
        modal_reporte.setWindowTitle(_translate("modal_reporte", "Alerta"))
        self.dateEditConsultarDesde.setDisplayFormat(_translate("modal_reporte", "dd-MM-yyyy"))
        self.lblFechaHora.setText(_translate("modal_reporte", "24 de Noviembre del 2023 - 12:00:00"))
        item = self.tblDetallePesadas.verticalHeaderItem(0)
        item.setText(_translate("modal_reporte", "00001"))
        item = self.tblDetallePesadas.horizontalHeaderItem(0)
        item.setText(_translate("modal_reporte", "TICKET"))
        item = self.tblDetallePesadas.horizontalHeaderItem(1)
        item.setText(_translate("modal_reporte", "FECHA INICIAL"))
        item = self.tblDetallePesadas.horizontalHeaderItem(2)
        item.setText(_translate("modal_reporte", "HORA INICIAL"))
        item = self.tblDetallePesadas.horizontalHeaderItem(3)
        item.setText(_translate("modal_reporte", "PESO BRUTO"))
        item = self.tblDetallePesadas.horizontalHeaderItem(4)
        item.setText(_translate("modal_reporte", "PESO TARA"))
        item = self.tblDetallePesadas.horizontalHeaderItem(5)
        item.setText(_translate("modal_reporte", "PESO NETO"))
        item = self.tblDetallePesadas.horizontalHeaderItem(6)
        item.setText(_translate("modal_reporte", "PLACA VEHICULAR"))
        item = self.tblDetallePesadas.horizontalHeaderItem(7)
        item.setText(_translate("modal_reporte", "RAZON SOCIAL"))
        item = self.tblDetallePesadas.horizontalHeaderItem(8)
        item.setText(_translate("modal_reporte", "CONDUCTOR"))
        item = self.tblDetallePesadas.horizontalHeaderItem(9)
        item.setText(_translate("modal_reporte", "TRANSPORTISTA"))
        item = self.tblDetallePesadas.horizontalHeaderItem(10)
        item.setText(_translate("modal_reporte", "PRODUCTO"))
        item = self.tblDetallePesadas.horizontalHeaderItem(11)
        item.setText(_translate("modal_reporte", "OBSERVACION"))
        item = self.tblDetallePesadas.horizontalHeaderItem(12)
        item.setText(_translate("modal_reporte", "FECHA FINAL"))
        item = self.tblDetallePesadas.horizontalHeaderItem(13)
        item.setText(_translate("modal_reporte", "HORA FINAL"))
        self.dateEditConsultarHasta.setDisplayFormat(_translate("modal_reporte", "dd-MM-yyyy"))
        self.lblNroTicket.setText(_translate("modal_reporte", "DESDE :"))
        self.lblNroTicket_2.setText(_translate("modal_reporte", "HASTA :"))
