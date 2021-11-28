from Account import Account


class ATMCard():

    def __init__(self, PIN, Card_ID):
        self.__PIN = PIN
        self.__Card_ID = Card_ID
        self.Acc = Account(0)

    def getCardInfo(self):
        return self.__PIN, self.__Card_ID

    def ChangePIN(self, newPIN):
        self.__PIN = newPIN