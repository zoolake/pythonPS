import itertools
import collections


# 응시자 간 맨해튼 거리 2이하면 안된다.
# 단, 파티션으로 막혀 있는 경우 가능
# P: 응시자가 앉아있는 자리
# O: 빈 테이블
# X: 파티션

def solution(places):
    answer = []
    # 각 TC 검사
    for place in places:
        people = []
        # 응시자의 위치를 찾는다.
        for row in range(5):
            for col in range(5):
                # 응시자인 경우 people에 저장
                if place[row][col] == 'P':
                    people.append([row, col])

        # 응시자가 없거나 한명인 경우
        if len(people) <= 1:
            answer.append(1)
            continue

        # 순회하면서 응시자 간의 맨해튼거리가 2이하인 경우만 파티션 검사
        combinations = list(itertools.combinations(people, 2))
        for data in combinations:
            p1, p2 = data
            if abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) <= 2:
                if not bfs(p1 + [0], p2, place):
                    answer.append(0)
                    break
        else:
            answer.append(1)

    return answer


def bfs(p1, p2, place):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]

    deque = collections.deque()
    visited = [[False] * 5 for _ in range(5)]

    deque.append(p1)
    visited[p1[0]][p1[1]] = True

    while deque:
        row, col, distance = deque.popleft()

        if row == p2[0] and col == p2[1] and distance <= 2:
            return False

        for d in zip(drow, dcol):
            nrow = row + d[0]
            ncol = col + d[1]
            if 0 <= nrow < 5 and 0 <= ncol < 5:
                if not visited[nrow][ncol] and place[nrow][ncol] != 'X':
                    visited[nrow][ncol] = True
                    deque.append([nrow, ncol, distance + 1])

    return True