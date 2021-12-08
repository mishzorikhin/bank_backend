#from datetime import datetime
import ATM
import BankCustomer

ATM1 = ATM.ATM("0001")
#ATM1.display_ATM()
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
person2 = BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")
#person1.display_Customer()
ATM1.crediting_funds(person1, 1000)
#person1.display_Customer()
ATM1.transfer_another(person1, person2, 800)
ATM1.crediting_funds(person2, 100)
ATM1.crediting_funds(person2, 300)
ATM1.withdrawal_funds(person2, -100)
ATM1.display_Transaction(person2)