# input
N = int(input())

nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
