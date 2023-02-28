class User:
    def __init__(self, name: str, age: int, ID: int, amount: float):
        self.__name = name
        self.__age = age
        self.__ID = ID
        self.__amount = amount

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getID(self):
        return self.__ID

    def getAmount(self):
        return self.__amount
    
    def setAmount(self, amount):
        self.__amount = amount
        
    def __str__(self) -> str:
        return f"{self.__name, self.__age, self.__ID, self.__amount}"