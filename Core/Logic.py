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

        # Se genera la ventana principal utilizando el ui_conversor.py
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

        # Se genera la ventana de gramatica utilizando el ui_gramatica.py
        self.grammar = QtWidgets.QWidget()
        self.grammar_ui = Ui_grammar()
        self.grammar_ui.setupUi(self.grammar)

        # Se genera la ventana de acercade utilizando el ui_acercade.py
        self.about = QtWidgets.QWidget()
        self.about_ui = Ui_AcercaDe()
        self.about_ui.setupUi(self.about)

        # Se inicializa el analizador Sintactico
        self.analizador_sin = SinAnalizer()

        # Se crean las conexiones de botones y acciones
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
            lambda: self.treeWindow()
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

        self.tree_ui.svgBtn.clicked.connect(
            lambda: self.download_svg()
        )
        
        self.tree_ui.pngBtn.clicked.connect(
            lambda: self.download_png()
        )

        self.tree_ui.tree.setHtml(self.getHtml())
        self.tree_viewer.show()

    def download_svg(self):
        """
            Ejecuta el codigo de JavaScript para descargar el arbol en formato svg
        """
        js_script = """descargarsvg()"""
        
        # Ejecuta la funcion de javascript
        self.tree_ui.tree.page().runJavaScript(js_script)
        
        # Maneja la solicitud de descarga
        self.tree_ui.tree.page().profile().downloadRequested.connect(self.tree_ui.download_requested)
        
        # Solo permite una descarga a la vez
        self.tree_ui.n = 0

    def download_png(self):
        """
            Ejecuta el codigo de JavaScript para descargar el arbol en formato png
        """
        js_script = """descargarpng()"""

        # Ejecuta la funcion de javascript
        self.tree_ui.tree.page().runJavaScript(js_script)

        # Maneja la solicitud de descarga        
        self.tree_ui.tree.page().profile().downloadRequested.connect(self.tree_ui.download_requested)
        
        # Solo permite una descarga a la vez
        self.tree_ui.n = 0

        
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
        # Agrega los encabezados a la tabla de lexemas
        self.ui.lexTable.setModel(TableModel(data, ["Línea", "Token", "Lexema", "Descripción"]))
        self.ui.lexTable.resizeColumnsToContents()
        self.ui.lexTable.setColumnWidth(3,250)
        
    
    def load_sin_table(self, data):
        """
            Carga la tabla de tokens del analizador sintáctico
        """
        # Agrega los encabezados a la tabla sintactica
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
            Genera pagina html y funciones JavaScript, esta pagina contiene el arbol generado (Utiliza d3.js)
        """
        parte1 = """<!DOCTYPE html><html><meta charset="utf-8" /><head><script src="http://d3js.org/d3.v5.min.js"></script><style>body{background-color:#eee;}</style></head><body><canvas id="canvas" hidden></canvas><script type="text/javascript">const treeData="""
        arbol = str(self.analizador_sin.get_formated_tree())
        parte2 = """;let tamanio=0;treeData.children.forEach((t=>{tamanio+=175})),tamanio=tamanio<750?750:tamanio;const margin={top:50,right:90,bottom:50,left:90},width=tamanio-margin.left-margin.right,height=500-margin.top-margin.bottom,treemap=d3.tree().size([width,height]).separation((function(t,e){return t.parent,e.parent,2}));let nodes=d3.hierarchy(treeData,(t=>t.children));nodes=treemap(nodes);const svg=d3.select("body").append("svg").attr("xmlns","http://www.w3.org/2000/svg").attr("width",width+margin.left+margin.right).attr("height",height+margin.top+margin.bottom).attr("style","background-color:#eee;"),g=svg.append("g").attr("transform","translate("+margin.left+","+margin.top+")"),link=g.selectAll(".link").data(nodes.descendants().slice(1)).enter().append("path").attr("style","fill:none ;stroke: #cccccc;stroke-width: 2px;").attr("d",(t=>"M"+t.x+","+t.y+"C"+t.x+","+(t.y+t.parent.y)/2+" "+t.parent.x+","+(t.y+t.parent.y)/2+" "+t.parent.x+","+t.parent.y)),node=g.selectAll(".node").data(nodes.descendants()).enter().append("g").attr("class",(t=>"node"+(t.children?" node--internal":" node--leaf"))).attr("transform",(t=>"translate("+t.x+","+t.y+")"));node.append("circle").attr("style","fill: #fff;stroke: steelblue;stroke-width: 3px;").attr("r",(t=>30)).style("stoke",(t=>t.data.level)),node.append("text").attr("style","text-anchor: middle;font: 12px sans-serif;text-overflow: ellipsis;white-space: nowrap;").attr("dy",".35em").attr("y",(t=>0)).text((t=>t.data.name));descargarsvg=()=>{const e=btoa(unescape(encodeURIComponent(document.querySelector("svg").outerHTML))),t=document.createElement("a"),o=new MouseEvent("click");t.download="download.svg",t.href="data:text/html;base64,"+e,t.dispatchEvent(o)};descargarpng=()=>{var e=document.getElementById("canvas");e.setAttribute("width",document.querySelector("svg").width.baseVal.value),e.setAttribute("height",document.querySelector("svg").height.baseVal.value);var t=e.getContext("2d"),a=new Image,n=new Blob([(new XMLSerializer).serializeToString(document.querySelector("svg"))],{type:"image/svg+xml;charset=utf-8"}),r=(self.URL||self.webkitURL||self).createObjectURL(n);a.src=r,a.onload=function(){t.drawImage(a,0,0);const n=document.createElement("a"),r=new MouseEvent("click");n.download="arbol.png",n.href=e.toDataURL("image/png"),n.dispatchEvent(r)}};</script></body></html>"""
        
        return parte1+arbol+parte2
