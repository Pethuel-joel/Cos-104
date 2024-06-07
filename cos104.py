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
