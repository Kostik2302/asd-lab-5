def check(game):

    flag_x = 0
    flag_0 = 0
    
    for i in range(3):
        col = game[0][i] + game[1][i] + game[2][i]

        if sum(game[i]) == 3 or col == 3:
            flag_x = 1
        elif sum(game[i]) == 0 or col == 0:
            flag_0 = 1

    cross_1 = game[0][0] + game[1][1] + game[2][2]
    cross_2 = game[0][2] + game[1][1] + game[2][0]

    if cross_1 == 3 or cross_2 == 3:
        flag_x = 1
    elif cross_1 == 0 or cross_2 == 0:
        flag_0 = 1

    if flag_0 == 1 and flag_x == 1:
        return 'Игра сыграна неверно! Победили обе стороны!'
    elif flag_0 == 1:
        return 'Победили нолики!'
    elif flag_x == 1:
        return 'Победили крестики!'
    else:
        return 'Ничья, победителя нет!'
    
game = [[int(i) for i in input(f'Введите {j+1} строку через пробел: "1" - крестик, "0" - нолик: ').split()] for j in range(3)]
    
print(check(game))

