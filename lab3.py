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
