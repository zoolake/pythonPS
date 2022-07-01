import collections

N, d, k, c = map(int, input().split())

dishes = [int(input()) for _ in range(N)]

left, right = 0, k - 1
window = collections.deque(dishes[left:right + 1])

# 현재 window에 어떤 종류의 초밥이 몇개 있는지 저장하는 테이블 초기화
table = dict({c: 1})
for dish in window:
    if dish in table:
        table[dish] += 1
    else:
        table[dish] = 1

answer = len(table)
if N != k:
    # 슬라이딩 윈도우 진행
    for i in range(1, N):
        left = i
        right = left + (k - 1) if left + (k - 1) < N else (left + (k - 1)) % N
        # 윈도우의 가장 왼쪽 제거
        front = window[0]
        table[front] -= 1
        if table[front] == 0:
            del table[front]
        window.popleft()
        # 윈도우의 오른쪽에 새로운 원소 추가
        back = dishes[right]
        window.append(back)
        if back in table:
            table[back] += 1
        else:
            table[back] = 1
        # answer 갱신
        answer = max(answer, len(table))

print(answer)
