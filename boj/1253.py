N = int(input())

nums = list(map(int, input().split()))
nums.sort()

answer = set()
for i in range(N):
    target = nums[i]

    temp = nums[:i] + nums[i + 1:]
    left, right = 0, N - 2
    while left < right:
        total = nums[left] + nums[right]
        # "좋은 수" 인 경우
        if target == total:
            answer.add(i)
            break

        if target < total:
            right -= 1
        else:
            left += 1

print(len(answer))
