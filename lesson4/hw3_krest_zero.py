def print_field(field):
    for i in range(0,len(field)):
        print('*' * 13)
        print('* ',end='')
        for j in range(0,len(field[i])):
            element = field[i][j]
            if element == 1:
                print('X','* ',end='')
            elif element == 2:
                print('0', '* ', end='')
            else:
                print(' ', '* ', end='')
        print()
    print('*' * 13)


def make_move(field):
    while True:
        try:
            adress = input("Введите пожалуйста адрес, куда выполнить ход: ").split(',')
            row = int(adress[0]) - 1
            column = int(adress[1]) - 1
            true_range = range(0,3)
            if not row in  true_range or not column in true_range:
                print("Введите число от 1 до 3")
                continue
            if field[row][column] == 0:
                field[row][column] = 1
            else:
                print("Это поле уже занято")
                continue
            break
        except TypeError:
            print("Введите число!")
            continue
    return field


def make_move_computer(field):
    r = range(0, len(field))
    for i in r:
        try:
            if check_where_to_move(field):
                break
            else:
                if field[1][1] == 0:
                    field[1][1] = 2
                else:
                    index = field[i].index(0)
                    field[i][index] = 2
                break
        except ValueError:
            continue
    return field

def check_where_to_move(field):
    r = range(0, len(field))
    for i in r:
        count = 0
        for j in r:
            if field[i][j] == 1:
                count +=1
        if count > 1:
            try:
                index = field[i].index(0)
                field[i][index] = 2
                return True
            except ValueError:
                continue
    for i in r:
        count = 0
        for j in r:
            if field[j][i] ==1:
                count +=1
        if count > 1:
            for j in r:
                if field[j][i] == 0:
                    field[j][i] = 2
                    return True
            break
    count = 0
    for i in r:
        if field[i][i] == 1:
            count +=1
    if count > 1:
        for i in r:
            if field[i][i]==0:
                field[i][i] = 2
                return True
    count = 0
    j = 0
    for i in range(2, -1, -1):
        if field[j][i] == 1:
            count +=1
        j += 1
    if count > 1:
        j = 0
        for i in range(2, -1, -1):
            if field[j][i]==0:
                field[j][i] = 2
                return True
            j +=1
    return False

def transpose(matrix):
    return list(map(list,zip(*matrix)))

def check_if_the_game_end(field):
    if not check_matrix(field, False):
        return False
    field = transpose(field)
    if not check_matrix(field, False):
        return False
    field = transpose(field)
    if not check_matrix(field, True):
        return False
    return True

def check_matrix(field, diagonal):
    r = range(len(field))
    man = 0
    comp = 0
    if not diagonal:
        for i in r:
            man = 0
            comp = 0
            for j in r:
                element = field[i][j]
                if element == 1:
                    man += 1
                elif element == 2:
                    comp += 1
            if man == 3:
                print("You win!!!")
                return False
            elif comp == 3:
                print("Comp wins!!!")
                return False
    else:
        for i in r:
            element = field[i][i]
            if element == 1:
                man += 1
            elif element == 2:
                comp += 1
        if man == 3:
            print("You win!!!")
            return False
        elif comp == 3:
            print("Comp wins!!!")
            return False
        man = 0
        comp = 0
        j = 0
        for i in range(2,-1, -1):
            element = field[j][i]
            if element == 1:
                man += 1
            elif element == 2:
                comp += 1
            j += 1
        if man == 3:
            print("You win!!!")
            return False
        elif comp == 3:
            print("Comp wins!!!")
            return False
    for i in r:
        for j in r:
            if field[i][j] == 0:
                return True
    print("Ничья!")
    return False

field =[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print_field(field)
while check_if_the_game_end(field):
    make_move(field)
    print_field(field)
    if not check_if_the_game_end(field):
        break
    make_move_computer(field)
    print_field(field)