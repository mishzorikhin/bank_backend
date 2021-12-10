import ATM
import BankCustomer

ATM1 = ATM.ATM("0001")


person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
person2 = BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")


ATM1.replenishment_savings_account(person2, 50)
print(person2)

