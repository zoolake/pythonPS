count = 0
drow = [-1, -1, -1, 0, 1, 1, 1, 0]
dcol = [-1, 0, 1, 1, 1, 0, -1, -1]


def solution(word, board, N, M):
    global count

    # word의 첫 단어와 일치하는 칸에서 시작
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == word[0]:
                dfs(word[0], (i, j), word, board, N, M)
    return count


def dfs(temp, pos, word, board, N, M):
    global count, drow, dcol

    if temp == word:
        count += 1
        return

    for i in range(8):
        nrow = pos[0] + drow[i]
        ncol = pos[1] + dcol[i]

        if nrow < 0:
            nrow = N - 1
        elif nrow >= N:
            nrow = 0

        if ncol < 0:
            ncol = M - 1
        elif ncol >= M:
            ncol = 0

        if board[nrow][ncol] == word[len(temp)]:
            dfs(temp + board[nrow][ncol], (nrow, ncol), word, board, N, M)

    return


N, M, K = map(int, input().split())
board = []
for _ in range(N):
    line = list(input())
    board.append(line)

table = dict()
for _ in range(K):
    word = input()
    if word not in table:
        table[word] = solution(word, board, N, M)
        print(table[word])
    else:
        print(table[word])
