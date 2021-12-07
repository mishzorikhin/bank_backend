from ATMCard import ATMCard
from Acc import Account


class BankCustomer:

    #__CustomerName = " "
    #__Address = " "
    #__Email = " "
    #__Card = ATMCard.ATMCard
    #Acc = []

    def __init__(self, CustomerName, Address, Email):
        self.__CustomerName = CustomerName
        self.__Address = Address
        self.__Email = Email
        self.__Card = ATMCard(1234, "001")
        self.CurAcc = self.__Card.CurAcc
        self.SavAcc = self.__Card.SavAcc



    def display_Customer(self):
        print("CustomerName : ", self.__CustomerName,
              "\nAddress : ", self.__Address,
              "\nEmail : ", self.__Email,
              "\nCard"
              "\n   PIN : ", self.__Card.getCardInfo()[0],
              "\n   Card_ID : ", self.__Card.getCardInfo()[1],
              "\nAccount"
              "\n   Savings Account Balance : ", self.SavAcc.Balance,
              "\n   Current Account Balance : ", self.CurAcc.Balance)




    def InsertCard(self):
        pass

    def SelectTransaction(self):
        pass

    def EnterPIN(self):
        pass

    def ChangePIN(self, newPIN):
        self.__Card.ChangePIN(newPIN)

    def RequestTransactionSummary(self):
        pass