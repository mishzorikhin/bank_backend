# Сценарии 
## Сценарий 1

* Создание банкомата
* Создание пользователя
* Изменение PIN кода
* Просмотр информации о пользователе
* Занесение 100 наличных
* Занесение 300 наличных
* Просмотр баланса
* Просмотр транзакций

***
```python
ATM1 = ATM.ATM("0001")

person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")`

person1.ChangePIN(1234)
print(person1)
ATM1.crediting_funds(person1, 100)
ATM1.crediting_funds(person1, 300)
print(ATM1.get_balance(person2)[0])
print(*ATM1.display_transaction(person2))
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

***
```python
ATM1 = ATM.ATM("0001")
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")`
person2 = BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")

ATM1.crediting_funds(person2, 100)
ATM1.crediting_funds(person2, 300)
ATM1.transfer_another(person1, person2, 50)
ATM1.transfer_another(person1, person2, 100)
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
* Просмотр баланса пользователя 1
* Снятие 100 наличных пользователя 2
* Просмотр баланса пользователя 2

***
```python
ATM1 = ATM.ATM("0001")
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")`
person2 = BankCustomer.BankCustomer("Сорокина Елизавета Яновна", " бульвар Славы, 32", "kellie22@green.com")

ATM1.crediting_funds(person2, 100)
ATM1.transfer_another(person1, person2, 100)
print(ATM1.get_balance(person1)[0])
print(ATM1.get_balance(person2)[0])
ATM1.withdrawal_funds(person2, -100)
print(ATM1.get_balance(person2)[0])
```
***

