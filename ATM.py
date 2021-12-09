import Transaction


class ATM:

    def __init__(self, ATM_ID):
        self.ATM_ID = ATM_ID

    def __repr__(self):
        return "ATM_ID : " + str(self.ATM_ID)

    def display_transaction(self, Customer):
        return Customer.CurAcc.Transactions

        #  Зачисление денежных средств

    def crediting_funds(self, Customer, balance):
        if balance < 0:
            return -1
        newTransaction = Transaction.Transaction(Customer, Customer, balance, self.ATM_ID)
        newTransaction.start_transaction()
        Customer.CurAcc.add_transaction(newTransaction)
        if newTransaction.state == -1:
            return -1

    # снятие денежных средств
    def withdrawal_funds(self, Customer, balance):
        if balance > 0:
            return -1
        newTransaction = Transaction.Transaction(Customer, Customer, balance, self.ATM_ID)
        newTransaction.start_transaction()
        Customer.CurAcc.add_transaction(newTransaction)
        if newTransaction.state == -1:
            return -1

    # перевод другому лицу
    def transfer_another(self, Customer1, Customer2, balance):
        if balance < 0:
            return -1
        else:
            newTransaction = Transaction.Transaction(Customer1, Customer2, balance, self.ATM_ID)
            newTransaction.start_transaction()
            Customer1.CurAcc.add_transaction(newTransaction)
            Customer2.CurAcc.add_transaction(newTransaction)
            if newTransaction.state == -1:
                return -1

    def get_balance(self, Customer):
        return Customer.CurAcc, Customer.SavAcc
