import bisect
import sys

# 입력
N, M = map(int, input().split())

grade = []
limit = []
for _ in range(N):
    key, value = sys.stdin.readline().rstrip().split()
    grade.append(key)
    limit.append(int(value))

for _ in range(M):
    power = int(sys.stdin.readline().rstrip())
    index = bisect.bisect_left(limit, power)
    print(grade[index])
