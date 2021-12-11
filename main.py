import ATM
import BankCustomer

ATM1 = ATM.ATM("0001")

person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")

print(person1)
ATM1.crediting_funds(person1, 100)
print("CurAcc : " + str(ATM1.get_balance(person1, "CurAcc")))
print("SavAcc : " + str(ATM1.get_balance(person1, "SavAcc")))
print(*ATM1.display_transaction(person1))