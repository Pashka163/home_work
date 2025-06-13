# Задача 1

# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
# circle = Circle(15)
# print("Радиус круга:", circle.radius)
# print("Площадь круга:", circle.area())
# print("Периметр круга:", circle.perimeter())

# Задача 2

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# rectangle = Rectangle(4, 5)
# print("Ширина прямоугольника:", rectangle.width)
# print("Высота прямоугольника:", rectangle.height)
# print("Площадь прямоугольника:", rectangle.area())
# print("Периметр прямоугольника:", rectangle.perimeter())

# Задача 3

# class Counter:
#     def __init__(self):
#         self.value = 0
#
#     def increment(self):
#         self.value += 1
#
#     def get_value(self):
#         return self.value
#
# counter = Counter()
# print("Текущее значение счетчика:", counter.get_value())
#
# counter.increment()
# print("После увеличения:", counter.get_value())

# Задача 4

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f"Автомобиль: {self.brand} {self.model}, {self.year} года выпуска")
#
# car1 = Car("Toyota", "Camry", 2022)
# car1.display_info()
#
# car2 = Car("Tesla", "Model S", 2023)
# car2.display_info()

# Задача 5

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 5:
#             self.grades.append(grade)
#         else:
#             print(f"Ошибка: оценка {grade} должна быть от 1 до 5")
#
#     def get_average_grade(self):
#         if not self.grades:
#             return 0.0
#         return sum(self.grades) / len(self.grades)
#
#     def get_full_name(self):
#         return f"{self.last_name} {self.first_name}"
#
#     def display_info(self):
#         print(f"Студент: {self.get_full_name()}")
#         print(f"Оценки: {self.grades}")
#         print(f"Средний балл: {self.get_average_grade():.2f}")
#
# student = Student("Иван", "Петров")
#
# student.add_grade(4)
# student.add_grade(5)
# student.add_grade(3)
#
# student.display_info()