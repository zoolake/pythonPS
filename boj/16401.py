M, N = map(int, input().split())
snacks = list(map(int, input().split()))

left, right = 1, max(snacks)

answer = 0
while left <= right:
    mid = (left + right) // 2

    # mid 길이로 과자를 받을 수 있는 최대 인원을 구하기
    count = 0
    for snack in snacks:
        if snack >= mid:
            count += (snack // mid)

    if count >= M:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(int(answer))
