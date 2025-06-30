# Задача 1

# class BankAccount:
#     def __init__(self, name, balance, passport):
#         self.name = name
#         self.balance = balance
#         self.passport = passport
#
#     def print_public_data(self):
#         print("Данные через метод:")
#         print("Имя:", self.name)
#         print("Баланс:", self.balance)
#         print("Паспорт:", self.passport)
#
# account1 = BankAccount('Иван', 1000, '1234567890')
#
# account1.print_public_data()
#
# print("\nДанные через прямое обращение к атрибутам:")
#
# print("Имя:", account1.name)
# print("Баланс:", account1.balance)
# print("Паспорт:", account1.passport)

# Задача 2

# class BankAccount:
#     def __init__(self, name, money, passport):
#         self._name = name
#         self._money = money
#         self._passport = passport
#     def show_data(self):
#         print(f"Имя: {self._name}, Деньги: {self._money}, Паспорт: {self._passport}")
#
# my_account = BankAccount("Анна", 5000, "1234567890")
# my_account.show_data()
#
# print("\nПрямой доступ (не рекомендуется):")
# print(my_account._name)
# print(my_account._money)
# print(my_account._passport)

# Задача 3

# class BankAccount:
#     def __init__(self, name, money):
#         self.__name = name
#         self.__money = money
#
#     def show_info(self):
#         print(f"Владелец: {self.__name}, Баланс: {self.__money}")
#         self.__print_secret()
#
#     def __print_secret(self):
#         print("Это приватные данные!")
#
# my_account = BankAccount("Анна", 5000)
#
# my_account.show_info()
