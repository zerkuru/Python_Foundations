#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#и метод running (запуск).
#Атрибут реализовать как приватный.
#В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#третьего (зеленый) — на ваше усмотрение.
#Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить,
#реализовав проверку порядка режимов,
#и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from datetime import datetime
import time
class Trafficlight:
    # атрибуты класса
    def __init__(self):
        print("Светофор работает")
        self.__color = "Красный"
        print(f"Цвет светофора {self.__color}")
    # методы класса
    def running(self):
        current_datetime = datetime.now()
        current_date = datetime.now()
        timelapse = 0
        print(f"Светофор работает и переключается")
        if self.__color =="Красный":
            nextcolor = "Желтый"
            timelapse = 7
        elif self.__color == "Желтый":
            nextcolor = "Зеленый"
            timelapse = 2
        else:
            nextcolor = "Красный"
            timelapse = 10

        while (current_date - current_datetime).total_seconds() < timelapse:
            time.sleep(1)
            current_date = datetime.now()
        self.__color = nextcolor
        print(f"Цвет светофора {self.__color}")


Traffic = Trafficlight()
Traffic.running()
Traffic.running()
Traffic.running()
Traffic.running()
