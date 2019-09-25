# task2
# Напишите программу, которая определяет положение точки относительно
# выпуклого четырехуголника в двумерном пространстве. Координаты
# фигуры считываются из файла №1. Это вершины четырехугольника, которые
# располагаются в порядке обхода фигуры по часовой стрелке. Пример:
# 0 0
# 0 5.5
# 5.5 5.5
# 5.5 0
# Координаты точек считываются из файла №2. Пример:
# 1.3 1.23
# 10 9
# 0 3
# 5.5 5.5
# 0 -1
# Файлы передаются программе в качестве аргументов: файл с координатами
# четырехугольника - аргумент 1; файл с координатами точек - аргумент 2.
# Количество точек от 1 до 100. Координаты четырехугольника и точек -
# в диапазоне float. Вывод каждого положения точки заканчивается символом
# новой строки.
# Соответствие ответов:
# 0 - точка на одной из вершин;
# 1 - точка на одной из сторон;
# 2 - точка внутри;
# 3 - точка снаружи.


import copy, math, sys


# Класс Точка
class Point:

    # Конструктор
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Переопределение функций вывода на экран
    def __str__(self):
        return 'x={}, y={}'.format(self.__x, self.__y)

    # Переопределение оператора сравнения ==
    def __eq__(self, other):
        if self.__x == other.x and self.__y == other.y:
            return True
        else:
            return False

    # Переопределение оператора сложения +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Переопределение оператора вычитания -
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Переопредение оператора умножения *:
    # для объектов класса будет вычисляться векторное произведение
    def __mul__(self, other):
        return self.x * other.y - self.y * other.x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


# Класс Четырехугольник
class Tetragon:

    # Конструктор
    def __init__(self, points):
        self.__points = []
        for p in points:
            self.__points.append(p)

    # Переопределение метода вывода на экран
    def __str__(self):
        out_line = 'Четырехугольник:'
        for p in self.__points:
            out_line += '\nx={}, y={}'.format(p.x, p.y)
        return out_line

    # Функция определяет, находится ли точка в вершине
    def is_at_top(self, point):
        for p in self.__points:
            if p == point:
                return True
        return False

    # Функция определяет, находится ли точка на стороне
    def is_on_side(self, point):
        n = len(self.__points)
        for i in range(n - 1):
            # Определяются параметры прямой y=a*x+b, которую можно провести
            # через соседние вершины многоугольника
            p1 = self.__points[i]
            p2 = self.__points[i + 1]
            if p1.x != p2.x:
                a = (p1.y - p2.y) / (p1.x - p2.x)
                b = (p2.y * p1.x - p1.y * p2.x) / (p1.x - p2.x)
                if point.y == a * point.x + b and ((p1.x <= point.x <= p2.x and p1.y <= point.y <= p2.y) or (
                        p2.x <= point.x <= p1.x and p2.y <= point.y <= p1.y)):
                    return True
            elif p1.x == p2.x == point.x and (p1.y <= point.y <= p2.y or p1.y <= point.y <= p2.y):
                return True
        # Определяются параметры прямой y=a*x+b, которую можно провести
        # через первую и последнюю вершины
        p1 = self.__points[n - 1]
        p2 = self.__points[0]
        if p1.x != p2.x:
            a = (p1.y - p2.y) / (p1.x - p2.x)
            b = (p2.y * p1.x - p1.y * p2.x) / (p1.x - p2.x)
            if point.y == a * point.x + b and ((p1.x <= point.x <= p2.x and p1.y <= point.y <= p2.y) or (
                    p2.x <= point.x <= p1.x and p2.y <= point.y <= p1.y)):
                return True
        elif p1.x == p2.x == point.x and (p1.y <= point.y <= p2.y or p1.y <= point.y <= p2.y):
            return True
        else:
            return False

    # Функция определяет, находится ли точка внутри многоугольника.
    # Принцип определения следующий. Пусть 1 и 2 две последовательные вершины
    # многоугольника. Точка P будет находиться внутри многоугольника, если
    # угол 1P2 будет меньше (больше) 180 для всех вершин 1 и 2. Определяем,
    # что угол меньше или больше 180 по его синусу, который вычисляется из
    # векторного произведения векторов P1*P2.
    def is_inside(self, point):
        # Словарь, который хранит количество углов 1P2 с синусами больше, меньше 0
        sin_a = {'-': 0, '0': 0, '+': 0}
        # Вычисляем знаки синусов углов 1P2 для вершин от 0 до n-1
        n = len(self.__points)
        for i in range(n - 1):
            p1 = self.__points[i] - point
            p2 = self.__points[i + 1] - point
            if p1 * p2 > 0:
                sin_a['+'] += 1
            elif p1 * p2 == 0:
                sin_a['0'] += 1
            else:
                sin_a['-'] += 1
        p1 = self.__points[n - 1] - point
        p2 = self.__points[0] - point
        if p1 * p2 > 0:
            sin_a['+'] += 1
        elif p1 * p2 == 0:
            sin_a['0'] += 1
        else:
            sin_a['-'] += 1
        # Если синусы углов имеют только положительные или только отрицательные значения,
        # то точка находится внутри многоугольника
        if (sin_a['-'] != 0 and sin_a['0'] == sin_a['+'] == 0) or (
                sin_a['0'] != 0 and sin_a['-'] == sin_a['+'] == 0) or (
                sin_a['+'] != 0 and sin_a['-'] == sin_a['0'] == 0):
            return True
        else:
            return False


if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 2:
        # Если программа запускается из консоли
        file_name1 = sys.argv[1]  # имя файла с данными четырехугольника
        file_name2 = sys.argv[2]  # имя файла с данными о точках
    else:
        # Если программа запускается не из консоли
        names = input()
        file_name1, file_name2 = names.split(' ')  # имена файлов с данными
    # Считываются координаты четырехугольника
    points = []
    with open(file_name1, 'r') as file:
        for line in file:
            x, y = line.split()
            points.append(Point(float(x), float(y)))
        tetragon = Tetragon(points)
    # Считываются координаты точек
    points = []
    with open(file_name2, 'r') as file:
        for line in file:
            x, y = line.split()
            points.append(Point(float(x), float(y)))
    # Определяется, где точка относительно многоугольника
    for p in points:
        if tetragon.is_at_top(p):
            print('0')
        elif tetragon.is_on_side(p):
            print('1')
        elif tetragon.is_inside(p):
            print('2')
        else:
            print('3')
