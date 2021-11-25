# import CashDispenser
# import Transaction
import BankCustomer


class Account():

    # __trans = Transaction.Transaction

    def __init__(self, Balanse):
        self.Balanse = Balanse

    def top_up_balance(self, cash):
        self.Balanse = + cash

    def withdraw_from_balance(self, cash):
        self.Balanse = - cash

    def CalculateInterest(self, cash):
        pass

    def UpdateAccount(self):
        pass

    def VentyWithdrawAmount(self):
        pass
