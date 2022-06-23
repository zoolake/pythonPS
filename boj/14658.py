# input
N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]

answer = 0

for i in range(K):
    for j in range(K):
        r = stars[i][0]
        c = stars[j][1]

        count = 0
        for k in range(K):
            row, col = stars[k]
            if r <= row <= r + L and c <= col <= c + L:
                count += 1

        answer = max(answer, count)

print(K - answer)
