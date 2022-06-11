# 참고: https://staticvoidlife.tistory.com/143

# 입력
import sys


def check(before, after, N):
    for i in range(N):
        if before[i] != after[i]:
            return False

    else:
        return True


def solution(before, after, N):
    count = 0
    for i in range(1, N):
        if before[i - 1] != after[i - 1]:
            before[i - 1] = 0 if before[i - 1] == 1 else 1
            before[i] = 0 if before[i] == 1 else 1
            if i + 1 < N:
                before[i + 1] = 0 if before[i + 1] == 1 else 1
            count += 1

    if check(before, after, N):
        return count
    else:
        return sys.maxsize


N = int(input())
before = list(map(int, input()))
after = list(map(int, input()))

answer = sys.maxsize
# 0번째 스위치를 누르는 경우
copy_before = before[:]
copy_before[0] = 0 if copy_before[0] == 1 else 1
copy_before[1] = 0 if copy_before[1] == 1 else 1
answer = min(answer, 1 + solution(copy_before, after, N))
# 0번째 스위치를 누르지 않는 경우
copy_before = before[:]
answer = min(answer, solution(copy_before, after, N))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
