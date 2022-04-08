# Proyecto de Diseño de Compiladores

## Integrantes: 
- Alexis Ochoa
- Hector Vasquez
- Jose Barrientos
- Josue Caballero
- Melissa Diaz
- Nora Rodriguez

## Descripción
El objetivo de este programa es implementar un analizador léxico y uno sintáctico, de modo que a partir de una entrada de números (base 10) pueda obtenerse una salida convirtiendo a distintas bases y a su vez mostrarse los tokens, el resultado y el árbol.

<table border="1">
    <tr>
        <td>
            <p align="center"><span>Operador</span> </p>
        </td>
        <td>
            <p align="center"><span>Ejemplo</span> </p>
        </td>
        <td>
            <p align="center"><span>Resultado</span> </p>
        </td>
        <td>
            <p align="center"><span>Descripción</span> </p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center"><span>hex</span> </p>
        </td>
        <td>
            <p align="center"><span>403hex</span> </p>
        </td>
        <td>
            <p align="center"><span>193 (hex)</span> </p>
        </td>
        <td>
            <p align="center"><span>Convierte a hexadecimal</span> </p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center"><span>oct</span> </p>
        </td>
        <td>
            <p align="center"><span>403oct</span> </p>
        </td>
        <td>
            <p align="center"><span>623 (hex)</span> </p>
        </td>
        <td>
            <p align="center"><span>Convierte a octal</span> </p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center"><span>rom</span> </p>
        </td>
        <td>
            <p align="center"><span>403rom</span> </p>
        </td>
        <td>
            <p align="center"><span>CDIII</span> </p>
        </td>
        <td>
            <p align="center"><span>Convierte a números romanos</span> </p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center"><span>alt</span> </p>
        </td>
        <td>
            <p align="center"><span>403alt</span> </p>
        </td>
        <td>
            <p align="center"><span>cuatrocientos tres</span></p>
        </td>
        <td>
            <p align="center"><span>Convierte a números verbales</span></p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center"><span>ran</span> </p>
        </td>
        <td>
            <p align="center"><span>403ran</span> </p>
        </td>
        <td>
            <p align="center"> <span>CDIII</span></p>
        </td>
        <td>
            <p align="center"><span>Convierte a cualquiera de las anteriores de manera aleatoria</span> </p>
        </td>
    </tr>
</table>

## Instalación

### Dev

Se utilizó [python 3.10](https://www.python.org/downloads/release/python-3100/) para desarrollarse. Ver [requirements.txt](requirements.txt) para ver las dependencias de paquetes.
Para instalar las dependencias se puede utilizar `pip install -r requirements.txt`.

### Prerrequisitos

* **PyQt5==5.15.6** para el desarrollo del GUI

## Uso

Se provee el script [main.py](main.py), el cual implementa la interfaz gráfica.

## License

[MIT](https://mit-license.org/)