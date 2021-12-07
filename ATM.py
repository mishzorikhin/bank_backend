import Transaction
from CashDispenser import CashDispenser


class ATM:

    def __init__(self, ATM_ID):
        self.ATM_ID = ATM_ID

    def display_ATM(self):
        print("ATM_ID : ", self.ATM_ID)

        #  Зачисление денежных средств

    def crediting_funds(self, Customer, balance):
        if balance > 0:
            newTransaction = Transaction.Transaction(Customer, Customer, balance, self.ATM_ID)
            newTransaction.StartTransaction()
            Customer.CurAcc.addTransaction(newTransaction)
            if newTransaction.state == -1:
                print(False)
        else:
            print(False)

    # снятие денежных средств
    def withdrawal_funds(self, Customer, balance):
        if balance < 0:
            newTransaction = Transaction.Transaction(Customer, Customer, balance, self.ATM_ID)
            newTransaction.StartTransaction()
            Customer.CurAcc.addTransaction(newTransaction)
            if newTransaction.state == -1:
                print("state = -1")

        else:
            print(False)

    # перевод другому лицу
    def transfer_another(self, Customer1, Customer2, balance):
        if balance > 0:
            newTransaction = Transaction.Transaction(Customer1, Customer2, balance, self.ATM_ID)
            newTransaction.StartTransaction()
            Customer1.CurAcc.addTransaction(newTransaction)
            Customer2.CurAcc.addTransaction(newTransaction)
           # print(newTransaction)
            if newTransaction.state == -1:
                print(False)
        else:
            print(False)
