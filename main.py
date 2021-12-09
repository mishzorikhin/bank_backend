import getpass

import ATM
import BankCustomer


ATM1 = ATM.ATM("0001")

person1, person2 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com"),\
                   BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")

ATM1.crediting_funds(person2, 100)
ATM1.transfer_another(person1, person2, 100)
print(ATM1.get_balance(person1)[0])
print(ATM1.get_balance(person2)[0])
ATM1.withdrawal_funds(person2, -100)
print(ATM1.get_balance(person2)[0])
