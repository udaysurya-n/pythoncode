class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance-amount >= self.min_balance:
            self.balance -= amount
        else:
            print("sorry, insufficient funds")

    def printstatement(self):
        print("Account balance:", self.balance)


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=- 5000)

    def __str__(self):
        return "{}'s Current Account with Balance :{}" .format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings account with Balance :{}" .format(self.name, self.balance)

c=Savings('surya',10000)
print(c)
c.deposit(5000)
c.printstatement()
c.withdraw(16000)
c.withdraw(15000)
print(c)

c1=Current('uday',20000)
c1.deposit(5000)
print(c1)
c1.withdraw(27000)
print(c1)