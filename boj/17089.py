# 참고: https://www.acmicpc.net/board/view/67659
# 시간복잡도: O(N^2 + M*N)
import sys
import collections

input = sys.stdin.readline
N, M = map(int, input().split())


graph = [[False] * N for _ in range(N)]
table = collections.defaultdict(int)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = True
    graph[b][a] = True
    table[a] += 1
    table[b] += 1

answer = sys.maxsize
for i in range(N):
    for j in range(i + 1, N):
        # i와 j가 친구라면
        if graph[i][j]:
            for k in range(j + 1, N):
                # i와 k가 친구이고 j와 k가 친구라면
                if graph[i][k] and graph[j][k]:
                    answer = min(answer, table[i] + table[j] + table[k] - 6)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
