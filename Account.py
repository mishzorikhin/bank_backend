# import CashDispenser
# import Transaction
import BankCustomer
import Transaction


class Account():

    def __init__(self, Balanse):
        self.Balanse = Balanse
        self.__trans = []

    def top_up_balance(self, cash):
        self.Balanse = self.Balanse + cash



    def withdraw_from_balance(self, cash):
        if self.Balanse >= cash:
            self.Balanse = self.Balanse - cash

        else:
            return None

    def CalculateInterest(self, cash):
        pass

    def UpdateAccount(self):
        pass

    def VentyWithdrawAmount(self):
        pass
