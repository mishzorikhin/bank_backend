import ATM
import BankCustomer

ATM1 = ATM.ATM("0001")

person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")

person1.ChangePIN(1234)
print(person1)
ATM1.crediting_funds(person1, 100)
ATM1.crediting_funds(person1, 300)
print(ATM1.get_balance(person1, "CurAcc"))
print(*ATM1.display_transaction(person1))

