# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tree.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Arbol(object):
    def setupUi(self, Arbol):
        Arbol.setObjectName("Arbol")
        Arbol.resize(800, 600)
        Arbol.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Arbol.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Arbol)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree = QtWebEngineWidgets.QWebEngineView(Arbol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree.sizePolicy().hasHeightForWidth())
        self.tree.setSizePolicy(sizePolicy)
        self.tree.setMinimumSize(QtCore.QSize(750, 500))
        self.tree.setObjectName("tree")
        self.verticalLayout.addWidget(self.tree)
        self.actionGuardar = QtWidgets.QAction(Arbol)
        self.actionGuardar.setObjectName("actionGuardar")

        self.retranslateUi(Arbol)
        QtCore.QMetaObject.connectSlotsByName(Arbol)

    def retranslateUi(self, Arbol):
        _translate = QtCore.QCoreApplication.translate
        Arbol.setWindowTitle(_translate("Arbol", "Árbol Generado"))
        self.actionGuardar.setText(_translate("Arbol", "Guardar"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Arbol = QtWidgets.QWidget()
    ui = Ui_Arbol()
    ui.setupUi(Arbol)
    Arbol.show()
    sys.exit(app.exec_())
