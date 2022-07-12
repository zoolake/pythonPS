import collections
import sys


def solution(current, end, total, visited):
    global nodes, graph, BIG_NUMBER

    if current == end:
        print(int(total) % BIG_NUMBER)
        return True

    # 현재 노드와 이어진 노드를 순회
    for next_node in graph[current]:
        # 이미 방문했다면 continue
        if visited[next_node]:
            continue

        visited[next_node] = True
        if solution(next_node, end, total + str(nodes[next_node]), visited):
            return True
        else:
            visited[next_node] = False

    return False


BIG_NUMBER = 1000000007
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, Q = map(int, input().split())
nodes = list(map(int, input().split()))
graph = collections.defaultdict(list)
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)
for _ in range(Q):
    start, end = map(lambda x: int(x) - 1, input().split())
    if start == end:
        print(nodes[start])
    else:
        visited = [False] * N
        visited[start] = True
        solution(start, end, str(nodes[start]), visited)
