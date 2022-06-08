global answer


def solution(n):
    global answer
    answer = 0
    visited = [0] * n
    dfs(visited, 0, n)
    return answer


def dfs(visited, row, n):
    # 종료 조건
    if row == n:
        global answer
        answer += 1
        return

    # 열 순회
    for col in range(n):
        visited[row] = col
        for r in range(row):
            # 위로 겹치는지
            if visited[r] == col:
                break
            # 대각선으로 겹치는지
            if abs(row - r) == abs(visited[r] - col):
                break
        else:
            dfs(visited, row + 1, n)
