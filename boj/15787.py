import sys


def move_back(train):
    for i in range(20, 0, -1):
        train[i] = train[i - 1]


def move_forward(train):
    for i in range(1, 21):
        train[i] = train[i + 1]


input = sys.stdin.readline
N, M = map(int, input().split())
trains = [[False] * 22 for _ in range(N + 1)]
for _ in range(M):
    command = list(map(int, input().split()))
    op, train = command[0], command[1]
    if op == 1:
        seat = command[2]
        trains[train][seat] = True
    if op == 2:
        seat = command[2]
        trains[train][seat] = False
    if op == 3:
        move_back(trains[train])
    if op == 4:
        move_forward(trains[train])

pattern_set = set()
for train in range(1, N + 1):
    pattern = ''
    for seat in range(1, 20 + 1):
        if trains[train][seat]:
            pattern += 'O'
        else:
            pattern += 'X'

    if pattern not in pattern_set:
        pattern_set.add(pattern)

print(len(pattern_set))
