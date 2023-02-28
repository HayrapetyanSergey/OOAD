from cell import Cell

class Sheet:
    def __init__(self, row, column):
        self.__matrix = [[Cell() for i in range(column)] for k in range(row)]

    def getCellAt(self, row, column):
        return self.__matrix[row][column]

    def setCellAt(self, row, column, value):
        self.__matrix[row][column].setValue(value)
    
    def addRow(self, row_index):
        self.__matrix.insert(row_index, [Cell() for i in range(self.__column)])

    def removeRow(self, row_index):
        del self.data[row_index]

    def addColumn(self, column_index):
        for i in range(self.__row):
            self.__matrix[i].insert(column_index, Cell())

    def removeColumn(self, column_index):
        for i in range(self.__row):
            self.__matrix[i].pop(column_index)

    def swapRows(self, row1, row2):
        self.__matrix[row1], self.__matrix[row2] = self.__matrix[row2], self.__matrix[row1]

    def swapColumns(self, column1, column2):
        for i in range(self.__row):
            self.__matrix[i][column1], self.__matrix[i][column2] = self.__matrix[i][column2], self.__matrix[i][column1]


    