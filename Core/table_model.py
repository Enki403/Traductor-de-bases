# -*- coding: utf-8 -*-
from PyQt5 import QtCore

class TableModel(QtCore.QAbstractTableModel):
    """
    Clase de modelo customizada
    """
    def __init__(self, data, columns):
        """
            data es un arreglo de arreglos
        """
        super(TableModel, self).__init__()
        self._data = data
        self._columns = columns

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # Tamaño de lista de listas
        return len(self._data)

    def columnCount(self, index):
        # Tamaño de la primera lista dentro de la lista
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._columns[section])
            
            if orientation == QtCore.Qt.Vertical:
                return str([idx + 1 for idx in range(self.rowCount(0))][section])