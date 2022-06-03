# 이분탐색
def solution(stones, k):
    answer = 0

    left, right = 1, 200000000

    while left+1 < right:
        mid = (left + right) // 2
        count = 0
        # 연속으로 0인 구간의 길이가 K인 경우를 검사
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0

            if count == k:
                break

        if k <= count:
            right = mid
        else:
            left = mid

    return right
