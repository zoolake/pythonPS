import collections
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    students = list(map(int, input().split()))

    cycle = [False] * n
    impossible = [False] * n
    visited = [False] * n

    for i in range(n):
        # 이미 사이클에 속한 경우
        if cycle[i] or impossible[i] or visited[i]:
            continue

        queue = collections.deque()
        path = []

        queue.append(i)
        visited[i] = True
        path.append(i)

        is_cycle = False
        is_impossible = False
        while queue:
            node = queue.popleft()
            next_node = students[node] - 1

            if visited[next_node] and path[0] == next_node:
                if not cycle[next_node]:
                    for p in path:
                        cycle[p] = True
                break

            if impossible[next_node] or cycle[next_node]:
                for p in path:
                    impossible[p] = True
                break

            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                path.append(next_node)
            else:
                flag = True
                for p in path:
                    if p == next_node:
                        flag = False

                    if flag:
                        impossible[p] = True
                    else:
                        cycle[p] = True

    result = cycle.count(False)
    print(result)
