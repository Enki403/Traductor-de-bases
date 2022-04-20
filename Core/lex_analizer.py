# -*- coding: utf-8 -*-

import re

class LexAnalizer():
    """
        Esta clase recibe un arreglo y las analiza indice a indice
    """
    def __init__(self, text):
        
        self._text = text
        self.data = []

        """ # ? Patrones
        # entero
        self.int_ptrn = r'(\d+)'
        # hex
        self.hex_ptrn = r'(?<=(?:\d)|(?:x)|(?:t)|(?:m)|(?:n))(hex+)(?=(?:hex)|(?:oct)|(?:rom)|(?:alt)|(?:ran)|(?:\Z)|(?:\s))'
        # oct
        self.oct_ptrn = r'(?<=(?:\d)|(?:x)|(?:t)|(?:m)|(?:n))(oct+)(?=(?:hex)|(?:oct)|(?:rom)|(?:alt)|(?:ran)|(?:\Z)|(?:\s))'
        # rom
        self.rom_ptrn = r'(?<=(?:\d)|(?:x)|(?:t)|(?:m)|(?:n))(rom+)(?=(?:hex)|(?:oct)|(?:rom)|(?:alt)|(?:ran)|(?:\Z)|(?:\s))'
        # alt
        self.alt_ptrn = r'(?<=(?:\d)|(?:x)|(?:t)|(?:m)|(?:n))(alt+)(?=(?:hex)|(?:oct)|(?:rom)|(?:alt)|(?:ran)|(?:\Z)|(?:\s))'
        # ran
        self.ran_ptrn = r'(?<=(?:\d)|(?:x)|(?:t)|(?:m)|(?:n))(ran+)(?=(?:hex)|(?:oct)|(?:rom)|(?:alt)|(?:ran)|(?:\Z)|(?:\s))'
        # cadena vacia
        self.vacia_ptrn = r'^$' """
        
        # ? Patrones
        # entero
        self.int_ptrn = r'(\d+)'
        # hex
        self.hex_ptrn = r'(hex)'
        # oct
        self.oct_ptrn = r'(oct)'
        # rom
        self.rom_ptrn = r'(rom)'
        # alt
        self.alt_ptrn = r'(alt)'
        # ran
        self.ran_ptrn = r'(ran)'
        # cadena vacia
        self.vacia_ptrn = r'^$'

    def tokenizar(self):
        """
            Crea la tabla de tokens y retorna un arreglo conteniendo la informacion de tokens por linea
        """
        
        for idx, item in enumerate(self._text):
            flag = True
            item = item.lower()
            if(re.search(self.int_ptrn, item)):
                temp = re.findall(self.int_ptrn, item)
                for element in temp:
                    self.add_to_data(idx+1, "Número entero", element, "Identificador de número entero")
            if(re.search(self.hex_ptrn, item)):
                flag = False
                temp = re.findall(self.hex_ptrn, item)
                for element in temp:
                    self.add_to_data(idx + 1, "operador hex", element, "Identificador de hexadecimal")
            if(re.search(self.oct_ptrn, item)):
                flag = False
                temp = re.findall(self.oct_ptrn, item)
                for element in temp:
                    self.add_to_data(idx + 1, "operador oct", element, "Identificador de octal")
            if(re.search(self.ran_ptrn, item)):
                flag = False
                temp = re.findall(self.ran_ptrn, item)
                for element in temp:
                    self.add_to_data(idx + 1, "operador ran", element, "Identificador de aleatorio")
            if(re.search(self.rom_ptrn, item)):
                flag = False
                temp = re.findall(self.rom_ptrn, item)
                for element in temp:
                    self.add_to_data(idx + 1, "operador rom", element, "Identificador de romano")
            if(re.search(self.alt_ptrn, item)):
                flag = False
                temp = re.findall(self.alt_ptrn, item)
                for element in temp:
                    self.add_to_data(idx + 1, "operador alt", element, "Identificador de alternativo")
            if(re.search(self.vacia_ptrn, item)):
                flag = False
                temp = re.findall(self.vacia_ptrn, item)
                for element in temp:
                    self.add_to_data(idx + 1, "Vacio", item, "Linea vacia, se omite")
            if flag:
                self.add_to_data(idx + 1, "Error", item, "Error en linea {} lexema desconocido".format(idx + 1))

        return self.data

    def add_to_data(self, idx, type, value, description):
        self.data.append([idx, type, value, description])