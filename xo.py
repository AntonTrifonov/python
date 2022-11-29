import json

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(playar_token):
    while True:
        value = input('Куда поставить: ' + playar_token + ' ? ')
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[value - 1] = playar_token
        break


def check_win(board):
    with open("init.json", "r") as f:
        wins_coord = json.load(f)
    for each in wins_coord:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False
