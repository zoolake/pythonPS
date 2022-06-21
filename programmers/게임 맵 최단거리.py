import collections

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

n, m = 0, 0


def solution(maps):
    global drow, dcol, n, m

    n = len(maps)
    m = len(maps[0])

    queue = collections.deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        row, col, cost = queue.popleft()

        # 도착
        if row == n - 1 and col == m - 1:
            return cost

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if 0 <= nrow < n and 0 <= ncol < m and maps[nrow][ncol] == 1 and not visited[nrow][ncol]:
                queue.append((nrow, ncol, cost + 1))
                visited[nrow][ncol] = True

    return -1
