print('Hello, Github!')


def main():
    print("Программа для выполнения различных задач")
    print("=" * 40)

    # 1. Таблица умножения от 1 до 9
    print("\n1. Таблица умножения от 1 до 9:")
    print("-" * 30)
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} × {j} = {i * j:2}", end="  ")
        print()

    # 2. Сумма всех нечётных чисел от 1 до 100
    print("\n2. Сумма всех нечётных чисел от 1 до 100:")
    odd_sum = 0
    for i in range(1, 101, 2):
        odd_sum += i
    print(f"Сумма = {odd_sum}")

    # 3. Вывод всех делителей числа
    print("\n3. Поиск делителей числа:")
    try:
        num = int(input("Введите число: "))
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        print(f"Делители числа {num}: {divisors}")
    except ValueError:
        print("Ошибка! Введите целое число.")

    # 4. Факториал числа
    print("\n4. Вычисление факториала:")
    try:
        n = int(input("Введите число: "))
        if n < 0:
            print("Факториал отрицательного числа не определён")
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            print(f"{n}! = {factorial}")
    except ValueError:
        print("Ошибка! Введите целое число.")

    # 5. Последовательность Фибоначчи
    print("\n5. Последовательность Фибоначчи:")
    try:
        length = int(input("Введите длину последовательности: "))
        if length <= 0:
            print("Длина должна быть положительным числом")
        else:
            fib_sequence = []
            a, b = 0, 1
            for _ in range(length):
                fib_sequence.append(a)
                a, b = b, a + b
            print(f"Последовательность Фибоначчи: {fib_sequence}")
    except ValueError:
        print("Ошибка! Введите целое число.")


# Запуск программы
if __name__ == "__main__":
    main()