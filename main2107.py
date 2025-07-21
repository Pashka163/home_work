# Задача 1

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = None
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

if __name__ == "__main__":
    singleton1 = Singleton()
    singleton1.set_value("Hello, Singleton!")

    singleton2 = Singleton()

    print(f"Singleton1 value: {singleton1.get_value()}")
    print(f"Singleton2 value: {singleton2.get_value()}")
    print(f"Are instances the same? {singleton1 is singleton2}")

    singleton2.set_value("Value changed!")

    print(f"Singleton1 value after change: {singleton1.get_value()}")

# Задача 2

class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Простой кофе"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", с молоком"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", с сахаром"

if __name__ == "__main__":

    simple_coffee = Coffee()
    print(f"{simple_coffee.description()}: ${simple_coffee.cost()}")

    coffee_with_milk = MilkDecorator(simple_coffee)
    print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")

    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")

    coffee_with_sugar = SugarDecorator(simple_coffee)
    print(f"{coffee_with_sugar.description()}: ${coffee_with_sugar.cost()}")