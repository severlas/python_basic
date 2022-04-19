import random
rsp_list = ['R', 'S', 'P']
while True:
    rsp_random = random.choice(rsp_list)
    game_input = input('R - камень, S - ножницы, P - бумага: ')
    print(rsp_random)
    print(game_input)
    win_combination = [('R', 'S'), ('S', 'P'), ('P', 'R')]
    if rsp_random == game_input:
        print('Ничья!')
    elif (rsp_random, game_input) in win_combination:
        print('Вы проиграли!')
    else:
        print('Вы выиграли!')
    question = input('Хотите сыграть еще раз? ( Y / N ): ')
    if question == 'Y':
        continue
    elif question == 'N':
        print('Игра закрыта...')
        break
