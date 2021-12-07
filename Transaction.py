from datetime import datetime
import Acc


class Transaction():

    def __init__(self, customer1, customer2, amount, ATM_ID):
        self.customer1 = customer1  # клиент 1 отправитель
        self.customer2 = customer2  # клиент 2 принимающий
        self.amount = amount  # сумма
        self.state = 0  # 0 - не завершенная -1 - отклонена 1 - завершена
        self.ATM_ID = ATM_ID

        if customer1 == customer2:
            self.type = 0  # взоимодейсвие с банкоматом
        else:
            self.type = 1  # взоимодейсвие между клиентами

    def GetBalance(self, customer):
        return customer.CurAcc.Balanse

    def StartTransaction(self):
        if self.type == 1:
            if self.GetBalance(self.customer1) < self.amount:
                self.EndTransaction(-1)
                # баланс отправителя меньше суммы перевода
            else:
                # перевод стредств от customer1 - customer2
                self.customer1.CurAcc.edit_balance(self.amount*(-1))
                self.customer2.CurAcc.edit_balance(self.amount)
                self.EndTransaction(1)

        else:
            if self.amount < 0:
                # снятие с баланса
                if self.GetBalance(self.customer1) > 0:
                    self.customer1.CurAcc.edit_balance(self.amount)
                    self.EndTransaction(1)
                else:
                    # если сумма снятия больше баланса
                    self.EndTransaction(-1)

            else:
                # пополнение баланса
                self.customer1.CurAcc.edit_balance(self.amount)
                self.EndTransaction(1)

    def EndTransaction(self, state):
        self.state = state
        self.data = datetime.today()

    def __repr__(self):
        return "customer1 " # + self.customer1  # + \
        #       " customer2 " + self.customer2 + \
        #    " amount " + str(self.amount) + \
        #    " state " + str(self.state) + \
        #    " ATM_ID " + str(self.ATM_ID) +\
        #    " type " + str(self.type)