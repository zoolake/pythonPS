import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    cafes = []
    for _ in range(n):
        x, y = map(int, input().split())
        cafes.append((x, y))

    cafes.sort(key=lambda elem: elem[0])

    before_x, before_y = -1, 0
    left = 0
    while left < n:
        # y 축 이동하는 범위를 찾는다.
        x, y = cafes[left]
        right = left + 1
        while right < n:
            if cafes[right][0] != x:
                break
            else:
                right += 1
        # 해당 범위를 직전 좌표의 y값과 가까운 기준으로 오름차순 정렬
        if right - left > 1:
            cafes[left:right] = sorted(cafes[left:right], key=lambda elem: abs(before_y - elem[1]))
        before_x, before_y = cafes[right - 1]
        left = right

    cafe = list(map(int, input().split()))[1:]
    for no in cafe:
        print(*cafes[no - 1])
