class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance!")
acc = BankAccount()
acc.deposit(1000)
acc.withdraw(400)
print("Balance:", acc.balance)
