import uuid
from ATMCard import ATMCard


class BankCustomer:

    def __init__(self, CustomerName, Address, Email):
        self.CustomerName = CustomerName
        self.__Address = Address
        self.__Email = Email
        self.__Card = ATMCard(str(uuid.uuid4().fields[-1])[:4], str(uuid.uuid4().fields[-1])[:6])
        self.CurAcc = self.__Card.CurAcc
        self.SavAcc = self.__Card.SavAcc

    def display_Customer(self):
        print("\nCustomerName : ", self.CustomerName,
              "\nAddress : ", self.__Address,
              "\nEmail : ", self.__Email,
              "\nCard"
              "\n   PIN : ", self.__Card.getCardInfo()[0],
              "\n   Card_ID : ", self.__Card.getCardInfo()[1],
              "\nAccount"
              "\n   Savings Account Balance : ", self.SavAcc.Balance,
              "\n   Current Account Balance : ", self.CurAcc.Balance)

    def ChangePIN(self, newPIN):
        self.__Card.ChangePIN(newPIN)
