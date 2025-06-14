class BankAccount:

    def __init__(self, account_number,initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance > 0:
            return True
        elif self.balance < 0:
            return False

    def display_balance(self):
        return f'Current Balance: {self.balance}'