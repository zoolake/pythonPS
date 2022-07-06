import sys

# input
N = int(input())
nums = sorted(list(map(int, input().split())))
# solution
min_total = sys.maxsize
answer = []
for i in range(N - 2):
    first = nums[i]
    left = i + 1
    right = N - 1

    flag = False
    while left < right:
        second = nums[left]
        third = nums[right]

        total = first + second + third

        # 정답
        if total == 0:
            flag = True
            answer = [first, second, third]
            break

        # 0에 더 근접한 경우
        if abs(total) < min_total:
            min_total = abs(total)
            answer = [first, second, third]
        # 음수
        if total < 0:
            left += 1
        else:
            right -= 1

    # 정답을 찾아서 while 문을 탈출한 경우
    if flag:
        break

print(*answer)
