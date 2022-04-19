import random
print('*** ИГРА УГАДАЙ ЧИСЛО ОТ 1 ДО 50 ЗА 6 ПОПЫТОК ***')
number_r = random.randint(1, 50)
limit_game = 0
while True:
    number_input = int(input('Вводи число: '))
    limit_game += 1
    if number_input != number_r and limit_game == 6:
        print(f'Проиграл, попытки закончились! \n Загаданное число {number_r}')
        break
    if number_input > number_r:
        print('Число меньше!')
    if number_input < number_r:
        print('Число больше!')
    if number_input == number_r:
        print(f'Число отгадано, за {limit_game} попыток!')
        break

