# Задача 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

first_item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
first_item.find_element(By.XPATH, "./../..//button").click()

second_item = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']")
second_item.find_element(By.XPATH, "./../..//button").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

items = driver.find_elements(By.CLASS_NAME, "cart_item")
print(f"В корзине {len(items)} товара")

driver.quit()

# Задача 2

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID, "firstName").send_keys("Иван")
driver.find_element(By.ID, "lastName").send_keys("Иванов")
driver.find_element(By.ID, "userEmail").send_keys("ivan@example.com")
driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

print("Форма заполнена успешно!")
driver.quit()

# Задача 3

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/books")

books = driver.find_elements(By.CLASS_NAME, "action-buttons")
data = []

for book in books:
    title = book.find_element(By.TAG_NAME, "a").text
    author = book.find_element(By.CLASS_NAME, "mr-2").text
    data.append([title, author])

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Автор'])
    writer.writerows(data)

print("Данные сохранены в books.csv")
driver.quit()

# Задача 4

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")

try:
    buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Click Me')]")
    if buttons:
        print(f"Найдено {len(buttons)} кнопок 'Click Me'")
    else:
        print("Кнопки не найдены")
except Exception as e:
    print(f"Ошибка: {e}")

driver.quit()