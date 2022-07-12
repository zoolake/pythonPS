import collections
import sys


def solution(total, orders, visited, potions, discount_table):
    global answer

    if total > answer:
        return

    if len(orders) == len(potions):
        answer = min(answer, total)
        return

    for i in range(len(potions)):
        if visited[i]:
            continue

        # i 번째 물약을 구매 후 탐색 진행
        total += copy_potions[i]
        visited[i] = True
        orders.append(i)
        # 할인 적용
        before_discount = []
        for potion, discount in discount_table[i]:
            after_discount = copy_potions[potion] - discount
            before_discount.append((potion, copy_potions[potion]))
            if after_discount > 0:
                copy_potions[potion] = after_discount
            else:
                copy_potions[potion] = 1
        # 재귀
        solution(total, orders, visited, potions, discount_table)
        # 할인 취소
        for potion, price in before_discount:
            copy_potions[potion] = price
        orders.pop()
        visited[i] = False
        total -= copy_potions[i]


N = int(input())
potions = list(map(int, input().split()))
discount_table = collections.defaultdict(list)

for i in range(N):
    loop = int(input())
    for _ in range(loop):
        potion, discount = map(int, input().split())
        discount_table[i].append((potion - 1, discount))

answer = sys.maxsize

total = 0
copy_potions = potions[:]
visited = [False] * N
orders = []

solution(total, orders, visited, copy_potions, discount_table)

print(answer)
