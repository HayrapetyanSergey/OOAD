from datetime import datetime

class Cell:

    COLORS = {'red':1, 'green':2, 'blue':3}

    def __init__(self, value = "", color = "white"):
        self.__value = value
        self.__color = color

    def getValue(self):
        return self.__value
    
    def getColor(self):
        return self.__color

    def setValue(self, new_value):
        self.__value = new_value
    
    def setColor(self, new_color):
        if new_color not in Cell.COLORS:
            raise ValueError('Cell doesn\'t support such color.')
        self.__value = new_color

    def toInt(self):
        return int(self.__value)

    def toDouble(self):
        return float(self.__value)

    def toDate(self):
        return datetime.strptime(self.__value, '%d/%m/%Y')

    def reset(self):
        self.__value = ""