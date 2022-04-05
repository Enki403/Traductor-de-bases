# -*- coding: utf-8 -*-

import re
import random

class SinAnalizer():
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

    def analizar(self):
        """
            Analiza la entrada para resolver
        """

        data = []

        for item in self._text:
            if(re.match(self.hex_ptrn, item)):
                temp = re.match(self.hex_ptrn, item).groups()
                data.append([item, self.hex_translate(temp[0])])
            elif(re.match(self.oct_ptrn, item)):
                temp = re.match(self.oct_ptrn, item).groups()
                data.append([item, self.oct_translate(temp[0])])
            elif(re.match(self.ran_ptrn, item)):
                temp = re.match(self.ran_ptrn, item).groups()
                data.append([item, self.ran_translate(temp[0])])
            elif(re.match(self.rom_ptrn, item)):
                temp = re.match(self.rom_ptrn, item).groups()
                data.append([item, self.rom_translate(temp[0])])
            elif(re.match(self.alt_ptrn, item)):
                temp = re.match(self.alt_ptrn, item).groups()
                data.append([item, self.alt_translate(temp[0])])
            elif(re.match(self.vacia_ptrn, item)):
                data.append([item, item])
            else:
                data.append([item, self.err_translate()])
                #break

        return data


    def hex_translate(self, value):
        """
            Devuelve el valor de un entero en hexadecimal
        """
        return str(hex(int(value))[2:]) + " (hex)"

    def oct_translate(self, value):
        """
            Devuelve el valor de un entero en octal
        """
        return str(oct(int(value))[2:]) + " (oct)"

    def rom_translate(self, value):
        """
            Devuelve el valor de un entero en numeros romanos
            TODO: Escribir codigo para transformar de decimal a numeros romanos
        """
        return "{} rom".format(value)

    def alt_translate(self, value):
        """
            Devuelve el valor de un entero en alternativo (ver documentacion)
            TODO: Escribir codigo para transformar de decimal a alternativo y definir gramatica de alternativo
        """
        return "{} alt".format(value)

    def ran_translate(self, value):
        """
            Devuelve el valor de un entero a un valor aleatorio
        """
        opcion = random.randint(1,4)
        if(opcion == 1):
            return self.hex_translate(value)
        if(opcion == 2):
            return self.oct_translate(value)
        if(opcion == 3):
            return self.rom_translate(value)
        if(opcion == 4):
            return self.alt_translate(value)
    
    def spc_translate(self, value):
        """
            Devuelve un espacio vacio
        """
        return "{} ran".format(value)

    def err_translate(self):
        """
            Devuelve el un error
            TODO: Se podria mejorar de alguna forma ?
        """
        return "Operacion no valida"
    