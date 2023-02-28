from user import User

class Bank:

    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__user = []

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def add_user(self, user: User):
        (self.__user).append(user.getID())

    def deposit(self, user: User, money):

        if user.getID() not in self.__user:
            print("This user not in Bank.")
            
        elif user.getAmount() < money:
            print("Insufficient funds")

        else:
            user.setAmount(user.getAmount() - money)
            self.__amount += money

    def withdrow(self, user: User, money):
        if user.getID() not in self.__user:
            print("This user not in Bank.")

        elif self.__amount < money:
            print("The bank is bankrupt")

        else:
            self.__amount -= money
            user.setAmount(user.getAmount() + money)

    def __str__(self) -> str:
        return f"{self.__name, self.__amount}"