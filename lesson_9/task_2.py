# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def AsphaltMassCalculation(self, mass=25, thickness=5):
        print(f" {self.length} м * {self.width} м * {mass} кг * {thickness} см =",
              (self.length * self.width * mass * thickness / 1000), "т.")


road_1 = Road(20, 5000)
road_1.AsphaltMassCalculation()
