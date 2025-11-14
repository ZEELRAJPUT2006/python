class insufficientbalanceException(Exception):
    def __init__(self, msg):
        super().__init__(msg)





class bank:
    balance = 0

    def check_balance(self):
        print("your current balance is :", self.balance)

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            # print("insufficient balance")
            raise insufficientbalanceException(f"you need more {amt-self.balance} in your account")
        else:
            self.balance-amt



b = bank()
b.check_balance()
b.deposit(5000)
b.deposit(7000)
b.check_balance()
try:
    b.withdraw(20000)
except Exception as e:
    print(e)

b.check_balance()