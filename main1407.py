# Задача 1

import time

def log_time_and_args(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Функция выполнилась за {end_time - start_time:.4f} секунд")
        return result

    return wrapper

@log_time_and_args
def add(a, b):
    return a + b

print(add(3, 5))

# Задача 2

def check_types(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, type_ in zip(args, types):
                if not isinstance(arg, type_):
                    raise TypeError(f"Аргумент {arg} должен быть типа {type_}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_types(int, int)
def multiply(a, b):
    return a * b

print(multiply(2, 3))

# Задача 3

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls > max_calls:
                raise Exception(f"Превышен лимит вызовов ({max_calls})")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(2)
def greet(name):
    return f"Привет, {name}!"

print(greet("Анна"))  # Работает

# Задача 4

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1)
    return "Готово!"

print(slow_function())

# Задача 5

def requires_auth(allowed_roles):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role not in allowed_roles:
                print("Доступ запрещен!")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования
@requires_auth(["admin", "moderator"])
def delete_post(post_id):
    return f"Пост {post_id} удален"

print(delete_post("admin", 123))

# Задача 6

def stringify_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wrapper

@stringify_result
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
print(type(result))

# Задача 7

import time

def check_duration(max_seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            if duration > max_seconds:
                print(f"Внимание! Функция {func.__name__} выполнялась {duration:.2f} секунд (дольше {max_seconds} сек)")
            return result
        return wrapper
    return decorator

@check_duration(1)
def long_running_task():
    time.sleep(2)

long_running_task()