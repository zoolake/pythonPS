T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    team_score = [[0] * (k + 1) for _ in range(n + 1)]
    submit_count = [0] * (n + 1)
    submit_time = [0] * (n + 1)

    for time in range(m):
        i, j, s = map(int, input().split())
        team_score[i][j] = max(team_score[i][j], s)
        submit_count[i] += 1
        submit_time[i] = time

    rank_board = []
    for i in range(1, n + 1):
        score = sum(team_score[i])
        count = submit_count[i]
        time = submit_time[i]
        team = i

        rank_board.append((score, count, time, i))

    sorted_rank_board = sorted(rank_board, key=lambda x: (-x[0], x[1], x[2]))

    for i in range(n):
        if sorted_rank_board[i][3] == t:
            print(i + 1)
            break
