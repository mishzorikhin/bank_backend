from CashDispenser import CashDispenser


class ATM:

    def __init__(self, ATM_ID):
        self.ATM_ID = ATM_ID


    def display_ATM(self):
        print("ATM_ID : ", self.ATM_ID)


    def cash_deposit(self, Customer, balanse):
        Customer.Acc.top_up_balance(balanse)





