# Задача 1

import threading
import time

def print_numbers():
    for i in range(1, 51):
        print(i)
        time.sleep(0.5)

def print_letters():
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(letter)
        time.sleep(0.5)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

# Задача 2

import threading
import random

def calculate_sum(arr, result, index):
    result[index] = sum(arr)

numbers = [random.randint(1, 100) for _ in range(1000)]
part_size = len(numbers) // 4
results = [0] * 4

threads = []
for i in range(4):
    start = i * part_size
    end = start + part_size
    t = threading.Thread(target=calculate_sum, args=(numbers[start:end], results, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Суммы частей: {results}")
print(f"Общая сумма: {sum(results)}")

# Задача 3

import threading

def add(a, b):
    print(f"{a} + {b} = {a + b}")

def subtract(a, b):
    print(f"{a} - {b} = {a - b}")

def multiply(a, b):
    print(f"{a} * {b} = {a * b}")

def divide(a, b):
    print(f"{a} / {b} = {a / b}")

a, b = 10, 5
threads = [
    threading.Thread(target=add, args=(a, b)),
    threading.Thread(target=subtract, args=(a, b)),
    threading.Thread(target=multiply, args=(a, b)),
    threading.Thread(target=divide, args=(a, b))
]

for t in threads:
    t.start()

for t in threads:
    t.join()

# Задача 4

from concurrent.futures import ThreadPoolExecutor
import time

def task(number):
    print(f"Задача {number} начата")
    time.sleep(2)
    print(f"Задача {number} завершена")

with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(10):
        executor.submit(task, i)

# Задача 5

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

urls = [
    'https://example.com',
    'https://python.org',
    'https://www.google.com'
]

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else 'No title'
    print(f"URL: {url} | Title: {title}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(scrape, urls)