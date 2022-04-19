hello = str(print('Приветствуем, мы поможем подобрать вам фильм к просмотру с учетом ваших данных'))
name = str(input('Введите ваше имя?'))
age = int(input('Введите ваш возраст?'))
gender = str(input('Введите ваш пол, если мужской вводи "М", если женский вводи "Ж"'))
# Задаем переменные для системы баллов
bonus_1 = 0  # Рекомендация к просмотру 'StarWars' или 'Мандалорец'
bonus_2 = 0  # Рекомендация к просмотру 'Трансформеры'
bonus_3 = 0  # Рекомендация к просмотру 'Инсургент'
bonus_4 = 0  # Рекомендация к просмотру 'TMNT'
bonus_5 = 0  # Рекомендация к просмотру 'Дурак'
if 'admin' in name:
    print("Привет, повелитель!")
if ((gender == 'М') and (age > 10) and (age < 14)) or ((age > 30) and (gender == 'М')):
    bonus_1 = 5  # Соответствие по возрасту и полу (2+3 у.е)
elif (age > 22) and (age < 32) and (gender == 'Ж'):
    bonus_2 = 5
elif (age < 16) and (gender == 'Ж'):
    bonus_3 = 5
elif (age < 12) and (gender == 'М'):
    bonus_4 = 5
elif name == 'Женя':
    bonus_5 = 4  # Соответствие по имени имеет самый большой вес в условии (4 у.е.)
elif gender == 'М':
    bonus_1 = 3  # Соответствие по полу имеет второй по величине вес (3 у.е.)
elif gender == 'Ж':
    bonus_2 = 3
elif (age > 10) and (age < 14) or (age > 30):
    bonus_1 = 2  # Соответствие по возрасту имеет вес (2 у.е.)
elif (age > 22) and (age < 32):
    bonus_2 = 2
elif age < 16:
    bonus_3 = 2
elif age < 12:
    bonus_4 = 2
# Проверяем, какая рекомендация набрала больше баллов
if (bonus_1 > bonus_2) and (bonus_1 > bonus_3) and (bonus_1 > bonus_4) and (bonus_1 > bonus_5):
    print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'")
elif (bonus_2 > bonus_1) and (bonus_2 > bonus_3) and (bonus_2 > bonus_4) and (bonus_2 > bonus_5):
    print("Советую Вам посмотреть 'Трансформеры'")
elif (bonus_3 > bonus_1) and (bonus_3 > bonus_2) and (bonus_3 > bonus_4) and (bonus_3 > bonus_5):
    print("Советую Вам посмотреть 'Инсургент'")
elif (bonus_4 > bonus_1) and (bonus_4 > bonus_2) and (bonus_4 > bonus_3) and (bonus_4 > bonus_5):
    print("Советую Вам посмотреть 'TMNT'")
elif (bonus_5 > bonus_1) and (bonus_5 > bonus_2) and (bonus_5 > bonus_3) and (bonus_5 > bonus_4):
    print("Советую Вам посмотреть 'Дурак'")
if name == 'Guido':
    print("Огромное спасибо!")
