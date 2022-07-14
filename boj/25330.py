def solution(current_hp, damage, save, visited):
    global N, monsters, people, answer

    for i in range(N):
        # 방문한 곳
        if visited[i]:
            continue

        after_hp = current_hp - (damage + monsters[i])
        # 방문하지 않았고, 몬스터를 잡을 수 있다면
        if after_hp >= 0:
            visited[i] = True
            solution(after_hp, damage + monsters[i], save + people[i], visited)
            visited[i] = False

    # 더 이상 방문할 곳이 없다면
    answer = max(answer, save)
    return


N, K = map(int, input().split())
monsters = list(map(int, input().split()))
people = list(map(int, input().split()))

answer = 0
solution(K, 0, 0, [False] * N)
print(answer)
