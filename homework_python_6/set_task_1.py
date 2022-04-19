n: int
_list = (input('Введите список чисел: \n')).split(', ')
_list = set(_list)
n = len(_list)
print(f'Уникальных чисел : {n}')
