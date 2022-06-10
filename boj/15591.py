# 참고 : PyPy3로 제출
import collections
import sys

# 입력
N, Q = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())

    # base case: k==1
    if k == 1:
        print(N - 1)
        continue

    # BFS
    answer = 0
    queue = collections.deque()
    visited = [False] * (N + 1)

    queue.append((v, sys.maxsize))
    visited[v] = True

    while queue:
        cur_node, min_cost = queue.popleft()

        for next_node, next_cost in graph[cur_node]:
            if not visited[next_node]:
                cost = next_cost if next_cost < min_cost else min_cost
                queue.append((next_node, cost))
                visited[next_node] = True
                if cost >= k:
                    answer += 1

    print(answer)
