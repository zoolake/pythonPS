import collections
import copy
import itertools


def bfs(greens, reds, board, N, M):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]

    # visited[row][col] = [시간, 색깔]
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

    # 배양액들을 뿌려준다.
    queue = collections.deque()
    for row, col in greens:
        visited[row][col] = [0, -1]
        queue.append((row, col, 0, -1))
    for row, col in reds:
        visited[row][col] = [0, 1]
        queue.append((row, col, 0, 1))

    # 시뮬레이션 진행
    flowers = 0
    while queue:
        row, col, time, color = queue.popleft()

        # 해당 지점이 꽃이 되어서 더 이상 퍼질 수 없는 경우
        if visited[row][col][1] == 3:
            continue

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            # 범위 내부 + 호수가 아닌 경우
            if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] != 0:
                # 한번도 방문하지 않은 경우
                if visited[nrow][ncol] == [0, 0]:
                    visited[nrow][ncol] = [time + 1, color]
                    queue.append((nrow, ncol, time + 1, color))

                # 초록색 배양액과 빨간색 배양액이 동일한 시간에 만나는 경우
                if visited[nrow][ncol] == [time + 1, -color]:
                    flowers += 1
                    visited[nrow][ncol] = [time + 1, 3]

    return flowers


N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 배양액을 뿌릴 수 있는 칸을 구해놓는다.
yellow_ground = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            yellow_ground.append((r, c))

# 어떻게 배양액을 뿌릴건지 정한다.
answer = 0
for combination in itertools.combinations(yellow_ground, G + R):
    # 초록색을 어디다가 뿌릴지를 정한다.
    greens_combinations = itertools.combinations(combination, G)
    for greens_combination in greens_combinations:
        greens = set(greens_combination)
        reds = set(combination) - greens

        copy_board = copy.deepcopy(board)
        answer = max(answer, bfs(greens, reds, copy_board, N, M))

print(answer)
