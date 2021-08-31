from datetime import datetime
import Account


class Transaction(Account):
    __date = datetime
    __amount = 0
    __deposit = " "
    state = 0 #




    def StartTransaction(self):

        #customer1.
        #customer2.

        if Account.Balanse <= self.__deposit:
            self.state = True
            return self.__date, self.state

        else:
            self.state = False
            return self.state

    def GetAccountBalance(self):
        return Account.Balanse

    def CancelTransaction(self):
        if self.state == 1:
            print("Транзакция отменена! ")
        return self.state
        if self.state == -1:
            print("Транзакцию отменить невозможно! ")
