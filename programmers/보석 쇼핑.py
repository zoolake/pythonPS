import collections
import sys


# 투 포인터 + 슬라이딩 윈도우
def solution(gems):
    answer = [0, sys.maxsize]

    # 보석의 종류 저장
    gems_set = set()
    for gem in gems:
        gems_set.add(gem)

    left, right = 0, 0
    window = collections.defaultdict(int)
    window[gems[0]] += 1
    while left <= right:
        # 모든 종류의 보석을 구매 못하는 경우
        if len(window) < len(gems_set) and right < len(gems) - 1:
            right += 1
            window[gems[right]] += 1
        # 모든 종류의 보석을 구매 할 수 있는 경우
        elif len(window) == len(gems_set):
            if (right - left) < (answer[1] - answer[0]):
                answer = [left + 1, right + 1]
            # left 포인터를 오른쪽으로 한 칸 이동 -> window에서 기존 left 포인터가 가리키는 보석의 수를 줄여준다.
            left = move_left(gems, left, window)

        # right 포인터가 끝에 도달한 경우 left를 계속 움직여준다.
        elif right == len(gems) - 1:
            left = move_left(gems, left, window)

    return answer


def move_left(gems, left, window):
    window[gems[left]] -= 1
    if window[gems[left]] == 0:
        del window[gems[left]]
    left += 1
    return left
