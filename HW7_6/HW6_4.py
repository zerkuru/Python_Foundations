# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")

    def show_color(self):
        print(f"Машина {self.name} имеет цвет {self.color}")

    def show_police(self):
        if self.is_police:
            print(f"Машина {self.name} - полицейская")
        else:
            print(f"Машина {self.name} - не полицейская")


class TownCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")
        if self.speed > 60:
            print(f"Машина {self.name} превышает допустимую скорость 60 км/ч")


class WorkCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")
        if self.speed > 40:
            print(f"Машина {self.name} превышает допустимую скорость 40 км/ч")


class SportCar(Car):
    color = "смешанный"

class PoliceCar(Car):
    def __init__(self):
        self.is_police = True


Mercy = PoliceCar()
Volks = TownCar()
Andy = WorkCar()
Alice = SportCar()

Mercy.speed = 120
Mercy.name = "Мерседес"
Mercy.color = "Белый"
Mercy.show_color()
Mercy.show_speed()
Mercy.show_police()

Volks.speed = 100
Volks.name = "Фольксваген"
Volks.show_speed()
Volks.show_police()

Alice.name = "Ягуар"
Alice.speed = 300
Alice.show_speed()

