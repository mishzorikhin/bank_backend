import ATM
import BankCustomer

ATM1 = ATM.ATM("0001")

person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")

person1.ChangePIN(1234)

ATM1.replenishment_savings_account(person1,50)
print(person1)
