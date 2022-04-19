def new_list(list_1, list_2):
    list_3 = zip(list_1, list_2)  # Через модуль zip создаем кортежи с двух словарей
    list_3 = list(list_3)
    list_out = [a for b in list_3 for a in b]  # Распаковываем кортежи в словарь использую генератор последовательностей
    return list_out


list_a = input('Введите первый список, через пробел: \t') .split(' ')
list_b = input('Введите второй список, через пробел: \t') .split(' ')
output_list = new_list(list_a, list_b)
print(output_list)
