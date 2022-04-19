def distance_3d(x_1, y_1, z_1, x_2=0, y_2=0, z_2=0):
        distance: float = ((x_1 - x_2)**2) + ((y_1 - y_2)**2)+((z_1 - z_2)**2)  # Формула для вычисления длины
        distance = abs((distance)**0.5)
        distance = round(distance, 2)  #  Округляем значение до двух знаков после запятой
        return distance
print('Введите координаты первых точек в пространстве: ')  # Получаем значения первых 3-х точек
x_1 = float(input('x_1 =  '))
y_1 = float(input('y_1 =  '))
z_1 = float(input('z_1 =  '))
answer = input('Если нужны координаты x_2, y_2, z_2, введите (1) \t')  # При необходимости берем вторые 3 точки
if answer == '1':
    x_2 = float(input('x_2 =  '))
    y_2 = float(input('y_2 =  '))
    z_2 = float(input('z_2 =  '))
    distance_print = distance_3d(x_1, y_1, z_1, x_2, y_2, z_2)  # Вычисляем длину с 6-ю точками
else:
    distance_print = distance_3d(x_1, y_1, z_1)  # Вычисляем длину если 3 точки дефолтные = 0 и 3 точки от пользователя
print(f'Растояние между точками: {distance_print}')
