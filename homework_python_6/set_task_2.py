n: int
_list = (input('Введите первый список чисел: \n')).split(', ')
_list_2 = (input('Введите второй список чисел: \n')).split(', ')
_list = set(_list)
_list_2 = set(_list_2)
same_elem = _list.intersection(_list_2)
n = len(same_elem)
print(f'Одновременно в первом и втором списке содержится чисел : {n}')
