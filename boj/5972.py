# 1 <= N,M <= 50,000
import collections
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().rstrip().split())

# graph 초기화
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 다익스트라
distance_table = [INF] * (N + 1)
priority_queue = []

heapq.heappush(priority_queue, (1, 0))
distance_table[1] = 0

while priority_queue:
    node, cost = heapq.heappop(priority_queue)

    if node == N:
        break

    if distance_table[node] < cost:
        continue

    for next_node, next_cost in graph[node]:
        next_total_cost = cost + next_cost
        if next_total_cost < distance_table[next_node]:
            heapq.heappush(priority_queue, (next_node, next_total_cost))
            distance_table[next_node] = next_total_cost

print(distance_table[N])
