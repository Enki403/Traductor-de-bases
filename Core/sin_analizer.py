# -*- coding: utf-8 -*-

import re
import random

from Core.auxiliar import Auxiliar

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
        """
        value = int(value)
        literals = [(1000,  'M'), (900,  'CM'), (500,  'D'), (400,  'CD'),
                    (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
                    (10,  'X'), (9,  'IX'), (5,  'V'), (4,  'IV'), (1,  'I')]
        result = []
        for numero, literal in literals:
            aux = value // numero
            result.extend([literal] * aux)
            value -= aux * numero
        return "".join(result)

    def alt_translate(self, value):
        """
            Devuelve el valor de un entero en formato verbal
        """
        numero_entero = int(value)
        value = int(value)
        MAX_NUMERO = 999999999999
        Aux = Auxiliar()

        if numero_entero > MAX_NUMERO:
            return 'Número demasiado alto'
        if numero_entero < 0:
            return 'menos {}'.format(self.alt_translate(abs(value)))
        letras_decimal = ''
        parte_decimal = int(round((abs(value) - abs(numero_entero)) * 100))
        if parte_decimal > 9:
            letras_decimal = 'punto {}'.format(self.alt_translate(parte_decimal))
        elif parte_decimal > 0:
            letras_decimal = 'punto cero {}'.format(self.alt_translate(parte_decimal))
        if (numero_entero <= 99):
            resultado = Aux.leer_decenas(numero_entero)
        elif (numero_entero <= 999):
            resultado = Aux.leer_centenas(numero_entero)
        elif (numero_entero <= 999999):
            resultado = Aux.leer_miles(numero_entero)
        elif (numero_entero <= 999999999):
            resultado = Aux.leer_millones(numero_entero)
        else:
            resultado = Aux.leer_millardos(numero_entero)
        
        resultado = resultado.replace('uno mil', 'un mil')
        resultado = resultado.strip()
        resultado = resultado.replace(' _ ', ' ')
        resultado = resultado.replace('  ', ' ')
        
        if parte_decimal > 0:
            resultado = '{} {}'.format(resultado, letras_decimal)
        
        return resultado

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
