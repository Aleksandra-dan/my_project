#базовый класс
class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Транспорт движется со скоростью {self.speed} км/ч")

    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed}"


#наследники
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Бип-бип!")

    def move(self):
        print(f"Машина марки {self.brand} движется со скоростью {self.speed} км/ч")

    def __str__(self):
        return f"Машина: {self.brand}, Скорость: {self.speed}, Мест: {self.seats}"

    #магич методы
    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        # Если пытаемся сложить с не-Car объектом
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Велосипед {self.brand} движется со скорость. {self.speed} км/ч")

    def __str__(self):
        return f"Bелосипед: {self.brand}, скорость: {self.speed}, тип: {self.type}"


#использование
if __name__ == "__main__":
    print("4 лабораторная работа")

    #создание объектов
    transport1 = Transport("Hawk", 55)
    car1 = Car("Aston Martin", 132, 5)
    car2 = Car("Forseven", 111, 4)
    bike1 = Bike("Ginetta", 34, "mountain")

    #вывод на экран (работа __str__)
    print("\n2. Вывод введённых объектов:")
    print(transport1)
    print(car1)
    print(car2)
    print(bike1)

    #проверка методов move() и honk()
    print("\n3. Проверка методов:")
    transport1.move()
    car1.move()
    bike1.move()
    car1.honk()

    #использование len(car)
    print(f"\n4. Количество мест в car1: {len(car1)}")

    #сравнение двух машин
    print(f"\n5. Сравнение машин:")
    print(f"car1 == car2: {car1 == car2}")

    #сложение скоростей двух машин
    print(f"\n6. Сложение скоростей машин:")
    total_speed = car1 + car2
    print(f"car1 + car2 = {total_speed}")

    #сложение машины и велосипеда
    print(f"\n7. Сложение машины и велосипеда:")
    try:
        result = car1 + bike1
        print(f"car1 + bike1 = {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

    #Доп задание
    print("\n Дополнительное задание")

    #созд списка объектов
    vehicles = [
        Transport("Generic Transport", 80),
        Car("Vanwall", 150, 4),
        Car("Williams", 130, 5),
        Bike("Locust", 30, "road"),
        Bike("Westfield", 20, "mountain")
    ]

    # Вызов метода move() для каждого объекта
    print("Вызов метода move() для всех транспортных средств:")
    for vehicle in vehicles:
        vehicle.move()