# input
import collections
import sys

N, M = map(int, input().split())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# solution
answer = sys.maxsize
dcol = [-1, 0, 1]

for i in range(M):
    current = (0, i, -1, board[0][i])

    queue = collections.deque()
    queue.append(current)

    while queue:
        row, col, d, total = queue.popleft()

        if row == N - 1:
            answer = min(answer, total)
            continue

        for j in range(3):
            if j != d:
                nrow = row + 1
                ncol = col + dcol[j]
                if 0 <= nrow < N and 0 <= ncol < M:
                    queue.append((nrow, ncol, j, total + board[nrow][ncol]))

print(answer)