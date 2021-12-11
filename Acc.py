class Account:

    def __init__(self, Balance):
        self.Balance = Balance
        self.Transactions = []

    def edit_balance(self, cash):
        self.Balance = self.Balance + cash

    def add_transaction(self, Transaction):
        self.Transactions.append(Transaction)

