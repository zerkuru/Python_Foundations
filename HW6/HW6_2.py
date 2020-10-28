#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#Значения данных атрибутов должны передаваться при создании экземпляра класса.
#Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    # атрибуты класса
    asphalt_total_mass = 0
    mass_per_meter_cm = int(input("Введите массу асфальта на 1 м2 на глубину 1 см: "))
    depth = int(input("Введите общую толщину полотна: "))
    # методы класса
    def __init__(self):
        print("Создана новая дорога")
        self._width = int(input("Введите ширину дороги: "))
        self._length = int(input("Введите длину дороги: "))
        self._asphalt = self._width * self._length * self.depth * self.mass_per_meter_cm
        self.asphalt_total_mass += self._asphalt
        print(f"Общая масса асфальта {self.asphalt_total_mass}")


Road1 = Road()
Road2 = Road()
Road3 = Road()

