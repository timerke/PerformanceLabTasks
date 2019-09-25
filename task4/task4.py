# task4
# В течении дня в банк заходят люди, для каждого посещения фиксируется время
# захода в банк и время выхода. Банк работает с 8:00 до 20:00. Написать
# программу, которая определяет периоды времени, когда в банке было
# максимальное количество посетителей. Файл содержит информацию о времени
# посещения банка каждым посетителем, округленном до минут. Время входа
# посетителя меньше либо равно времени выхода. Выведите интервалы времени,
# когда в банке было максимальное число посетителей. Начало и конец интервала
# разделяются пробелом. В случае необходимости вывести несколько периодов, в
# качестве разделителя между ними следует использовать символ перевода строки.

import sys

if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 1:
        # Если программа запускается из консоли
        file_name = sys.argv[1]  # имя файла с данными
    else:
        # Если программа запускается не из консоли
        file_name = input()  # имя файла с данными
    #
    intervals = set()  # моменты времени, в которые входят или выходят посетители
    times = []  # список из интервалов времени, в которые посетители были в банке
    with open(file_name, 'r') as file:
        for line in file:
            time1, time2 = line.split()
            time1 = time1.replace(':', '.')
            time1 = float(time1)
            intervals.add(time1)
            time2 = time2.replace(':', '.')
            time2 = float(time2)
            intervals.add(time2)
            times.append([time1, time2])
    intervals = list(intervals)
    intervals.sort()
    customers = []  # список с количеством посетителей в интервалах времени
    for i in range(len(intervals) - 1):
        customers.append(0)
        for j in range(len(times)):
            if times[j][0] <= intervals[i] < intervals[i + 1] <= times[j][1]:
                customers[i] += 1
    max_number = max(customers)
    for i in range(len(intervals) - 1):
        if max_number == customers[i] and (i == 0 or max_number != customers[i - 1]):
            to_write = '{:.2f}'.format(intervals[i]).replace('.', ':')
            print(to_write, end=' ')
        if max_number != customers[i] and max_number == customers[i - 1]:
            to_write = '{:.2f}'.format(intervals[i]).replace('.', ':')
            print(to_write)
