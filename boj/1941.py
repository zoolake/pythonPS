import collections
import itertools


def bfs(combination, board):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]

    start_row, start_col = combination[0]
    y_count = 0

    queue = collections.deque()
    visited = [False] * 7

    queue.append((start_row, start_col))
    visited[0] = True

    while queue:
        row, col = queue.popleft()

        if board[row][col] == 'Y':
            y_count += 1

        if y_count > 3:
            return False

        for index, pos in enumerate(combination):
            if visited[index]:
                continue

            # 방문하지 않고 상하좌우 중 하나로 인접해 있다면
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                if nrow == pos[0] and ncol == pos[1]:
                    queue.append([nrow, ncol])
                    visited[index] = True

    for flag in visited:
        if not flag:
            return False

    else:
        return True


board = [list(input()) for _ in range(5)]

s_count = 0
pos_list = []
for row in range(5):
    for col in range(5):
        if board[row][col] == 'S':
            s_count += 1
        pos_list.append([row, col])
# S < 4 이면 불가능
if s_count < 4:
    print(0)
else:
    answer = 0
    # 25C7 = 480,700
    for combination in itertools.combinations(pos_list, 7):
        if bfs(combination, board):
            answer += 1
    print(answer)
