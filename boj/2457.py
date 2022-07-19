import sys

input = sys.stdin.readline
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def calculate(month, day):
    global months

    sum_months = [0] * 13
    for m in range(1, 13):
        sum_months[m] = sum_months[m - 1] + months[m]

    return sum_months[month - 1] + day


N = int(input())
valid_range_start, valid_range_end = calculate(3, 1), calculate(12, 1)
flowers = []
for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    start, end = calculate(start_month, start_day), calculate(end_month, end_day)
    flowers.append((start, end))

flowers.sort(key=lambda x: x[0])

answer = 1
temp = valid_range_start
start, end = flowers[0]
for i in range(1, len(flowers)):
    flower = flowers[i]

    if flower[0] <= temp < flower[1]:
        end = max(end, flower[1])
    else:
        if flower[0] <= end < flower[1]:
            answer += 1
            temp = end
            end = flower[1]
    # end >= 12월 1일
    if end >= valid_range_end:
        break

# 유효 범위가 아닌 경우
if start > valid_range_start or end < valid_range_end:
    print(0)
else:
    print(answer)
