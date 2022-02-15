# 7. Реализовать проект «Операции с комплексными числами».
# Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа),
# выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.x = 'a + b * j'

    def __add__(self, other):
        print(f'Сумма x_1 и x_2 равна')
        return f'x = {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        print(f'Произведение x_1 и x_2 равно')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * j'

    def __str__(self):
        return f'x = {self.a} + {self.b} * j'


x_1 = ComplexNumber(1, -2)
x_2 = ComplexNumber(3, 4)
print(x_1)
print(x_2)
print(x_1 + x_2)
print(x_1 * x_2)
