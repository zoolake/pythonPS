import collections

# 입력
N = int(input())
M = int(input())

graph = collections.defaultdict(list)
for start in range(1, N + 1):
    end_list = list(map(int, input().split()))
    for end in range(len(end_list)):
        if end_list[end] == 1:
            graph[start].append(end + 1)

plan = list(map(int, input().split()))

queue = collections.deque()
visited = [False] * (N + 1)

queue.append(plan[0])
visited[plan[0]] = True

while queue:
    current_node = queue.popleft()
    for next_node in graph[current_node]:
        if not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True

for node in plan:
    if not visited[node]:
        print('NO')
        break

else:
    print('YES')
