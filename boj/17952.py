import sys

input = sys.stdin.readline

N = int(input())

current_hw = []
stack = []
answer = 0
for _ in range(N):
    line = list(map(int, input().split()))
    # 새로운 과제가 없고 기존에 하고 있던 과제가 있다면 그대로 진행
    if line[0] == 0 and current_hw:
        current_hw[1] -= 1

    # 새로운 과제가 있는 경우
    if line[0] == 1:
        # 기존에 하던 과제가 있는 경우
        if current_hw:
            # 기존에 하던 과제를 스택에 삽입
            stack.append(current_hw[:])
        # 새로운 과제 시작
        current_hw = line[1:]
        current_hw[1] -= 1

    # 기존에 하던 과제가 있고, 해당 과제를 마무리 했다면 직전에 하던 과제를 진행
    if current_hw and current_hw[1] <= 0:
        answer += current_hw[0]
        current_hw = None
        if stack:
            current_hw = stack.pop()

print(answer)
