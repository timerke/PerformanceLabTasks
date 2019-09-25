# task1
# Напишите программу, которая рассчитывает и подает в стандартный вывод
# следующие значения:
# - 90 перцентиль;
# - медиана;
# - максимальное значение;
# - минимальное значение;
# - среднее значение.
# Входные данные:
# Данные для расчетов считываются из файла, путь к которому подается в
# виде аргумента. Числа в файле в пределах от -32768 до 32767. Каждое
# число с новой строки. В файлах не более 1000 строк.
# Вывод:
# Вывод значений в указанной последовательности, каждое значение
# заканчивается символом новой строки. Все значения с точностью до
# сотых: 2.50 2.00 0.03.


import math, sys


# Функция для вычисления перцентиля
def percentile(data,  # данные для расчета
               percent):  # величина процента перцентиля
    i = percent * len(data)
    if i.is_integer():
        i = int(i)
        p = (data[i - 1] + data[i]) / 2
    else:
        i = math.ceil(i)
        p = data[i - 1]
    return '{:.2f}'.format(p)


# Функция для вычисления медианы
def median(data):
    n = len(data)
    if n % 2:
        i = math.ceil(n / 2)
        m = data[i]
    else:
        i = int(n / 2)
        m = (data[i - 1] + data[i]) / 2
    return '{:.2f}'.format(m)


# Функция для вычисления среднего значения
def mean(data):
    m = 0
    for element in data:
        m += element
    n = len(data)
    m /= n
    return '{:.2f}'.format(m)


if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 1:
        # Если программа запускается из консоли
        file_name = sys.argv[1]  # имя файла с данными
    else:
        # Если программа запускается не из консоли
        file_name = input()  # имя файла с данными
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(int(line))
    # Список с данными сортируется по возрастанию
    data.sort()
    # Вычисляется перцентиль
    percent = 0.9
    p = percentile(data, percent)
    print(p)
    # Вычисляется медиана
    m = median(data)
    print(m)
    # Максимальное значение
    max_value = max(data)
    print(max_value)
    # Минимальное значение
    min_value = min(data)
    print(min_value)
    # Вычисляется среднее значение
    mean_value = mean(data)
    print(mean_value)
