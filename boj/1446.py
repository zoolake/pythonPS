# 입력
import collections

N, D = map(int, input().split())
dict = collections.defaultdict(list)
for _ in range(N):
    start, end, cost = map(int, input().split())
    dict[end].append((start, cost))

dp = [0] * (D + 1)
for i in range(1, D + 1):
    # 거리 갱신
    dp[i] = dp[i - 1] + 1
    # 지름길 존재 여부 확인 및 필요시 갱신
    if dict[i]:
        for start, cost in dict[i]:
            if dp[i] > dp[start] + cost:
                dp[i] = dp[start] + cost

print(dp[D])
