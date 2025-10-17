# Объединяем все вместе для удобного тестирования

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        return result

    return wrapper


def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None

        return wrapper

    return decorator


# Функции с декоратором логирования
@logger
def add(a, b):
    return a + b


@logger
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


@logger
def greet(name):
    return f"Привет, {name}!"


# Функции с декоратором доступа
@require_role(['admin'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "База данных успешно удалена"


@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки успешно изменены"


@require_role(['user', 'admin', 'manager'])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные успешно просмотрены"


# Тестирование
if __name__ == "__main__":
    print("~~~~~~~~~~~ ТЕСТИРОВАНИЕ ДЕКОРАТОРА ЛОГИРОВАНИЯ ~~~~~~~~~~~")
    add(5, 3)
    print()
    divide(10, 2)
    print()
    divide(10, 0)
    print()
    greet("Анна")

    print("\n~~~~~~~~ ТЕСТИРОВАНИЕ ДЕКОРАТОРА ДОСТУПА ~~~~~~~~~~~")
    users = [
        {'name': 'Вардеван', 'role': 'admin'},
        {'name': 'Нарэк', 'role': 'manager'},
        {'name': 'Азарапет', 'role': 'user'},
        {'name': 'Дареджан', 'role': 'guest'},
        {'name': 'Заринэ', 'role': 'user'}
    ]

    for user in users:
        print(f"\n~~~ Пользователь: {user['name']} (роль: {user['role']}) ~~~")
        delete_database(user)
        edit_settings(user)
        view_data(user)