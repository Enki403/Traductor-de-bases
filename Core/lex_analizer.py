# -*- coding: utf-8 -*-

import re

class LexAnalizer():
    """
        Esta clase recibe un arreglo y las analiza indice a indice
    """
    def __init__(self, text):
        
        self._text = text
        
        # ? Patrones
        # hex
        self.hex_ptrn = r'^(\d+)+(hex)$'
        # oct
        self.oct_ptrn = r'^(\d+)+(oct)$'
        # rom
        self.rom_ptrn = r'^(\d+)+(rom)$'
        # alt
        self.alt_ptrn = r'^(\d+)+(alt)$'
        # ran
        self.ran_ptrn = r'^(\d+)+(ran)$'
        # cadena vacia
        self.vacia_ptrn = r'^$'

    def tokenizar(self):
        """
            Crea la tabla de tokens
        """
        data = []

        for idx, item in enumerate(self._text):
            if(re.match(self.hex_ptrn, item)):
                temp = re.match(self.hex_ptrn, item).groups()
                data.append([idx + 1, "Número entero", temp[0], "Identificador de Número"])
                data.append([idx + 1, "operador hex", temp[1], "Identificador de hexadecimal"])
            elif(re.match(self.oct_ptrn, item)):
                temp = re.match(self.oct_ptrn, item).groups()
                data.append([idx + 1, "Número entero", temp[0], "Identificador de Número"])
                data.append([idx + 1, "operador oct", temp[1], "Identificador de octal"])
            elif(re.match(self.ran_ptrn, item)):
                temp = re.match(self.ran_ptrn, item).groups()
                data.append([idx + 1, "Número entero", temp[0], "Identificador de Número"])
                data.append([idx + 1, "operador ran", temp[1], "Identificador de aleatorio"])
            elif(re.match(self.rom_ptrn, item)):
                temp = re.match(self.rom_ptrn, item).groups()
                data.append([idx + 1, "Número entero", temp[0], "Identificador de Número"])
                data.append([idx + 1, "operador rom", temp[1], "Identificador de romano"])
            elif(re.match(self.alt_ptrn, item)):
                temp = re.match(self.alt_ptrn, item).groups()
                data.append([idx + 1, "Número entero", temp[0], "Identificador de Número"])
                data.append([idx + 1, "operador alt", temp[1], "Identificador de alternativo"])
            elif(re.match(self.vacia_ptrn, item)):
                data.append([idx + 1, "Vacio", item, "Linea vacia, se omite"])
            else:
                data.append([idx + 1, "Error", item, "Error en linea {}".format(idx + 1)])
                #break

        return data