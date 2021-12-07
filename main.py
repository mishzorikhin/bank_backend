#from datetime import datetime
import ATM
import BankCustomer

ATM1 = ATM.ATM("0001")
#ATM1.display_ATM()
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
person2 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
#person1.display_Customer()
ATM1.crediting_funds(person1, 1000)
#person1.display_Customer()
ATM1.transfer_another(person1, person2, 800)
person1.display_Customer()
person2.display_Customer()