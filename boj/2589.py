import collections

# 너비 우선 탐색 진행
# 더 이상 탐색할 곳이 없다면 탐색을 멈추고 정답 갱신
import sys


def bfs(row, col, N, M, board):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]

    length = 0

    visited = [[sys.maxsize] * M for _ in range(N)]
    visited[row][col] = 0

    deque = collections.deque()
    deque.append((row, col))

    while deque:
        r, c = deque.popleft()

        for i in range(4):
            nr = r + drow[i]
            nc = c + dcol[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 'L':
                if visited[nr][nc] > visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1
                    deque.append((nr, nc))
                    length = max(length, visited[nr][nc])

    return length


N, M = map(int, input().split())
board = [input() for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        # 육지: 탐색을 진행
        if board[i][j] == 'L':
            answer = max(answer, bfs(i, j, N, M, board))

print(answer)
