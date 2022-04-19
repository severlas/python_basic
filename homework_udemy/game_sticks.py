sticks_check = 10
sticks_output = sticks_check * '| '


def output_start_game():
    sticks_c = 10
    sticks_o = sticks_c * '| '
    print(f'      *** GAME_TO_STICKS ***\n'
          f'Все просто, тяни по очереди палочки,\n'
          f' кто последний тянет тот проиграл!\n'
          f'  Начнем -> сейчас палочек: {sticks_c}\n'
          f'       {sticks_o}')


output_start_game()

player_1 = input('Введите имя игрока: ')
player_2 = input('Введите имя игрока: ')


def f_control_sticks(sticks, player_s):
    return sticks - player_s


while True:
    player_1_input = int(input(f'{player_1} бери палочки (от 1 до 3): '))
    sticks_check = f_control_sticks(sticks_check, player_1_input)
    sticks_output = sticks_check * '| '
    if sticks_check != 0:
        print(f'{sticks_output}: {sticks_check}')
    else:
        print(f'Палочек не осталось, {player_1} ты проиграл(а)!')
        question_to_exit = input('Хотите сыграть еще раз? (Д (да) / Любая клавиша (нет)): ').upper()
        if question_to_exit == 'Д':
            output_start_game()
            sticks_check = 10
            continue
        else:
            break
    player_2_input = int(input(f'{player_2} бери палочки (от 1 до 3): '))
    sticks_check = f_control_sticks(sticks_check, player_2_input)
    sticks_output = sticks_check * '| '
    if sticks_check != 0:
        print(f'{sticks_output}: {sticks_check}')
    else:
        print(f'Палочек не осталось, {player_2} ты проиграл(а)!')
        question_to_exit = input('Хотите сыграть еще раз? (Д (да) / Любая клавиша (нет)): ').upper()
        if question_to_exit == 'Д':
            output_start_game()
            sticks_check = 10
            continue
        else:
            break
