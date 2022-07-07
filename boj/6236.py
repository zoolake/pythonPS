# input
import sys


def simulation(K, money_list):
    withdraw = 0
    current_money = 0

    for money in money_list:
        # 인출이 필요한 경우
        if current_money < money:
            withdraw += 1
            current_money = K
        current_money -= money

    return withdraw


input = sys.stdin.readline
N, M = map(int, input().split())
money_list = [int(input()) for _ in range(N)]

# 이분 탐색을 통한 K원 설정
left, right = max(money_list), N * 10000
K = sys.maxsize
while left <= right:
    mid = (left + right) // 2
    if simulation(mid, money_list) > M:
        left = mid + 1
    else:
        right = mid - 1
        K = min(K, mid)

print(int(K))
