from datetime import datetime
import Account


class Transaction():

    def __init__(self, customer1, customer2, amount):
        self.sender = customer1  # отправитель
        self.addressee = customer2  # получатель
        self.amount = amount #сумма
        self.type = 0  # 0 - снятие 1 - занесение
        self.state = 0  # 0 - не завершенная -1 - отклонена 1 - завершена
        self.data = datetime.today()


    def StartTransaction(self):
        #print(self.amount, self.sender.Acc.Balanse)
        self.addressee.Acc.top_up_balance(self.amount)
        self.state = 1


      #  if self.sender.Balanse <= self.amount:
      #      self.state = -1
      #      self.CompleteTransaction()
#
      #      return self.state
#
      #  else:
      #      self.addressee.top_up_balance(self.amount)



    def GetAccountBalance(self):
        pass

    def CompleteTransaction(self):
        pass



