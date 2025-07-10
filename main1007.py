# Задача 1

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.grade == other.grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.grade < other.grade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.grade > other.grade
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.grade <= other.grade
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.grade >= other.grade
        return NotImplemented

student1 = Student("Иван", 4)
student2 = Student("Мария", 5)
student3 = Student("Алексей", 4)

print(student1 == student3)
print(student1 < student2)
print(student2 > student1)
print(student1 >= student3)

# Задача 2

class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if not all(isinstance(side, (int, float)) for side in self.sides):
            return "Нужно вводить только числа!"
        a, b, c = sorted(self.sides)
        if a + b > c:
            return "Ура, можно построить треугольник!"
        else:
            return "Нет, из этого треугольник не сделать."

checker1 = TriangleChecker([3, 4, 5])
print(checker1.is_triangle())

# Задача 3

class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.age = age
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"

person1 = Nikola("Максим", 25)
print(person1.name)
print(person1.age)

person2 = Nikola("Николай", 30)
print(person2.name)

try:
    person1.surname = "Петров"
except AttributeError as e:
    print(f"Ошибка: {e}")