from datetime import datetime

import BankCustomer
import ATM

ATM1 = ATM.ATM("0001")
ATM1.display_ATM()

person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
#person1.ChangePIN("2345")
#person1.display_Customer()

#person2 = BankCustomer.BankCustomer("qweer", "qwe", "qwe")

#person1.display_Customer()

#ATM1.cash_deposit(person1, 500)

#person1.display_Customer()

ATM1.cash_deposit(person1, 200)
person1.display_Customer()
