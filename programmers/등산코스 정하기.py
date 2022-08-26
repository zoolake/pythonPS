# 모든 시작점에서 BFS 탐색 진행
# 현재 노드에서 갈 수 있는 노드의 개수가 여러 개 라면
# 비용이 가장 작은 노드 먼저 방문 "우선순위 큐"
# 방문처리 필요 / 산봉오리 검증 필요 / 중간에 다른 시작점 방문하지 않게 끔
import collections
import heapq
import sys


def solution(n, paths, gates, summits):
    min_node = sys.maxsize
    min_intensity = sys.maxsize

    gates_set = set(gates)
    summits_set = set(summits)

    # init graph
    graph = collections.defaultdict(list)
    for a, b, cost in paths:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    # bfs [시작노드, 현재노드, intensity]
    for gate in gates:
        heap = []
        visited = [sys.maxsize] * (n + 1)

        heapq.heappush(heap, (0, (gate, gate, 0)))
        visited[gate] = 0

        while heap:
            start, current, intensity = heapq.heappop(heap)[1]

            if current in summits_set:
                if intensity < min_intensity:
                    min_node = current
                    min_intensity = intensity
                elif intensity == min_intensity:
                    min_node = min(min_node, current)
                break

            for next_node, cost in graph[current]:
                if visited[next_node] > cost and next_node not in gates_set:
                    heapq.heappush(heap, (cost, (start, next_node, max(intensity, cost))))
                    visited[next_node] = min(visited[next_node], cost)

    answer = [min_node, min_intensity]
    return answer
