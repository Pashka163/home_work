# Задача 1

class Person:
    name = "Alice"
    age = 25

person = Person()

print(get_value(person, "name"))

# Задача 2

obj = DynamicAttributes()

obj.add_attr("color", "red")
obj.add_attr("size", 10)

print(obj.color)
print(obj.size)

obj.add_attr("color", "blue")
print(obj.color)

# Задача 3

class Car:
    brand = "Toyota"
    model = "Camry"

car = Car()

print(check_attributes(car, "brand", "model"))

# Задача 4

class Address:
    city = "Moscow"
    street = "Lenina"

class Person:
    name = "Ivan"
    address = Address()

person = Person()

print(get_nested_attr(person, "address.city"))

# Задача 5

class Product:
    def __init__(self):
        self.name = "Laptop"
        self.price = 1000
        self.weight = 2.5
        self.color = "black"

product = Product()

remove_attrs_if(product, lambda name, value: isinstance(value, str))

print(vars(product))