from bank import Bank
from user import User

u = User("Mariam", 18, 54845, 2000)
b = Bank("Sa", 800000)
b.add_user(u)
print(u)
print(b)
b.deposit(u, 1000)
print(u)
print(b)
b.withdrow(u, 3000)
print(u)
print(b)