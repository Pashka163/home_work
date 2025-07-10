# Задача 1

import json
import pickle

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def to_dict(self):
        return {"brand": self.brand, "model": self.model, "year": self.year}

    @classmethod
    def from_dict(cls, data):
        return cls(data["brand"], data["model"], data["year"])

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_pickle(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

car1 = Car("Toyota", "Camry", 2020)

car1.save_to_json("car.json")
car2 = Car.load_from_json("car.json")
print(car2)

car1.save_to_pickle("car.pkl")
car3 = Car.load_from_pickle("car.pkl")
print(car3)

# Задача 2

import json
import pickle

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"])

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_pickle(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

book1 = Book("1984", "George Orwell", 1949)

# Сохранение и загрузка JSON
book1.save_to_json("book.json")
book2 = Book.load_from_json("book.json")
print(book2)

book1.save_to_pickle("book.pkl")
book3 = Book.load_from_pickle("book.pkl")
print(book3)

# Задача 3

import json
import pickle

class Stadium:
    def __init__(self, name, city, capacity):
        self.name = name
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} ({self.city}), вместимость: {self.capacity}"

    def to_dict(self):
        return {"name": self.name, "city": self.city, "capacity": self.capacity}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["city"], data["capacity"])

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_pickle(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

stadium1 = Stadium("Лужники", "Москва", 81000)

stadium1.save_to_json("stadium.json")
stadium2 = Stadium.load_from_json("stadium.json")
print(stadium2)

stadium1.save_to_pickle("stadium.pkl")
stadium3 = Stadium.load_from_pickle("stadium.pkl")
print(stadium3)