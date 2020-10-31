#2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#К типам одежды в этом проекте относятся пальто и костюм.
#У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
#Проверить на практике полученные на этом уроке знания:
#реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from math import ceil

class Clothes(ABC):
    length = 0
    width = 0
    @abstractmethod
    def fabric_cost(self):
        return self.length * self.width

class Coat(Clothes):
    size = 0
    def __init__(self, newsize):
        self.size = newsize

    @property
    def fabric_cost(self):
        return ceil((self.size/6.5 + 0.5) * 10) / 10

class Costume(Clothes):
    height = 0
    def __init__(self, newheight):
        self.height = newheight

    @property
    def fabric_cost(self):
        return ceil((2*self.height + 0.3) * 10)/10

NewCoat = Coat(12)
print(f"Расход на новое пальто: {NewCoat.fabric_cost}")
NewCostume = Costume(3)
print(f"Расход на новый костюм: {NewCostume.fabric_cost}")