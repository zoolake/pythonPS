import sys


def calc(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


input = sys.stdin.readline
N = int(input())

points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 총 거리 계산
total = 0
for i in range(1, N):
    total += calc(points[i], points[i - 1])

# 최소 거리 계산
answer = sys.maxsize
for i in range(1, N - 1):
    temp = total - calc(points[i], points[i - 1]) - calc(points[i + 1], points[i]) + calc(points[i + 1], points[i - 1])
    answer = min(answer, temp)

print(answer)
