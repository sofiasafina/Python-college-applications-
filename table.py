# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 500)
        Widget.setWindowTitle("Мои данные")

        self.tableWidget = QtWidgets.QTableWidget(Widget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 760, 380))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Значение"])

        self.addButton = QtWidgets.QPushButton(Widget)
        self.addButton.setGeometry(QtCore.QRect(20, 420, 120, 30))
        self.addButton.setText("Добавить")
        self.addButton.setObjectName("addButton")

        self.deleteButton = QtWidgets.QPushButton(Widget)
        self.deleteButton.setGeometry(QtCore.QRect(150, 420, 120, 30))
        self.deleteButton.setText("Удалить")
        self.deleteButton.setObjectName("deleteButton")

        self.refreshButton = QtWidgets.QPushButton(Widget)
        self.refreshButton.setGeometry(QtCore.QRect(280, 420, 120, 30))
        self.refreshButton.setText("Обновить")
        self.refreshButton.setObjectName("refreshButton")

        self.exitButton = QtWidgets.QPushButton(Widget)
        self.exitButton.setGeometry(QtCore.QRect(680, 420, 100, 30))
        self.exitButton.setText("Выход")
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Мои данные"))