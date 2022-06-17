import collections
import sys

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


def spread_fire(fire_list, fire_board, board, R, C):
    global drow, dcol

    queue = collections.deque()

    for fire in fire_list:
        queue.append(fire + [0])
        fire_board[fire[0]][fire[1]] = 0

    while queue:
        row, col, time = queue.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            # 범위 내부 + 벽이 아니고 + 방문한 적이 없는 경우
            if 0 <= nrow < R and 0 <= ncol < C and board[nrow][ncol] != '#' and time + 1 < fire_board[nrow][ncol]:
                queue.append([nrow, ncol, time + 1])
                fire_board[nrow][ncol] = time + 1


def move_player(player, fire_board, board, R, C):
    global drow, dcol

    queue = collections.deque()
    visited = [[False] * C for _ in range(R)]

    queue.append(player + [0])
    visited[player[0]][player[1]] = True

    while queue:
        row, col, time = queue.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            # 탈출한다면
            if nrow < 0 or nrow >= R or ncol < 0 or ncol >= C:
                return time + 1

            if not visited[nrow][ncol] and (board[nrow][ncol] == 'J' or board[nrow][ncol] == '.'):
                if time + 1 < fire_board[nrow][ncol]:
                    queue.append([nrow, ncol, time + 1])
                    visited[nrow][ncol] = True

    return 'IMPOSSIBLE'


if __name__ == "__main__":
    # 입력
    R, C = map(int, input().split())

    player = None
    fire = []

    board = []
    for row in range(R):
        line = input().rstrip()
        board.append(line)
        for col in range(C):
            if line[col] == 'J':
                player = [row, col]
            if line[col] == 'F':
                fire.append([row, col])

    fire_board = [[sys.maxsize] * C for _ in range(R)]
    # 불을 먼저 퍼뜨린다.
    spread_fire(fire, fire_board, board, R, C)
    # 지훈이가 이동한다.
    answer = move_player(player, fire_board, board, R, C)

    print(answer)
