#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
#income (доход).
#Последний атрибут должен быть защищенным и ссылаться на словарь,
#содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#Создать класс Position (должность) на базе класса Worker.
#В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#и дохода с учетом премии (get_total_income).
#Проверить работу примера на реальных данных
#(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    # атрибуты класса

    mass_per_meter_cm = int(input("Введите массу асфальта на 1 м2 на глубину 1 см: "))
    depth = int(input("Введите общую толщину полотна: "))
    # методы класса
    def __init__(self):
        self._name = input("Введите имя сотрудника: ")
        self._surname = input("Введите фамилию сотрудника: ")
        self._position = ""
        self._income = {"wage": int(input("Введите оклад: ")), "bonus": int(input("Введите премию: "))}

class Position(Worker):
    def get_full_name(self):
        fullname = f"{self._name} {self._surname}"
        print(fullname)
    def get_total_income(self):
        total_income = self._income[wage] + self._income[bonus]
        print(f"Полный доход: {total_income}")

Cleaner = Position()
Cook = Position()

Cleaner.get_full_name()
Cleaner.get_total_income()
Cook.get_full_name()
Cook.get_total_income()
