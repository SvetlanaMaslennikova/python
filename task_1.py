# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31    22  | 3   5   32  |   3   5   8   3   |
# | 37    43  | 2   4   6   |   8   3   7   1   |
# | 51    86  | -1  64  -8  |                   |
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, data):
        self.data = data
        for line in self.data[: -1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Количество элементов в строках не совпадает')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if not len(self.data) == len(other.data):
            raise ValueError('Размерности матриц не совпадают')
        else:
            for i in range(len(self.data)):
                if not len(self.data[i]) == len(other.data):
                    raise ValueError('Размерности матриц не совпадают')
                item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in
                         range(len(self.data[line]))] for line in range(len(self.data))]
                return Matrix(item)


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [[31, 22, 37], [43, 51, 86], [3, 5, 8]]
mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
print(mtrx_1)
print(mtrx_2)
print(mtrx_1 + mtrx_2)

m_3 = [[3, 8], [5, 3], [8, 7]]
m_4 = [[3, 5, 32], [8, 3, 1], [2, 4, 6]]
mtrx_3 = Matrix(m_3)
mtrx_4 = Matrix(m_4)
print(mtrx_3)
print(mtrx_4)
print(mtrx_3 + mtrx_4)
