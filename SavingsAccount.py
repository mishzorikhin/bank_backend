import Acc


class SavingsAccount(Acc.Account):
    __interest_rate = 5

    def __repr__(self):
        return "\nБаланс сберегательного счета : " + str(self.Balance)

    def deposit_growth(self):
        self.Balance = self.Balance + self.Balance * self.__interest_rate / 100
