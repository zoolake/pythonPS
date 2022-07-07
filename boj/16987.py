def simulation(cur, eggs):
    global answer
    # 현재 들고 있는 계란이 맨 오른쪽
    if cur >= len(eggs):
        count = 0
        for egg in eggs:
            if egg[0] <= 0:
                count += 1
        answer = max(answer, count)
        return

    # 현재 들고 있는 계란이 부서진 경우
    if eggs[cur][0] <= 0:
        simulation(cur + 1, eggs)
        return

    for i in range(len(eggs)):
        # 현재 들고 있는 계란이거나 치려는 계란이 이미 깨진 경우
        if cur == i or eggs[i][0] <= 0:
            continue

        cur_durability, cur_weight = eggs[cur]
        next_durability, next_weight = eggs[i]

        # 손에 들고 있는 계란으로 다른 계란을 친다.
        eggs[cur][0] -= next_weight
        eggs[i][0] -= cur_weight
        # 가장 최근에 든 계란의 한 칸 오른쪽 계란을 들고 다시 진행한다.
        simulation(cur + 1, eggs)
        # 원상 복구
        eggs[cur][0] += next_weight
        eggs[i][0] += cur_weight

    if cur == len(eggs) - 1:
        count = 0
        for egg in eggs:
            if egg[0] <= 0:
                count += 1
        answer = max(answer, count)
        return

    return


# input
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
answer = 0
simulation(0, eggs)
print(answer)
