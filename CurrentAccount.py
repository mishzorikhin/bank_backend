import Acc

class CurrentAccount(Acc.Account):

    def __repr__(self):
        return "\nБаланс текущего счета : " + str(self.Balance)
