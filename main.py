# -*- coding: utf-8 -*-

from Core.Logic import *
import sys
import os

app = QtWidgets.QApplication(sys.argv)
Conversor = Logic()


Conversor.Conversor.show()
sys.exit(app.exec_())