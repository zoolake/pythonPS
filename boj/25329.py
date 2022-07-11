import collections
import sys


def calculate_time(time):
    hour, minute = time.split(':')
    return 60 * int(hour) + int(minute)


def calculate_fee(time):
    base_fee = 10
    # 기본 시간 이하로 통화한 경우
    if time <= 100:
        return base_fee

    time -= 100
    if time % 50 == 0:
        return base_fee + (time // 50) * 3
    else:
        return base_fee + ((time // 50) + 1) * 3


input = sys.stdin.readline

N = int(input())
table = collections.defaultdict(int)
for _ in range(N):
    time, name = input().split()
    table[name] += calculate_time(time)

bills = []
for name, time in table.items():
    bills.append((name, calculate_fee(time)))
bills.sort(key=lambda x: (-x[1], x[0]))

for bill in bills:
    print(*bill)
