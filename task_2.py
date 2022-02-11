# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence

    def __str__(self):
        return f'Пальто: размер {self.size}, расход ткани на одно пальто = {self.expence}, общий расход ткани = {Coat.expence_count:.02f}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.expence_count += self.expence

    def __str__(self):
        return f'Костюм: рост {self.height}, расход ткани на один костюм = {self.expence}, общий расход ткани = {Costume.expence_count}'

    @property
    def expence(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(f'{exp:.02f}')


cloth_1 = Coat(52)
print(cloth_1)
cloth_2 = Costume(185)
print(cloth_2)
cloth_3 = Costume(169)
print(cloth_3)
cloth_4 = Coat(44)
print(cloth_4)
