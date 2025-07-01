# Задача 1

class Restricted:
    def __getattribute__(self, name):
        if name.startswith('_secret_'):
            raise AttributeError("Доступ запрещен")
        return super().__getattribute__(name)

r = Restricted()
r._secret_data = 123
try:
    print(r._secret_data)
except AttributeError as e:
    print(e)

# Задача 2

class Dynamic:
    def __getattr__(self, name):
        if name.startswith('square_'):
            num = int(name[7:])
            return num * num
        raise AttributeError("Нет такого атрибута")

d = Dynamic()
print(d.square_5)
print(d.square_3)

# Задача 3

class Immutable:
    def __setattr__(self, name, value):
        if name.startswith('_lock_'):
            raise AttributeError("Нельзя изменять")
        super().__setattr__(name, value)

i = Immutable()
i._lock_data = 100
try:
    i._lock_data = 200
except AttributeError as e:
    print(e)

# Задача 4

class Lowercase:
    def __setattr__(self, name, value):
        super().__setattr__(name.lower(), value)

l = Lowercase()
l.MyAttr = "value"
print(l.myattr)

# Задача 5

class Restricted:
    allowed = ['name', 'age']

    def __setattr__(self, name, value):
        if name not in self.allowed:
            raise AttributeError("Атрибут запрещен")
        super().__setattr__(name, value)

p = Restricted()
p.name = "Alice"
try:
    p.address = "Street"
except AttributeError as e:
    print(e)