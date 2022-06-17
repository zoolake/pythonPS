# 입력
N, K = map(int, input().split())
data = input()

answer = 0
visited = [False] * N
for i in range(N):
    # 사람이라면
    if data[i] == 'P':
        # 현재 인덱스-K ~ 현재 인덱스+K 탐색
        left = i - K if i - K >= 0 else 0
        right = i + K if i + K < N else N - 1
        for j in range(left, right + 1):
            # 햄버거라면 먹는다.
            if data[j] == 'H' and not visited[j]:
                visited[j] = True
                answer += 1
                break

print(answer)
