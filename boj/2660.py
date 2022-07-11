import collections
import sys

N = int(input())
graph = [[sys.maxsize] * N for _ in range(N)]
while True:
    a, b = map(int, input().split())

    if a == b == -1:
        break

    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# 각 지점에서 bfs 진행하여 graph 갱신
for i in range(N):
    queue = collections.deque()
    queue.append((i, 0))

    graph[i][i] = 0

    while queue:
        pos, cost = queue.popleft()

        # 현재 노드에서 연결된 노드들을 확인한다.
        for j in range(N):
            # 자기 자신이거나 연결된 간선이 없다면
            if pos == j or graph[pos][j] == sys.maxsize:
                continue

            if cost + graph[pos][j] <= graph[i][j]:
                queue.append((j, cost + graph[pos][j]))
                graph[i][j] = cost + graph[pos][j]
                graph[j][i] = cost + graph[pos][j]

score, candidates = sys.maxsize, []
for i in range(N):
    if score > max(graph[i]):
        score = max(graph[i])
        candidates.clear()
        candidates.append(i + 1)
    elif score == max(graph[i]):
        candidates.append(i + 1)

print(score, len(candidates))
candidates.sort()
print(*candidates)
