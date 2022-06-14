# dp 배열 초기화
dp = [1] * 10001

# 2를 더하는 경우
for i in range(2, 10001):
    dp[i] += dp[i - 2]
# 3을 더하는 경우
for i in range(3, 10001):
    dp[i] += dp[i - 3]

# 입출력
T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
