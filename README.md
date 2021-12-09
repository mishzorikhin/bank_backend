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


`
person1 = BankCustomer.BankCustomer("Соколов Константин Тимофеевич", "въезд Ладыгина, 50", "pucru6081@yopmail.com")`
`person1.ChangePIN(1234)`
`print(person1)`
`ATM1.crediting_funds(person1, 100)`
`ATM1.crediting_funds(person1, 300)`
`print(ATM1.get_balance(person2)[0])`
`print(*ATM1.display_transaction(person2))`

