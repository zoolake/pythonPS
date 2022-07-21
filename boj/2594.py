def convert(hour, minute):
    return 60 * hour + minute


N = int(input())

OPEN = convert(10, 0)
CLOSE = convert(22, 0)

time_table = [(OPEN - 1, OPEN)]
for _ in range(N):
    start, end = input().split()

    start, end = convert(int(start[:2]), int(start[2:])) - 10, convert(int(end[:2]), int(end[2:])) + 10
    start = start if start >= OPEN else OPEN
    end = end if end <= CLOSE else CLOSE

    time_table.append((start, end))
time_table.append((CLOSE, CLOSE + 1))

# 시작 시간을 기준 오름차순 정렬
time_table.sort(key=lambda t: t[0])

answer = 0
start, end = time_table[0]
for i in range(1, N + 2):
    if end < time_table[i][0]:
        answer = max(answer, time_table[i][0] - end)
        start, end = time_table[i]
    else:
        end = max(end, time_table[i][1])

print(answer)
