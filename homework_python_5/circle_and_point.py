user_input = input('Введите три числа \n'
                   'x (координату точки по оси Х),'
                   'y (координату точки по оси Y),'
                   'r (радиус окружности): \t') .split(', ')
user_input = list(map(float, user_input))  # Приводим список к типу "float"
x = user_input[0]  # Достаем со списка значение "x"
y = user_input[1]  # Достаем со списка значение "y"
r = user_input[2]  # Достаем со списка значение "r"
if (abs(x)**2) + (abs(y)**2) <= r**2:  # Берем значение по модулю и сравниваем с радиусом
    print(True)
else:
    print(False)
