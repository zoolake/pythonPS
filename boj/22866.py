import sys


def solution(stack, i):
    global answer, heights, N

    height = heights[i]

    while stack:
        top = heights[stack[-1]]
        if top <= height:
            stack.pop()
        else:
            break

    if not stack:
        answer[i].append([0, sys.maxsize])
    else:
        answer[i].append([len(stack), stack[-1] + 1])

    stack.append(i)


# input
N = int(input())
heights = list(map(int, input().rstrip().split()))

answer = [[] for _ in range(N)]
# 왼쪽
left_stack = []
for i in range(N):
    solution(left_stack, i)

# 오른쪽
right_stack = []
for i in range(N - 1, -1, -1):
    solution(right_stack, i)

# output
for i in range(N):
    left, right = answer[i][0], answer[i][1]
    total = left[0] + right[0]

    if total == 0:
        print(0)
    else:
        # 거리가 가장 가까운 건물의 번호 중 작은 번호로 출력한다.
        index = left[1] if abs(left[1] - (i + 1)) <= abs(right[1] - (i + 1)) else right[1]
        print(total, index)
