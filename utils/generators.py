import random
import allure
import string
import time


@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.step("Генерация уникального логина")
def generate_unique_login():
    timestamp = str(int(time.time()))
    return f"courier_{generate_random_string(6)}_{timestamp[-6:]}"


@allure.step("Генерация уникального пароля")
def generate_unique_password():
    return generate_random_string(10)


@allure.step("Генерация уникального имени")
def generate_unique_first_name():
    names = ["Алексей", "Дмитрий", "Андрей", "Сергей", "Михаил", "Николай", "Владимир"]
    return f"{random.choice(names)}_{generate_random_string(4)}"


@allure.step("Генерация случайного номера телефона")
def generate_phone_number():
    return f"+7 {random.randint(900, 999)} {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}"


@allure.step("Генерация случайного адреса")
def generate_address():
    streets = ["Ленина", "Пушкина", "Гагарина", "Мира", "Советская"]
    return f"ул. {random.choice(streets)}, д. {random.randint(1, 100)}, кв. {random.randint(1, 200)}"