import uuid
from datetime import datetime


def get_balance(customer):
    return customer.CurAcc.Balance


class Transaction:

    def __init__(self, customer1, customer2, amount, acc, ATM_ID):
        self.data = datetime.today()
        self.transactionID = str(uuid.uuid4().fields[-1])[:8]
        self.customer1 = customer1  # клиент 1 отправитель
        self.customer2 = customer2  # клиент 2 принимающий
        self.amount = amount  # сумма
        self.state = 0  # 0 - не завершенная -1 - отклонена 1 - завершена
        self.ATM_ID = ATM_ID
        self.acc = acc # 0 - CurAcc 1 - SavAcc


        if customer1 == customer2:
            self.type = 0  # взоимодейсвие с банкоматом
        else:
            self.type = 1  # взоимодейсвие между клиентами

    def start_transaction(self):
        if self.type == 1:

            if get_balance(self.customer1) < self.amount:
                self.end_transaction(-1)
                # баланс отправителя меньше суммы перевода
            else:
                # перевод стредств от customer1 - customer2
                self.customer1.CurAcc.edit_balance(self.amount * (-1))
                self.customer2.CurAcc.edit_balance(self.amount)
                self.end_transaction(1)

        else:

            if self.amount <= 0:
                # снятие с баланса
                if get_balance(self.customer1) > 0:
                    if self.acc == 0:
                        self.customer1.CurAcc.edit_balance(self.amount)
                    else:
                        self.customer1.SavAcc.edit_balance(self.amount)
                    self.end_transaction(1)
                else:
                    # если сумма снятия больше баланса
                    self.end_transaction(-1)

            else:

                # пополнение баланса
                if self.acc == 1:
                    self.customer1.SavAcc.edit_balance(self.amount)
                    self.customer1.CurAcc.edit_balance((self.amount*-1))
                else:
                    self.customer1.CurAcc.edit_balance(self.amount)
                self.end_transaction(1)

    def end_transaction(self, state):
        self.state = state

    def __repr__(self):
        return "\nID транзакции : " + str(self.transactionID) + \
               "\nоправитель : " + str(self.customer1.CustomerName) + \
               "\nполучатель : " + str(self.customer2.CustomerName) + \
               "\nсумма : " + str(self.amount) + \
               "\nстатус : " + str(self.state) + \
               "\nдата : " + str(self.data) + \
               "\nId банкомата : " + str(self.ATM_ID) + \
               "\n"
