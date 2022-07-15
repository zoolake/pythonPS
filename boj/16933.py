import collections
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

queue = collections.deque()
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

queue.append((0, 0, 0))  # (row, col, wall)
visited[0][0][0] = 1  # (row, col, wall)

is_day = True
move = 1
while queue:
    # 같은 날 일괄처리
    for _ in range(len(queue)):
        row, col, wall = queue.popleft()
        # 도착
        if row == N - 1 and col == M - 1:
            print(move)
            sys.exit()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            nwall = wall + 1
            # 범위 밖
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
                continue
            # 벽x
            if board[nrow][ncol] == '0' and not visited[nrow][ncol][wall]:
                queue.append((nrow, ncol, wall))
                visited[nrow][ncol][wall] = move + 1
            # 벽o (낮에만 부술 수 있음)
            elif wall < K and not visited[nrow][ncol][nwall]:
                # 낮
                if is_day:
                    queue.append((nrow, ncol, nwall))
                    visited[nrow][ncol][nwall] = move + 1
                # 밤
                else:
                    queue.append((row, col, wall))

    is_day = not is_day
    move += 1

print(-1)
