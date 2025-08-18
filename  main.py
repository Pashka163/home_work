# Задача 1

import asyncio

async def wait_and_print(seconds):
    await asyncio.sleep(seconds)
    print(f"Завершено ожидание {seconds} секунд")

asyncio.run(wait_and_print(3))

# Задача 2

import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Статус ответа: {response.status}")

asyncio.run(fetch_url('https://example.com'))

# Задача 3

import asyncio

async def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

asyncio.run(read_file('test.txt'))

# Задача 4

import asyncio

async def task(name, seconds):
    await asyncio.sleep(seconds)
    print(f"Задача {name} завершена")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 2),
        task("C", 2)
    )

asyncio.run(main())

# Задача 5

import asyncio

async def timer(seconds):
    await asyncio.sleep(seconds)
    print(f"Таймер {seconds} сек завершен")

async def main():
    await asyncio.gather(
        timer(1),
        timer(2),
        timer(3)
    )

asyncio.run(main())

# Задача 6

import asyncio

async def process_number(n):
    await asyncio.sleep(1)
    return n * 2

async def process_list(numbers):
    results = await asyncio.gather(*[process_number(n) for n in numbers])
    print(results)

asyncio.run(process_list([1, 2, 3]))

# Задача 7

import asyncio

async def get_input():
    loop = asyncio.get_event_loop()
    text = await loop.run_in_executor(None, input, "Введите текст: ")
    await asyncio.sleep(2)
    print(f"Вы ввели: {text}")

asyncio.run(get_input())

# Задача 8

import asyncio

async def func1():
    await asyncio.sleep(1)
    print("Функция 1 завершена")

async def func2():
    await asyncio.sleep(2)
    print("Функция 2 завершена")

async def main():
    await asyncio.gather(func1(), func2())

asyncio.run(main())
