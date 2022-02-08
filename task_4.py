# 4. Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы, и покажите результат.

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет: {self.color}).')

    def go(self):
        print(f'{self.name}: машина поехала со скоростью {self.speed}.')

    def stop(self):
        print(f'{self.name}: машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'Скорость автомобиля {self.speed}'


class TownCar(Car):
    """Town car"""

    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости!'
        else:
            return f'Скорость автомобиля {self.speed}'


class SportCar(Car):
    """Sport car"""


class WorkCar(Car):
    """Work car"""

    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости!'
        else:
            return f'Скорость автомобиля {self.speed}'


class PoliceCar(Car):
    """Police car"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)
        print(f'Машина полицейская')


town_car = TownCar('MINI', 'красный', 65)
town_car.go()
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()

sport_car = SportCar('Ford', 'желтый', 180)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.stop()
print()

work_car = WorkCar('ГАЗ', 'серый', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

police_car = PoliceCar('Audi', 'белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()
