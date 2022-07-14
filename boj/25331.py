import collections
import copy
import sys


def drop_ball(board):
    for col in range(7):
        empty_space = 0
        for row in range(6, -1, -1):
            current_ball = board[row][col]
            if current_ball == 0:
                empty_space += 1
                continue
            else:
                if empty_space > 0:
                    board[row + empty_space][col] = current_ball
                    board[row][col] = 0


def check_vertical_group(board):
    group = []

    drow = [-1, 1]
    for col in range(7):
        queue = collections.deque()
        visited = [False] * 7

        queue.append((6, col))
        visited[6] = True
        temp = [(6, col)]

        while queue:
            r, c = queue.popleft()
            for i in range(2):
                nr = r + drow[i]
                if 0 <= nr < 6 and board[nr][col] > 0 and not visited[nr]:
                    queue.append((nr, col))
                    visited[nr] = True
                    temp.append((nr, col))

        group.append(temp)

    return group


def check_horizontal_group(board):
    group = []
    dcol = [-1, 1]

    visited = [[False] * 7 for _ in range(7)]
    for row in range(7):
        for col in range(7):
            if board[row][col] == 0 or visited[row][col]:
                continue

            queue = collections.deque()
            queue.append((row, col))
            visited[row][col] = True
            temp = [(row, col)]

            while queue:
                r, c = queue.popleft()
                for i in range(2):
                    nc = c + dcol[i]
                    if 0 <= nc < 7 and board[r][nc] > 0 and not visited[r][nc]:
                        queue.append((r, nc))
                        visited[r][nc] = True
                        temp.append((r, nc))

            group.append(temp)

    return group


def process_event(board, vertical_group, horizontal_group):
    remove = []

    for group in vertical_group:
        size = len(group)
        for row, col in group:
            ball = board[row][col]
            if size == ball:
                remove.append((row, col))

    for group in horizontal_group:
        size = len(group)
        for row, col in group:
            ball = board[row][col]
            if size == ball:
                remove.append((row, col))

    flag = False
    for row, col in remove:
        board[row][col] = 0
        flag = True

    return flag


def calculate(board):
    count = 0
    for i in range(7):
        for j in range(7):
            if board[i][j] != 0:
                count += 1
    return count


board = [list(map(int, input().split())) for _ in range(7)]
ball = int(input())

answer = sys.maxsize
for i in range(7):
    copy_board = copy.deepcopy(board)
    copy_board[0][i] = ball
    while True:
        # 공을 떨어뜨린다.
        drop_ball(copy_board)
        # 그룹을 확인
        vertical_group = check_vertical_group(copy_board)
        horizontal_group = check_horizontal_group(copy_board)
        # 삭제 이벤트 처리
        if not process_event(copy_board, vertical_group, horizontal_group):
            break

    answer = min(answer, calculate(copy_board))

print(answer)
