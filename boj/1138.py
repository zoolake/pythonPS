N = int(input())
people = list(map(int, input().split()))

visited = [0] * N
for h in range(1, N + 1):
    index = 0
    cnt = people[h - 1]
    while True:
        if visited[index] == 0:
            if cnt == 0:
                visited[index] = h
                break
            cnt -= 1
        index += 1

visited = list(map(str, visited))
print(' '.join(visited))
