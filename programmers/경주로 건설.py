import heapq
import sys


def solution(board):
    size = len(board)
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]
    queue = []
    visited = [[[sys.maxsize] * 2 for _ in range(size)] for _ in range(size)]
    heapq.heappush(queue, (0, [0, 0, -1]))
    visited[0][0][0] = 0
    visited[0][0][1] = 0

    while queue:
        current = heapq.heappop(queue)[1]

        for i in range(4):
            nrow = current[0] + drow[i]
            ncol = current[1] + dcol[i]
            direction = i // 2

            # 범위를 나가지 않고, 벽이 아니고
            if 0 <= nrow < size and 0 <= ncol < size and board[nrow][ncol] != 1:
                # 시작 지점인 경우
                if current[2] == -1:
                    heapq.heappush(queue, (0, [nrow, ncol, direction]))
                    visited[nrow][ncol][direction] = visited[current[0]][current[1]][direction] + 100
                else:
                    # 직진
                    if direction == current[2]:
                        # 이전에 방문한 적이 있다면, 비용이 더 작은 경우에만 다시 방문할 수 있다.
                        if visited[nrow][ncol][direction] > visited[current[0]][current[1]][current[2]] + 100:
                            heapq.heappush(queue, (0, [nrow, ncol, direction]))
                            visited[nrow][ncol][direction] = visited[current[0]][current[1]][current[2]] + 100
                    # 코너
                    else:
                        # 이전에 방문한 적이 있다면, 비용이 더 작은 경우에만 다시 방문할 수 있다.
                        if visited[nrow][ncol][direction] > visited[current[0]][current[1]][current[2]] + 600:
                            heapq.heappush(queue, (1, [nrow, ncol, direction]))
                            visited[nrow][ncol][direction] = visited[current[0]][current[1]][current[2]] + 600

    return min(visited[size - 1][size - 1][0], visited[size - 1][size - 1][1])
