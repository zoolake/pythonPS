import sys

input = sys.stdin.readline

word = '0' + input().rstrip()
N = len(word)

# 1행: 마름모 ON / 2행: 마름모 OFF
dp = [[0] * N for _ in range(2)]
dp[0][0] = 1

for i in range(1, N):
    alphabet = word[i]
    # 소문자
    if alphabet.islower():
        # 마름모 ON
        dp[0][i] = dp[0][i - 1] + 2
        # 마름모 OFF
        dp[1][i] = min(dp[0][i - 1] + 2, dp[1][i - 1] + 1)
    # 대문자
    elif alphabet.isupper():
        # 마름모 ON
        dp[0][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 2)
        # 마름모 OFF
        dp[1][i] = dp[1][i - 1] + 2

print(min(dp[0][N - 1], dp[1][N - 1]))
