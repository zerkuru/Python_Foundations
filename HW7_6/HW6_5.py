#Реализовать класс Stationery (канцелярская принадлежность).
#Определить в нем атрибут title (название) и метод draw (отрисовка).
#Метод выводит сообщение “Запуск отрисовки.”
#Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#В каждом из классов реализовать переопределение метода draw.
#Для каждого из классов метод должен выводить уникальное сообщение.
#Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery():
    title = ""
    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    title = "Pen"
    def draw(self):
        print("Отрисовка шариковой ручкой")

class Pencil(Stationery):
    title = "Pencil"
    def draw(self):
        print("Отрисовка простым карандашом")

class Handle(Stationery):
    title = "Handle"
    def draw(self):
        print("Отрисовка маркером")

White = Pen()
Yellow = Pencil()

White.draw()
Yellow.draw()
Red = Handle()
Red.draw()
