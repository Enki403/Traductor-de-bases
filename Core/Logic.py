# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Core.ui.ui_conversor import Ui_Conversor
from Core.ui.ui_acercade import Ui_AcercaDe
from Core.ui.ui_gramatica import Ui_grammar
from Core.ui.ui_tree import Ui_Arbol
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
        self.ui.lexTable.resizeColumnsToContents()
        self.ui.lexTable.setColumnWidth(3,250)
        self.ui.lexTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ui.sinTable.resizeColumnsToContents()
        self.ui.sinTable.setColumnWidth(0,100)
        self.ui.sinTable.setColumnWidth(1,165)
        self.ui.sinTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        self.grammar = QtWidgets.QWidget()
        self.grammar_ui = Ui_grammar()
        self.grammar_ui.setupUi(self.grammar)

        self.about = QtWidgets.QWidget()
        self.about_ui = Ui_AcercaDe()
        self.about_ui.setupUi(self.about)

        self.analizador_sin = SinAnalizer()

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
        self.ui.lexTable.resizeColumnsToContents()
        self.ui.lexTable.setColumnWidth(3,250)
        self.ui.sinTable.resizeColumnsToContents()
        self.ui.sinTable.setColumnWidth(0,100)
        self.ui.sinTable.setColumnWidth(1,165)
        self.analizador_sin.arbol = []

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
    
    def treeWindow(self):
        """
            Muestra la ventana de gramática
        """
        self.tree_viewer = QtWidgets.QWidget()
        self.tree_ui = Ui_Arbol()
        self.tree_ui.setupUi(self.tree_viewer)

        self.tree_ui.tree.setHtml(self.getHtml())
        self.tree_viewer.show()
        
    
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
        self.ui.lexTable.setColumnWidth(3,250)
        
    
    def load_sin_table(self, data):
        """
            Carga la tabla de tokens del analizador sintáctico
        """
        self.ui.sinTable.setModel(TableModel(data, ["Operacion", "Resultado"]))
        self.ui.sinTable.setColumnWidth(0,100)
        self.ui.sinTable.setColumnWidth(1,165)
        self.ui.sinTable.resizeColumnsToContents()


    def traducir(self):
        """
            Se encarga de analizar y traducir la entrada
        """
        self.analizador_sin.arbol = []
        data_array = Auxiliar().plain_2_array(self.ui.inputBox.toPlainText())
        lex_data = LexAnalizer(data_array).tokenizar()
        self.analizador_sin.setText(data_array)
        sin_data = self.analizador_sin.analizar()
        
        self.load_lex_table(lex_data)

        self.load_sin_table(sin_data)

    def getHtml(self):
        """
            Retorna el html del arbol para generarlo con d3js
        """
        # con boton de descarga
        # parte1 = """<!DOCTYPE html><meta charset=utf-8><script src=http://d3js.org/d3.v5.min.js></script><style>body{background-color:#eee}.node circle{fill:#fff;stroke:#4682b4;stroke-width:3px}.node text{font:12px sans-serif;text-overflow:ellipsis;white-space:nowrap}.node--internal text{text-shadow:0 1px 0 #fff,0 -1px 0 #fff,1px 0 0 #fff,-1px 0 0 #fff}.link{fill:none;stroke:#ccc;stroke-width:2px}</style><input onclick=descargar() type=button value="Descargar imagen"><script>descargar = ()=>{var svgData = document.getElementsByTagName("svg");var svgBlob = new Blob([svgData], {type:"image/svg+xml;charset=utf-8"});var svgUrl = URL.createObjectURL(svgBlob);var downloadLink = document.createElement("a");downloadLink.href = svgUrl;downloadLink.download = "arbol_generado.svg";document.body.appendChild(downloadLink);downloadLink.click();document.body.removeChild(downloadLink);};const treeData="""
        
        # sin boton de descarga
        parte1 = """<!DOCTYPE html><html><meta charset="utf-8" /><head><script src="http://d3js.org/d3.v5.min.js"></script><style>body{background-color:#eee;}.node circle {fill: #fff;stroke: steelblue;stroke-width: 3px;}.node text {font: 12px sans-serif;text-overflow: ellipsis;white-space: nowrap;}.node--internal text {text-shadow: 0 1px 0 #fff, 0 -1px 0 #fff, 1px 0 0 #fff, -1px 0 0 #fff;}.link {fill: none;stroke: #ccc;stroke-width: 2px;}</style></head><body><script type="text/javascript">const treeData="""
        arbol = str(self.analizador_sin.get_formated_tree())
        parte2 = """;let tamanio=0;treeData.children.forEach((e)=>{tamanio+=175});tamanio=tamanio<750?750:tamanio;console.log(tamanio);const margin={top:50,right:90,bottom:50,left:90},width=tamanio-margin.left-margin.right,height=500-margin.top-margin.bottom;const treemap=d3.tree().size([width,height]).separation(function separation(a,b){return a.parent==b.parent?2:2});let nodes=d3.hierarchy(treeData,(d)=>d.children);nodes=treemap(nodes);const svg=d3.select("body").append("svg").attr("width",width+margin.left+margin.right).attr("height",height+margin.top+margin.bottom),g=svg.append("g").attr("transform","translate("+margin.left+","+margin.top+")");const link=g.selectAll(".link").data(nodes.descendants().slice(1)).enter().append("path").attr("class","link").attr("d",(d)=>{return "M"+d.x+","+d.y+"C"+d.x+","+(d.y+d.parent.y)/2+" "+d.parent.x+","+(d.y+d.parent.y)/2+" "+d.parent.x+","+d.parent.y});const node=g.selectAll(".node").data(nodes.descendants()).enter().append("g").attr("class",(d)=>"node"+(d.children?" node--internal":" node--leaf")).attr("transform",(d)=>"translate("+d.x+","+d.y+")");node.append("circle").attr("r",(d)=>30).style("stoke",(d)=>d.data.level);node.append("text").attr("dy",".35em").attr("y",(d)=>0).style("text-anchor","middle").text((d)=>d.data.name);</script></body></html>"""
        
        return parte1+arbol+parte2

    def viewTree(self):
        """
            Se encarga de mostrar el arbol sintáctico
            ToDo: Ver como guardar el arbol
        """
        # print(self.analizador_sin.get_formated_tree())
        self.treeWindow()
