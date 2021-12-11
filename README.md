# Сценарии 
## Сценарий 1

* Создание банкомата
* Создание пользователя
* Просмотр информации о пользователе
* Занесение 100 наличных
* Просмотр баланса
* Просмотр транзакций

***
```python
ATM1 = ATM.ATM("0001")

person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")

print(person1)
ATM1.crediting_funds(person1, 100)
print("CurAcc : " + str(ATM1.get_balance(person1, "CurAcc")))
print("SavAcc : " + str(ATM1.get_balance(person1, "SavAcc")))
print(*ATM1.display_transaction(person1))

```
***

## Сценарий 2

* Создание банкомата
* Создание пользователя 1
* Создание пользователя 2
* Занесение 100 наличных пользователю 1
* перевод 50 от пользователя 1 пользователю 2
* перевод 100 от пользователя 1 пользователю 2
* Просмотр транзакций пользователя 1
* Просмотр транзакций пользователя 2

***
```python
ATM1 = ATM.ATM("0001")
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
person2 = BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")

ATM1.crediting_funds(person1, 100)
ATM1.transfer_another(person1, person2, 50)
ATM1.transfer_another(person1, person2, 100)
print(*ATM1.display_transaction(person1))
print(*ATM1.display_transaction(person2))
```
***

## Сценарий 3

* Создание банкомата
* Создание пользователя 1
* Создание пользователя 2
* Занесение 100 наличных пользователю 1
* Перевод 100 от пользователя 1 пользователю 2
* Просмотр баланса пользователя 2 
* Перевод на сберегательный счет 100 пользователя 2
* Просмотр баланса пользователя 2

***
```python
ATM1 = ATM.ATM("0001")
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")
person2 = BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")

ATM1.crediting_funds(person1, 100)
ATM1.transfer_another(person1, person2, 100)
print("CurAcc : " + str(ATM1.get_balance(person2, "CurAcc")))
print("SavAcc : " + str(ATM1.get_balance(person2, "SavAcc")))
ATM1.replenishment_savings_account(person2, 100)
print("CurAcc : " + str(ATM1.get_balance(person2, "CurAcc")))
print("SavAcc : " + str(ATM1.get_balance(person2, "SavAcc")))
print(*ATM1.display_transaction(person2))
```
***

