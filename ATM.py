import Transaction


class ATM:

    def __init__(self, ATM_ID):
        self.ATM_ID = ATM_ID

    def __repr__(self):
        return "ATM_ID : " + str(self.ATM_ID)

    def display_transaction(self, Customer):
        return Customer.CurAcc.Transactions

    def crediting_funds(self, Customer, balance):
        if balance < 0:
            return -1
        newTransaction = Transaction.Transaction(Customer, Customer, balance, 0, self.ATM_ID) # 0 - CurAcc
        newTransaction.start_transaction()
        Customer.CurAcc.add_transaction(newTransaction)
        if newTransaction.state == -1:
            return -1

    # снятие денежных средств
    def withdrawal_funds(self, Customer, balance):
        if balance > 0:
            return -1
        newTransaction = Transaction.Transaction(Customer, Customer, balance, 0, self.ATM_ID) # 0 - CurAcc
        newTransaction.start_transaction()
        Customer.CurAcc.add_transaction(newTransaction)
        if newTransaction.state == -1:
            return -1

    # перевод другому лицу
    def transfer_another(self, Customer1, Customer2, balance):
        if balance < 0:
            return -1
        else:
            newTransaction = Transaction.Transaction(Customer1, Customer2, balance, 0, self.ATM_ID) # 0 - CurAcc
            newTransaction.start_transaction()
            Customer1.CurAcc.add_transaction(newTransaction)
            Customer2.CurAcc.add_transaction(newTransaction)
            if newTransaction.state == -1:
                return -1


    def replenishment_savings_account(self, customer, balance):
        if balance < 0:
            return -1
        else:
            newTransaction = Transaction.Transaction(customer, balance, 1, self.ATM_ID)  # 1 - SavAcc
            newTransaction.start_transaction()
            customer.CurAcc.add_transaction(newTransaction)
            if newTransaction.state == -1:
                return -1



    def get_balance(self, Customer, type):
        if type == "CurAcc":
            return Customer.CurAcc

        if type ==  "SavAcc":
            return  Customer.SavAcc
