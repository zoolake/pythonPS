# 참고: https://blog.encrypted.gg/1029

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


n = 0
tree = [Node(None, None) for _ in range(17)]
visited = [False] * (1 << 17)
data = []
answer = 0


def dfs(state):
    global answer

    # 방문한적이 있는 상태인 경우
    if visited[state]:
        return
    visited[state] = True
    # 현 상태의 양과 늑대의 수를 검사
    wolf = 0
    sheep = 0
    for i in range(n):
        if state & (1 << i):
            # 양
            if data[i] == 0:
                sheep += 1
            # 늑대
            else:
                wolf += 1
    # 양이 다 잡아 먹히는 경우
    if sheep <= wolf:
        return
    # 갱신
    answer = max(answer, sheep)
    # 다음 상태 진행
    for i in range(n):
        if not (state & (1 << i)):
            continue
        if tree[i].left is not None:
            dfs(state | (1 << tree[i].left))
        if tree[i].right is not None:
            dfs(state | (1 << tree[i].right))


def solution(info, edges):
    global n, tree, data, answer

    # 트리 초기화
    n = len(info)
    for edge in edges:
        parent, child = edge
        if tree[parent].left is None:
            tree[parent].left = child
        else:
            tree[parent].right = child

    data = info[:]
    dfs(1)

    return answer
