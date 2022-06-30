import collections

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


def melt(board, memo_board, glaciers, N, M):
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                continue

            sea_count = 0
            for d in range(4):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] == 0:
                    sea_count += 1
            memo_board[row][col] = sea_count

    for row in range(N):
        for col in range(M):
            if board[row][col] - memo_board[row][col] > 0:
                board[row][col] -= memo_board[row][col]
            else:
                if board[row][col] > 0:
                    board[row][col] = 0
                    glaciers -= 1

    return glaciers


def bfs(board, glaciers, N, M):
    start_row, start_col = 0, 0
    for row in range(N):
        for col in range(M):
            if board[row][col] > 0:
                start_row = row
                start_col = col
                break

    queue = collections.deque()
    visited = [[False] * M for _ in range(N)]
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True

    count = 1
    while queue:
        row, col = queue.popleft()

        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol] and board[nrow][ncol] > 0:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True
                count += 1

    return 2 if count < glaciers else 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
memo_board = [[0] * M for _ in range(N)]

glaciers = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            glaciers += 1

time = 0
flag = True
while glaciers > 0:
    time += 1
    # 1. 녹인다
    glaciers = melt(board, memo_board, glaciers, N, M)
    # 2. 그래프 탐색 진행
    if bfs(board, glaciers, N, M) > 1:
        print(time)
        flag = False
        break

if flag:
    print(0)
