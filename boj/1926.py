import collections

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


def bfs(queue, board, visited, n, m, area):
    global drow, dcol

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_valid(board, m, n, ncol, nrow, visited):
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True
                area += 1
    return area


def is_valid(board, m, n, ncol, nrow, visited):
    if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and board[nrow][ncol] == 1:
        return True
    return False


n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

queue = collections.deque()
visited = [[False] * m for _ in range(n)]

count = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = True
            count += 1
            max_area = max(max_area, bfs(queue, board, visited, n, m, 1))

print(count)
print(max_area)
