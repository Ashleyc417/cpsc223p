from bank_exceptions import *

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative: $-200")
        else:
            self.balance += amount
            return(f"${'{:.2f}'.format(amount)} deposited successfully. New balance: ${'{:.2f}'.format(self.balance)}")

    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds. You tried to withdraw $2000, but your balance is only $1000.")
        elif amount < 0:
            raise NegativeAmountError("Amount cannot be negative: $-200")
        else:
            self.balance -= amount
            
            return(f"${'{:.2f}'.format(amount)} withdrawn successfully. New balance: ${'{:.2f}'.format(self.balance)}")

    def get_balance(self):
        return(f"Account balance for {self.account_holder}: ${'{:.2f}'.format(self.balance)}")

