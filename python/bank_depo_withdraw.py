class bankaccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Rs.",amount,"was debited")
        else:
            print("insufficient balance...!")
    def get_balance(self):
        return self.balance
a = bankaccount()
a.deposit(1000)
a.withdraw(500)
print("balance:",a.get_balance())

