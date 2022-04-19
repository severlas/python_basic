def decor_speed_function(function):
    memory_dict = dict()

    def wrapper(*args):
        if args not in memory_dict:  # Проверяем условие, есть ли элементы в нашем словаре
            memory_dict[args] = function(*args)  # Записываем в словарь, элементы как ключ, результат ф-и как значение
        return memory_dict[args]  # Возвращаем результат ф-и

    return wrapper


@decor_speed_function
def function_sum(*args):
    sum_elem = 0
    for i in args:
        sum_elem = sum_elem + i
    return sum_elem
