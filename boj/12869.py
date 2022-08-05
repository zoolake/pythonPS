import itertools
import sys

N = int(input())
robots = list(map(int, input().split()))

modes = list(itertools.permutations([1, 3, 9]))
dp = [[[sys.maxsize] * 6 for _ in range(61)] for _ in range(N)]

for time in range(61):
    for mode in range(6):
        for robot in range(N):
            if time == 0:
                dp[robot][time][mode] = robots[robot]
            else:
                for k in range(6):
                    temp = dp[robot][time - 1][k] - modes[mode][robot] if dp[robot][time - 1][k] - modes[mode][robot] > 0 else 0
                    dp[robot][time][mode] = min(dp[robot][time][mode], temp)

answer = sys.maxsize
for time in range(61):
    for mode in range(6):
        for robot in range(N):
            if dp[robot][time][mode] != 0:
                break

        else:
            answer = min(answer, time)

print(answer)
