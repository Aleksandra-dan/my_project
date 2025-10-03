# -*- coding: utf-8 -*- 
print("=== Task 1 ===") 
squares = [x**2 for x in range(1, 11)] 
print("Squares:", squares) 
print() 
print("=== Task 2 ===") 
even_numbers = [x for x in range(1, 21) if x % 2 == 0] 
print("Even numbers:", even_numbers) 
print() 
print("=== Task 3 ===") 
words = ["python", "Java", "c++", "Rust", "go"] 
filtered_words = [word.upper() for word in words if len(word)] 
print("Filtered words:", filtered_words) 
print() 
print("=== Task 4 ===") 
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
print("Countdown from 5:") 
for x in Countdown(5): 
    print(x, end=" ") 
print() 
print() 
print("=== Task 5 ===") 
def fibonacci(n): 
    a, b = 0, 1 
    for _ in range(n): 
        yield a 
        a, b = b, a + b 
print("Fibonacci numbers:") 
for num in fibonacci(5): 
    print(num, end=" ") 
print() 
print() 
print("=== Task 6 ===") 
from decimal import Decimal 
def deposit_calculator(): 
    P = Decimal(input("Initial deposit: ")) 
    r = Decimal(input("Annual interest rate: ")) 
    t = Decimal(input("Term in years: ")) 
    S = P * (1 + r / (12 * 100)) ** (12 * t) 
    print(f"Total amount: {S:.2f} RUB") 
    print(f"Profit: {S - P:.2f} RUB") 
print("Deposit calculator ready") 
print() 
print("=== Task 7 ===") 
from fractions import Fraction 
a = Fraction(3, 4) 
b = Fraction(5, 6) 
print(f"Fractions: {a}, {b}") 
print(f"Addition: {a + b}") 
print(f"Subtraction: {a - b}") 
print(f"Multiplication: {a * b}") 
print(f"Division: {a / b}") 
print() 
print("=== Task 8 ===") 
from datetime import datetime 
now = datetime.now() 
print(f"Current datetime: {now}") 
print(f"Date only: {now.date()}") 
print(f"Time only: {now.time()}") 
print() 
print("=== Task 9 ===")
from datetime import date
birthday = date(2005, 11, 7)  
today = date.today()
days_passed = (today - birthday).days
next_birthday = date(today.year, birthday.month, birthday.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)
days_to_birthday = (next_birthday - today).days
print(f"Days since birth: {days_passed}")
print(f"Days to next birthday: {days_to_birthday}")
print()
print("=== Task 10 ===") 
def format_date(dt): 
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'] 
    return f'Today is {dt.day} {months[dt.month-1]} {dt.year}, time: {dt.strftime("%H:%M")}' 
now = datetime.now() 
print(format_date(now)) 
