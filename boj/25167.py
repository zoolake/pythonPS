def calculate(time):
    hour, minute = time.split(':')
    return 60 * int(hour) + int(minute)


N, M, P = map(int, input().split())

table = {}  # <이름:문제 별 상태>
names = input().split()
for name in names:
    table[name] = [None] * (N + 1)

# (제출 시간, 상태, 점수)
# 상태 { None:미제출 / 1:실패 / 2:성공 / 3:부정행위 }
for _ in range(P):
    no, time, name, state = input().split()
    no, time = int(no), calculate(time)

    # 문제를 푼 경우
    if state == 'solve':
        # 한 번에 문제를 푼 경우
        if table[name][no] is None:
            table[name][no] = [time, 3, M + 1]
        # 틀렸던 문제를 푼 경우
        elif table[name][no][1] == 1:
            time_diff = time - table[name][no][0]
            table[name][no] = [time_diff, 2, 0]
    # 문제를 틀린 경우
    if state == 'wrong' and table[name][no] is None:
        table[name][no] = [time, 1, 0]

# 각 문제별 순회하면서 점수 계산
for no in range(1, N + 1):
    solvers = []
    for name, problems in table.items():
        # 문제를 시도 한 적이 없는 경우
        if problems[no] is None:
            problems[no] = [0, 0, M + 1]
            continue
        # 문제를 푼 경우
        if problems[no][1] == 2:
            solvers.append((name, problems[no][0]))
        # 문제를 시도했지만 못 푼 경우
        elif problems[no][1] == 1:
            problems[no][2] = M

    # solvers 정렬 (time_diff 오름차순)
    solvers.sort(key=lambda x: (x[1], x[0]))
    for i in range(len(solvers)):
        name = solvers[i][0]
        table[name][no] = [0, 0, i + 1]

# 전체 점수 계산
answer = []
for name, problems in table.items():
    total = 0
    for problem in problems:
        if problem is not None:
            total += problem[2]
    answer.append((name, total))

answer.sort(key=lambda x: (x[1], x[0]))
for name, score in answer:
    print(name)
