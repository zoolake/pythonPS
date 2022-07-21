import collections


def find_group(board):
    visited = [[False] * 6 for _ in range(12)]
    group = []
    for row in range(12):
        for col in range(6):
            if board[row][col] != '.' and not visited[row][col]:
                group += bfs(row, col, board, visited)

    return group


def bfs(start_row, start_col, board, visited):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]

    queue = collections.deque()

    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    color = board[start_row][start_col]

    group = [(start_row, start_col)]
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0 <= nrow < 12 and 0 <= ncol < 6 and not visited[nrow][ncol] and board[nrow][ncol] == color:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True
                group.append((nrow, ncol))

    if len(group) >= 4:
        return group

    return []


def boom(delete, board):
    for row, col in delete:
        board[row][col] = '.'


def go_down(board):
    for col in range(6):
        empty = 0
        for row in range(11, -1, -1):
            if board[row][col] == '.':
                empty += 1
            elif empty > 0:
                board[row + empty][col] = board[row][col]
                board[row][col] = '.'


board = [list(input()) for _ in range(12)]
answer = 0
while True:
    delete = find_group(board)
    if not delete:
        break
    boom(delete, board)
    go_down(board)
    answer += 1

print(answer)
