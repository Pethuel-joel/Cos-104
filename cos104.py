from abc import ABC, abstractmethod

class BankAccount(ABC):
    def _init_(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def get_account_info(self):
        return {
            'account_number': self._account_number,
            'account_name': self._account_name,
            'balance': self._balance
        }

class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_name, balance=0):
        super()._init_(account_number, account_name, balance)

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
    def _init_(self, account_number, account_name, balance=0):
        super()._init_(account_number, account_name, balance)

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Insufficient balance"

class ChildrensAccount(BankAccount):
    def _init_(self, account_number, account_name, balance=0):
        super()._init_(account_number, account_name, balance)

    def deposit(self, amount):
        self._balance += amount
        interest = 0.007 * amount
        self._balance += interest
        return self._balance

    def withdraw(self, amount):
        return "Withdrawals not allowed"

class StudentAccount(BankAccount):
    def _init_(self, account_number, account_name, balance=0):
        super()._init_(account_number, account_name, balance)

    def deposit(self, amount):
        if amount <= 50000:
            self._balance += amount
            return self._balance
        else:
            return "Deposit limit exceeded"

    def withdraw(self, amount):
        if amount <= 2000 and amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Withdrawal limit exceeded or insufficient balance"

# Test the implementation
if _name_ == "_main_":
    savings_account = SavingsAccount("001", "John Doe")
    current_account = CurrentAccount("002", "Jane Smith")
    childrens_account = ChildrensAccount("003", "Baby Johnson")
    student_account = StudentAccount("004", "Student Lee")

    print(savings_account.deposit(1000))  # 1000 + 5 = 1005
    print(savings_account.withdraw(500))  # 1005 - 500 = 505

    print(current_account.deposit(500))  # 500
    print(current_account.withdraw(200))  # 500 - 200 = 300

    print(childrens_account.deposit(500))  # 500 + 3.5 = 503.5
    print(childrens_account.withdraw(100))  # "Withdrawals not allowed"

    print(student_account.deposit(500))  # 500
    print(student_account.withdraw(100))  # 500 - 100 = 400
    print(student_account.deposit(60000))  # "Deposit limit exceeded"