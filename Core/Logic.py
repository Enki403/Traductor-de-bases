# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.ui.ui_conversor import Ui_Conversor
from Core.ui.ui_acercade import Ui_AcercaDe
from Core.ui.ui_gramatica import Ui_grammar
from Core.table_model import TableModel
from Core.ui.icons_rc import *
from Core.auxiliar import *
from Core.lex_analizer import *
from Core.sin_analizer import *

class Logic(object):
    def __init__(self):

        self.Conversor = QtWidgets.QMainWindow()
        self.ui = Ui_Conversor()
        self.ui.setupUi(self.Conversor)

        self.grammar = QtWidgets.QWidget()
        self.grammar_ui = Ui_grammar()
        self.grammar_ui.setupUi(self.grammar)

        self.about = QtWidgets.QWidget()
        self.about_ui = Ui_AcercaDe()
        self.about_ui.setupUi(self.about)

        self.connections()

    def connections(self):
        """
            Se encarga de las conexiones de botones y QAction
        """
        # QAction
        self.ui.actionNuevo.triggered.connect(
            lambda: self.new()
        )
        
        self.ui.actionImportar.triggered.connect(
            lambda: self.import_file()
        )

        self.ui.actionCerrar.triggered.connect(
            lambda: self.Conversor.close()
        )

        self.ui.actionGramatica.triggered.connect(
            lambda: self.grammarWindow()
        )

        self.ui.actionAcerca_de.triggered.connect(
            lambda: self.aboutWindow()
        )

        # Buttons
        self.ui.analizeBtn.clicked.connect(
            lambda: self.traducir()
        )
        self.ui.treeBtn.clicked.connect(
            lambda: self.viewTree()
        )

    def new(self):
        """
            Borra todo para que quede en blanco
        """
        self.ui.inputBox.clear()     
        self.load_lex_table([["","","",""]])
        self.load_sin_table([["",""]])

    def import_file(self):
        """
            Carga un archivo de texto plano e ingresa el resultado en InputBox
        """
        self.ui.inputBox.setPlainText(Auxiliar().open_file_dialog(parent = self.Conversor, msg = "Importar archivo de texto plano (.txt)"))

    def grammarWindow(self):
        """
            Muestra la ventana de gramática
        """    
        self.grammar_ui.grammarCloseBtn_2.clicked.connect(
            lambda: self.grammar.close()
        )
        self.grammar.show()
        
    
    def aboutWindow(self): 
        """
            Muestra la ventana de los integrantes del grupo
        """      
        self.about_ui.AboutCloseBtn.clicked.connect(
            lambda: self.about.close()
        )
        self.about.show()
    
    def load_lex_table(self, data):
        """
            Carga la tabla de tokens del analizador léxico
        """
        self.ui.lexTable.setModel(TableModel(data, ["Línea", "Token", "Lexema", "Descripción"]))
        self.ui.lexTable.resizeColumnsToContents()
        self.ui.lexTable.setColumnWidth(3,365)
    
    def load_sin_table(self, data):
        """
            Carga la tabla de tokens del analizador sintáctico
        """
        self.ui.sinTable.setModel(TableModel(data, ["Operacion", "Resultado"]))
        self.ui.sinTable.resizeColumnsToContents()


    def traducir(self):
        """
            Se encarga de analizar y traducir la entrada
        """
        data_array = Auxiliar().plain_2_array(self.ui.inputBox.toPlainText())
        lex_data = LexAnalizer(data_array).tokenizar()
        sin_data = SinAnalizer(data_array).analizar()
        
        self.load_lex_table(lex_data)

        self.load_sin_table(sin_data)


    def viewTree(self):
        """
            Se encarga de mostrar el arbol sintáctico
            ToDo: Ver como generar el arbol y que libreria utilizar
        """
        print("Mostrar arbol")
