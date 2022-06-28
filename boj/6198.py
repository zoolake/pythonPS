import sys

input = sys.stdin.readline

N = int(input())
buildings = []
for _ in range(N):
    buildings.append(int(input()))

stack = []
table = [0] * N
for index in range(N - 1, -1, -1):
    height = buildings[index]

    count = 0
    max_count = 0
    while stack:
        if height <= stack[-1][1]:
            break

        top = stack.pop()
        count += 1
        count += table[top[0]]

    table[index] = count
    stack.append((index, height))

print(sum(table))
