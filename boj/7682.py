# 3칸 이어지는 경우
bingo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
answer = set()


def game(blank, turn, board):
    global answer
    # 1. 3칸이 이어진 경우
    for case in bingo:
        if board[case[0]] == board[case[1]] == board[case[2]] != '.':
            answer.add(''.join(board))
            return
    # 2. 다 차는 경우
    if blank == 0:
        answer.add(''.join(board))
        return

    "X 차례"
    if turn == 1:
        for i in range(9):
            if board[i] == '.':
                board[i] = 'X'
                game(blank - 1, 2, board)
                board[i] = '.'
    else:
        for i in range(9):
            if board[i] == '.':
                board[i] = 'O'
                game(blank - 1, 1, board)
                board[i] = '.'


game(9, 1, ['.'] * 9)
while True:
    board = input()

    if board == 'end':
        break

    if board in answer:
        print('valid')
    else:
        print('invalid')
