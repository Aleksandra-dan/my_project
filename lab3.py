# Лабораторная работа 3 
print("=== Задание 1 ===") 
squares = [x**2 for x in range(1, 11)] 
print("Квадраты чисел:", squares) 
print() 
print("=== Задание 2 ===") 
even_numbers = [x for x in range(1, 21) if x % 2 == 0] 
print("Четные числа:", even_numbers) 
print() 
print("=== Задание 3 ===") 
words = ["python", "Java", "c++", "Rust", "go"] 
filtered_words = [word.upper() for word in words if len(word) 
print("Фильтрованные слова:", filtered_words) 
print() 
print("=== Задание 4 ===") 
class Countdown: 
    def __init__(self, n): 
        self.n = n 
    def __iter__(self): 
        return self 
    def __next__(self): 
        if self.n == 0: 
            raise StopIteration 
        current = self.n 
        self.n -= 1 
        return current 
print("Countdown от 5:") 
for x in Countdown(5): 
    print(x, end=" ") 
print() 
print() 
print("=== Задание 5 ===") 
def fibonacci(n): 
    a, b = 0, 1 
    for _ in range(n): 
        yield a 
        a, b = b, a + b 
print("Числа Фибоначчи:") 
for num in fibonacci(5): 
    print(num, end=" ") 
print() 
print() 
print("=== Задание 6 ===") 
from decimal import Decimal 
def deposit_calculator(): 
    P = Decimal(input("Начальная сумма вклада: ")) 
    r = Decimal(input("Процентная ставка годовых: ")) 
    t = Decimal(input("Срок вклада (лет): ")) 
    S = P * (1 + r / (12 * 100)) ** (12 * t) 
    print(f"Итоговая сумма: {S:.2f} руб") 
    print(f"Прибыль: {S - P:.2f} руб") 
# deposit_calculator()  # раскомментируй для теста 
print() 
print("=== Задание 7 ===") 
from fractions import Fraction 
a = Fraction(3, 4) 
b = Fraction(5, 6) 
print(f"Дроби: {a}, {b}") 
print(f"Сложение: {a + b}") 
print(f"Вычитание: {a - b}") 
print(f"Умножение: {a * b}") 
print(f"Деление: {a / b}") 
print() 
print("=== Задание 8 ===") 
from datetime import datetime 
now = datetime.now() 
print(f"Текущая дата и время: {now}") 
print(f"Только дата: {now.date()}") 
print(f"Только время: {now.time()}") 
print() 
print("=== Задание 9 ===") 
from datetime import date, timedelta 
birthday = date(2000, 1, 1)  # ЗАМЕНИ на свою дату рождения! 
today = date.today() 
days_passed = (today - birthday).days 
next_birthday = date(today.year, birthday.month, birthday.day) 
    next_birthday = date(today.year + 1, birthday.month, birthday.day) 
days_to_birthday = (next_birthday - today).days 
print(f"Дней с рождения: {days_passed}") 
print(f"Дней до следующего дня рождения: {days_to_birthday}") 
print() 
print("=== Задание 10 ===") 
def format_date(dt): 
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'] 
    return f'Сегодня {dt.day} {months[dt.month-1]} {dt.year} года, время: {dt.strftime("%H:%M")}' 
now = datetime.now() 
print(format_date(now)) 
print() 
