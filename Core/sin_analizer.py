# -*- coding: utf-8 -*-

import re
import random
from Core.auxiliar import Auxiliar

class SinAnalizer():
    """
        Esta clase recibe un arreglo y las analiza indice a indice
    """
    def __init__(self, text = None):
        
        self._text = text

        self.arbol = []

        # Para imprimir en consola
        self.debug = False
        
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

    def setText(self, text):
        self._text = text

    def analizar(self):
        """
            Analiza la entrada para resolver
        """
        self.lr1()
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
                data.append([item, self.spc_translate()])
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
    
    def spc_translate(self):
        """
            Devuelve un espacio vacio
        """
        return "Entrada es una linea vacia"

    def err_translate(self):
        """
            Devuelve el un error
            TODO: Se podria mejorar de alguna forma ?
        """
        return "Operacion no valida"

    def lr1(self):
        """
            analisis sintactico LR(1)
        """
        separator_ptrn = r'(\d+)(hex|oct|rom|alt|ran)(\$)'

        for cadena in (self._text):
            cadena = cadena+"$"
            tokens = None
            try:
                if re.match(separator_ptrn, cadena):
                    tokens = list(re.match(separator_ptrn, cadena).groups())

                    if self._lr1(tokens):
                        if(self.debug):
                            print(cadena[:-1])
                else:
                    if(re.match(self.vacia_ptrn, cadena[:-1])):
                        if(self.debug):
                            print(self.spc_translate())
                    else:
                        if(self.debug):
                            print(self.err_translate())
                
            except Exception as e:
                print(e)
        
        
        pila = list([0])

    def _lr1(self, tokens):
        """
            Funcion auxiliar para analisis sintactico LR(1)
        """
        self.pila_estado = list([0])
        self.pila_simbolo = list([''])
        tokens.reverse()

        if self.debug:
            print("================================================================")

        while(tokens):
            if self.debug:
                print("========== {} ===========)".format(tokens[-1]))
                print("self._tablaqry({}, {}, {})".format(self.pila_estado[-1], self.pila_simbolo[-1], tokens[-1]))
                print("self.pila_estado: {}".format(self.pila_estado))
                print("self.pila_simbolo: {}".format(self.pila_simbolo))
            self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], tokens.pop())

        self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], '$')
        if self.debug:
            print("========== {} ===========)".format("$"))
            print("self._tablaqry({}, {}, {})".format(self.pila_estado[-1], self.pila_simbolo[-1], "$"))
            print("self.pila_estado: {}".format(self.pila_estado))
            print("self.pila_simbolo: {}".format(self.pila_simbolo))

            print("================================================================")

        if self.pila_estado[-1] == 0 and self.pila_simbolo[-1] == 'S':
            return True
        else:
            return False

    def _tablaqry(self, state, simbolo, beta):
        """
            Retorna la accion a utilizar
        """
        """
            +-------+--------+-----+-----+-----+-----+-----+-----+---+---+---+---+---+---+
            | state | numero | hex | oct | rom | alt | ran |  $  | S | A | B | C | D | E |
            +-------+--------+-----+-----+-----+-----+-----+-----+---+---+---+---+---+---+
            |   0   |   s7   |     |     |     |     |     |     | 1 | 2 | 3 | 4 | 5 | 6 |
            |   1   |        |     |     |     |     |     | acc |   |   |   |   |   |   |
            |   2   |        |     |     |     |     |     |  r1 |   |   |   |   |   |   |
            |   3   |        |     |     |     |     |     |  r2 |   |   |   |   |   |   |
            |   4   |        |     |     |     |     |     |  r3 |   |   |   |   |   |   |
            |   5   |        |     |     |     |     |     |  r4 |   |   |   |   |   |   |
            |   6   |        |     |     |     |     |     |  r5 |   |   |   |   |   |   |
            |   7   |        |  s8 |  s9 | s10 | s11 | s12 |     |   |   |   |   |   |   |
            |   8   |        |     |     |     |     |     |  r6 |   |   |   |   |   |   |
            |   9   |        |     |     |     |     |     |  r7 |   |   |   |   |   |   |
            |   10  |        |     |     |     |     |     |  r8 |   |   |   |   |   |   |
            |   11  |        |     |     |     |     |     |  r9 |   |   |   |   |   |   |
            |   12  |        |     |     |     |     |     | r10 |   |   |   |   |   |   |
            +-------+--------+-----+-----+-----+-----+-----+-----+---+---+---+---+---+---+
        """
        # ? terminales
        numero_ptrn = r'\d+'
        hex_ptrn = r'^hex$'
        oct_ptrn = r'^oct$'
        rom_ptrn = r'^rom$'
        alt_ptrn = r'^alt$'
        ran_ptrn = r'^ran$'
        s_ptrn = r'^S$'
        a_ptrn = r'^A$'
        b_ptrn = r'^B$'
        c_ptrn = r'^C$'
        d_ptrn = r'^D$'
        e_ptrn = r'^E$'
        end_ptrn = r'\$'

        if state == 0:
            if re.match(numero_ptrn, beta):
                self.createNode('hoja', beta)
                self.pila_estado.append(7)
                self.pila_simbolo.append(beta)
                return
            elif re.match(s_ptrn, simbolo):
                self.pila_estado.append(1)
                self.createNode('raiz', simbolo, [self.arbol.pop(), self.arbol.pop()])
                return
            elif re.match(a_ptrn, simbolo):
                self.pila_estado.append(2)
                self.createNode('raiz', simbolo, [self.arbol.pop(), self.arbol.pop()])
                return
            elif re.match(b_ptrn, simbolo):
                self.pila_estado.append(3)
                self.createNode('raiz', simbolo, [self.arbol.pop(), self.arbol.pop()])
                return
            elif re.match(c_ptrn, simbolo):
                self.pila_estado.append(4)
                self.createNode('raiz', simbolo, [self.arbol.pop(), self.arbol.pop()])
                return
            elif re.match(d_ptrn, simbolo):
                self.pila_estado.append(5)
                self.createNode('raiz', simbolo, [self.arbol.pop(), self.arbol.pop()])
                return
            elif re.match(e_ptrn, simbolo):
                self.pila_estado.append(6)
                self.createNode('raiz', simbolo, [self.arbol.pop(), self.arbol.pop()])
                return
        elif state == 1:
            if re.match(end_ptrn, beta):
                if (self.debug):
                    print("accept")
                return
        elif state == 2:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self._reduce(1)
                return
        elif state == 3:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self._reduce(2)
                return
        elif state == 4:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self._reduce(3)
                return
        elif state == 5:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self._reduce(4)
                return
        elif state == 6:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self._reduce(5)
                return
        elif state == 7:
            if re.match(hex_ptrn, beta):
                self.createNode('hoja', beta)
                self.pila_estado.append(8)
                self.pila_simbolo.append(beta)
                return
            elif re.match(oct_ptrn, beta):
                self.createNode('hoja', beta)
                self.pila_estado.append(9)
                self.pila_simbolo.append(beta)
                return
            elif re.match(rom_ptrn, beta):
                self.createNode('hoja', beta)
                self.pila_estado.append(10)
                self.pila_simbolo.append(beta)
                return
            elif re.match(alt_ptrn, beta):
                self.createNode('hoja', beta)
                self.pila_estado.append(11)
                self.pila_simbolo.append(beta)
                return
            elif re.match(ran_ptrn, beta):
                self.createNode('hoja', beta)
                self.pila_estado.append(12)
                self.pila_simbolo.append(beta)
                return
        elif state == 8:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self.pila_simbolo.pop()
                self._reduce(6)
                return
        elif state == 9:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self.pila_simbolo.pop()
                self._reduce(7)
                return
        elif state == 10:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self.pila_simbolo.pop()
                self._reduce(8)
                return
        elif state == 11:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self.pila_simbolo.pop()
                self._reduce(9)
                return
        elif state == 12:
            if re.match(end_ptrn, beta):
                self.pila_simbolo.pop()
                self.pila_simbolo.pop()
                self._reduce(9)
                return
        if (self.debug):
            print("rechazar")
        return

    def _reduce(self, regla):
        """
            Reduce segun regla especificada
        """
        """
             1. S -> A
             2. S -> B
             3. S -> C
             4. S -> D
             5. S -> E
             6. A -> numero hex
             7. B -> numero oct
             8. C -> numero rom
             9. D -> numero alt
            10. E -> numero ran
        """

        if (regla == 1 or regla == 2 or regla == 3 or regla == 4 or regla == 5):
            self.pila_simbolo.append("S")
            self.createNode('raiz', self.pila_simbolo[-1], self.arbol.pop())
            self.pila_estado.pop()
        elif regla == 6:
            self.pila_simbolo.append("A")
            self.pila_estado.pop()
            self.pila_estado.pop()
            self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], '')
        elif regla == 7:
            self.pila_simbolo.append("B")
            self.pila_estado.pop()
            self.pila_estado.pop()
            self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], '')
        elif regla == 8:
            self.pila_simbolo.append("C")
            self.pila_estado.pop()
            self.pila_estado.pop()
            self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], '')
        elif regla == 9:
            self.pila_simbolo.append("D")
            self.pila_estado.pop()
            self.pila_estado.pop()
            self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], '')
        elif regla == 10:
            self.pila_simbolo.append("E")
            self.pila_estado.pop()
            self.pila_estado.pop()
            self._tablaqry(self.pila_estado[-1], self.pila_simbolo[-1], '')

    def createNode(self, tipo, valor, hijo = None):
        """
            Crea el arbol
        """
        self.arbol.append([tipo, valor, hijo])

    def get_formated_tree(self):
        """
            Retorna el arbol con formato (json)
        """
        formated_tree = {'name': 'Analisis', 'children': [self._format(child) for child in self.arbol]}
        if (self.debug):
            print("============== arbol ============")
        return formated_tree

    def _format(self, arreglo):
        """
            Funcion auxiliar para dar formato al arreglo
            returna dictionario en forma de arbol
        """
        if(arreglo):
            if arreglo[0] == 'hoja' or arreglo[0] == 'raiz':
                res = {'name':arreglo[1]}
                hijos = self._format([child for child in arreglo[2]])
                if (self.debug):
                    print("=======typo: {}  hijos: {}". format(type(hijos),hijos))
                if isinstance(hijos, list):
                    res['children'] = hijos
                elif isinstance(hijos, dict):
                    res['children'] = [hijos]
                return res
            else:
                return [{'name':child[1]} for child in arreglo]

