# Задача 1

# class Shape:
#     def area(self):
#         raise NotImplementedError("Этот метод должен быть переопределен")
#
# class Circle(Shape):
#     def area(self):
#         return 3.14 * 5 * 5
#
# class Rectangle(Shape):
#     def area(self):
#         return 10 * 20
#
# print("Площадь круга:", Circle().area())
# print("Площадь прямоугольника:", Rectangle().area())

# Задача 2

# class Animal:
#     def make_sound(self):
#         raise NotImplementedError("Этот метод должен быть переопределен")
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Гав-гав!"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Мяу!"
#
# print("Собака:", Dog().make_sound())
# print("Кошка:", Cat().make_sound())

# Задача 3

# class Vehicle:
#     def speed(self):
#         raise NotImplementedError("Этот метод должен быть переопределен")
#
# class Car(Vehicle):
#     def speed(self):
#         return "120 км/ч"
#
# class Bicycle(Vehicle):
#     def speed(self):
#         return "25 км/ч"
#
# print("Машина:", Car().speed())
# print("Велосипед:", Bicycle().speed())

# Задача 4

# class Payment:
#     def pay(self):
#         raise NotImplementedError("Этот метод должен быть переопределен")
#
# class CreditCard(Payment):
#     def pay(self):
#         return "Платеж картой: 100 руб."
#
# class PayPal(Payment):
#     def pay(self):
#         return "Платеж PayPal: 100 руб."
#
# payments = [CreditCard(), PayPal()]
# for p in payments:
#     print(p.pay())