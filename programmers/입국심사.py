import sys


def solution(n, times):
    answer = sys.maxsize

    # [최악의 경우]
    # 심사관: 10^5명 / 각 심사관 별 심사 시간: 10^9분 / 총 심사 대상자: 10^9명
    # 최대 시간: 10^9 * (10^9 / 10^5)
    left, right = 0, 10000000000000

    while left <= right:
        mid = (left + right) // 2
        # 순회를 하면서 몇 명의 고객을 처리할 수 있는지 확인
        total = 0
        for time in times:
            total += (mid // time)

        if total >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    return answer