class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def deposit(self, amount):
        self._balance += amount
        interest = 0.005 * amount
        self._balance += interest
        return self._balance

    def withdraw(self, amount):
        if amount <= 700000 and amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Withdrawal limit exceeded or insufficient balance"

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Insufficient balance"