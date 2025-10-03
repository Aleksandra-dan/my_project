# ������ୠ� ࠡ�� 3 
print("=== ������� 1 ===") 
squares = [x**2 for x in range(1, 11)] 
print("������� �ᥫ:", squares) 
print() 
print("=== ������� 2 ===") 
even_numbers = [x for x in range(1, 21) if x % 2 == 0] 
print("���� �᫠:", even_numbers) 
print() 
print("=== ������� 3 ===") 
words = ["python", "Java", "c++", "Rust", "go"] 
filtered_words = [word.upper() for word in words if len(word) 
print("�����஢���� ᫮��:", filtered_words) 
print() 
print("=== ������� 4 ===") 
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
print("Countdown �� 5:") 
for x in Countdown(5): 
    print(x, end=" ") 
print() 
print() 
print("=== ������� 5 ===") 
def fibonacci(n): 
    a, b = 0, 1 
    for _ in range(n): 
        yield a 
        a, b = b, a + b 
print("��᫠ ��������:") 
for num in fibonacci(5): 
    print(num, end=" ") 
print() 
print() 
print("=== ������� 6 ===") 
from decimal import Decimal 
def deposit_calculator(): 
    P = Decimal(input("��砫쭠� �㬬� ������: ")) 
    r = Decimal(input("��業⭠� �⠢�� �������: ")) 
    t = Decimal(input("�ப ������ (���): ")) 
    S = P * (1 + r / (12 * 100)) ** (12 * t) 
    print(f"�⮣���� �㬬�: {S:.2f} ��") 
    print(f"�ਡ��: {S - P:.2f} ��") 
# deposit_calculator()  # �᪮������� ��� ��� 
print() 
print("=== ������� 7 ===") 
from fractions import Fraction 
a = Fraction(3, 4) 
b = Fraction(5, 6) 
print(f"�஡�: {a}, {b}") 
print(f"��������: {a + b}") 
print(f"���⠭��: {a - b}") 
print(f"���������: {a * b}") 
print(f"�������: {a / b}") 
print() 
print("=== ������� 8 ===") 
from datetime import datetime 
now = datetime.now() 
print(f"������ ��� � �६�: {now}") 
print(f"���쪮 ���: {now.date()}") 
print(f"���쪮 �६�: {now.time()}") 
print() 
