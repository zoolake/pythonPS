import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())

stones = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(stones, (weight, value))

bags = [int(input()) for _ in range(K)]
bags.sort()

# 각 가방보다 가벼운 보석들 중 가장 가치가 큰 값을 넣는다.
answer = 0
heap = []
for bag in bags:
    # 가방 무게 >= 보석 무게
    while stones and bag >= stones[0][0]:
        weight, value = heapq.heappop(stones)
        heapq.heappush(heap, (-value, value))

    # heap에 있는 값 중 가장 가치가 큰 값을 answer에 더한다.
    if heap:
        answer += heapq.heappop(heap)[1]

print(answer)
