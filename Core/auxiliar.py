# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog

class Auxiliar():
    """
        Contiene funciones auxiliares
    """
    def __init__(self):
        pass

    def plain_2_array(self, plain = ""):
        """
            Toma como entrada una cadena de texto y retorna un arreglo con las palabras separadas
        """
        return [ element.strip()  for element in plain.split('\n')]

    def open_file_dialog(self, parent, msg):
        """
            Abre una ventana para buscar un archivo y devuelve el contenido del archivo seleccionado
        """
        self.file_content = ""
        options = QFileDialog.Options()
        self.file_name, file_type = QFileDialog.getOpenFileName(parent, msg,"","Text Files (*.txt);;All Files (*)", options=options)
        if self.file_name:
            try:
                file = open(self.file_name, 'r')
                self.file_content = file.read()
                file.close()
            except:
                pass

        return self.file_content