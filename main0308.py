# Задание №1

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

import pytest

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

# Задание №2

class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def test_calculator():
    calc = Calculator()

    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0
    assert calc.multiply(-2, 3) == -6
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3

    with pytest.raises(ValueError) as excinfo:
        calc.divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

# Задание №3

class BankAccount:
    def __init__(self, initial_balance: float = 0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance


def test_bank_account():
    account = BankAccount()
    assert account.get_balance() == 0

    account = BankAccount(100)
    assert account.get_balance() == 100

    account.deposit(50)
    assert account.get_balance() == 150

    account.withdraw(30)
    assert account.get_balance() == 120

    with pytest.raises(ValueError) as excinfo:
        account.deposit(-10)
    assert "Deposit amount must be positive" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        account.withdraw(-10)
    assert "Withdrawal amount must be positive" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        account.withdraw(200)
    assert "Insufficient funds" in str(excinfo.value)

# Задание №4

import math

class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

def test_shapes():
    # Тестирование прямоугольника
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    # Тестирование круга
    circle = Circle(3)
    assert math.isclose(circle.area(), 28.274333882308138, rel_tol=1e-9)

    # Проверка полиморфизма
    shapes = [Rectangle(2, 3), Circle(2)]
    areas = [shape.area() for shape in shapes]
    assert areas[0] == 6
    assert math.isclose(areas[1], 12.566370614359172, rel_tol=1e-9)

# Задание №5

def is_even(number: int) -> bool:
    return number % 2 == 0

@pytest.mark.parametrize("number,expected", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (10, True),
    (11, False),
    (-2, True),
    (-3, False),
])
def test_is_even(number, expected):
    assert is_even(number) == expected