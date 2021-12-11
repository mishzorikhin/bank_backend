import Acc


class CurrentAccount(Acc.Account):

    def __repr__(self):
        return str(self.Balance)
