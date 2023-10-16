class BankAccount:
    def __init__(self, acc_number, balance, date_opening, customer_name):
        self.acc_number = acc_number
        self.balance = balance
        self.date_opening = date_opening
        self.customer_name = customer_name
    def deposit(self, money):
        self.balance = self.balance + money
    def withdraw(self, money):
        self.balance = self.balance - moneey
    def check_balance(self):
        print(f"Remaining money: {self.balance}")


a = BankAccount("123", 12, "12/2/2003", "Minh")
a.deposit(123)
a.check_balance()