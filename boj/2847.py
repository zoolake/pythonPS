# input
N = int(input())
nums = [int(input()) for _ in range(N)]

answer = 0
for i in range(N - 2, -1, -1):
    # 뒤에서 부터 순회하면서 nums[cur] >= nums[cur+1] 인 경우 검사
    if nums[i] >= nums[i + 1]:
        answer += nums[i] - (nums[i + 1] - 1)
        nums[i] = nums[i + 1] - 1
print(answer)
