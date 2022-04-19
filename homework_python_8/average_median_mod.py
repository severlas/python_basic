def math_operation(list_n):
    list_n = sorted(list_n)
    # Расчитваем среднее арифметическое
    check_n = len(list_n)
    average = round(sum(list_n) / check_n, 2)
    # Расчитываем медиану
    if check_n % 2 == 0:
        a = int(check_n / 2)
        b = int(check_n / 2) - 1
        result_a = list_n[a]
        result_b = list_n[b]
        median = (result_a + result_b) / 2
    else:
        result_c = int(check_n / 2)
        median = list_n[result_c]
    # Расчитываем моду
    max_c = 0
    mod = 0
    for i in list_n:
        result_m = list_n.count(i)
        if result_m > max_c:
            max_c = result_m
            mod = list_n[i]
    tuple_result = (f'среднее арифметическое - {average}', f'медиана - {median}', f'мода - {mod}')
    return tuple_result


# Проверка
list_r = [1, 2, 3, 4, 5, 1, 2, 7, 1]
result_function = math_operation(list_r)
print(f'Результат: {result_function}')
