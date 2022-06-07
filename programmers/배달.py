import collections


def solution(N, roads, K):
    answer = 0

    # 초기화
    max_num = 500001
    board = [[max_num] * (N + 1) for _ in range(N + 1)]

    for road in roads:
        start, end, cost = road
        board[start][end] = min(board[start][end], cost)
        board[end][start] = min(board[end][start], cost)

    visited = collections.defaultdict(lambda: max_num)
    visited[1] = 0
    queue = collections.deque()
    for end in range(2, N + 1):
        cost = board[1][end]
        if cost <= K and visited[end] > cost:
            queue.append([end, cost])
            visited[end] = cost

        bfs(queue, visited, board, N, K)

    for k, v in visited.items():
        if v < max_num:
            answer += 1

    return answer


def bfs(queue, visited, board, N, K):
    while queue:
        start, total_cost = queue.popleft()
        for end in range(1, N + 1):
            new_total_cost = board[start][end] + total_cost
            if visited[end] > new_total_cost and new_total_cost <= K:
                queue.append([end, new_total_cost])
                visited[end] = new_total_cost
