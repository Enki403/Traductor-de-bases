# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog

class Auxiliar():
    """
        Contiene funciones auxiliares
    """
    def __init__(self):

        self.UNIDADES = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
        self.UNIDADES_DIEZ = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve']
        self.DECENAS = ['cero', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
        self.CIENTOS = ['_', 'ciento', 'docientos', 'trecientos', 'cuatrocientos', 'quinientos', 'seicientos', 'setecientos', 'ochocientos', 'novecientos']

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

    def leer_decenas(self, numero):
        """
            lee las decenas del numero
        """
        if numero < 10:
            return self.UNIDADES[numero]
        decena, unidad = divmod(numero, 10)
        if numero <= 19:
            resultado = self.UNIDADES_DIEZ[unidad]
        elif numero == 20:
            resultado = 'veinte'
        elif numero <= 29:
            resultado = 'veinti{}'.format(self.UNIDADES[unidad])
        else:
            resultado = self.DECENAS[decena]
            if unidad > 0:
                resultado = '{} y {}'.format(resultado, self.UNIDADES[unidad])
        return resultado

    def leer_centenas(self, numero):
        centena, decena = divmod(numero, 100)
        if decena == 0 and centena == 1:
            resultado = 'cien'
        else:
            resultado = self.CIENTOS[centena]
            if decena > 0:
                resultado = '{} {}'.format(resultado, self.leer_decenas(decena))
        return resultado

    def leer_miles(self, numero):
        millar, centena = divmod(numero, 1000)
        resultado = ''
        if (millar == 1):
            resultado = ''
        if (millar >= 2) and (millar <= 9):
            resultado = self.UNIDADES[millar]
        elif (millar >= 10) and (millar <= 99):
            resultado = self.leer_decenas(millar)
        elif (millar >= 100) and (millar <= 999):
            resultado = self.leer_centenas(millar)
        resultado = '{} mil'.format(resultado)
        if centena > 0:
            resultado = '{} {}'.format(resultado, self.leer_centenas(centena))
        return resultado

    def leer_millones(self, numero):
        millon, millar = divmod(numero, 1000000)
        resultado = ''
        if (millon == 1):
            resultado = ' un millon '
        if (millon >= 2) and (millon <= 9):
            resultado = self.UNIDADES[millon]
        elif (millon >= 10) and (millon <= 99):
            resultado = self.leer_decenas(millon)
        elif (millon >= 100) and (millon <= 999):
            resultado = self.leer_centenas(millon)
        if millon > 1:
            resultado = '{} millones'.format(resultado)
        if (millar > 0) and (millar <= 999):
            resultado = '{} {}'.format(resultado, self.leer_centenas(millar))
        elif (millar >= 1000) and (millar <= 999999):
            resultado = '{} {}'.format(resultado, self.leer_miles(millar))
        return resultado

    def leer_millardos(self, numero):
        millardo, millon = divmod(numero, 1000000)
        return '{} millones {}'.format(self.leer_miles(millardo), self.leer_millones(millon))