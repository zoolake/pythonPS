import sys

input = sys.stdin.readline

N, M, T = map(int, input().split())

work_board = [list(map(int, input().split())) for _ in range(N)]
time_board = [list(map(int, input().split())) for _ in range(N)]

# dp[row][col][time]
dp = [[[-1] * (T + 1) for _ in range(M)] for _ in range(N)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(M):

        # 집
        if i == 0 and j == 0:
            continue

        for time in range(1, T + 1):
            # 상
            if i - 1 >= 0 and time - 1 >= 0:
                # 일을 안하는 경우
                dp[i][j][time] = max(dp[i][j][time], dp[i - 1][j][time - 1])
                # 일을 하는 경우
                ntime = time - 1 - time_board[i][j]
                if ntime >= 0 and dp[i - 1][j][ntime] != -1:
                    dp[i][j][time] = max(dp[i][j][time], dp[i - 1][j][ntime] + work_board[i][j])
            # 좌
            if j - 1 >= 0 and time - 1 >= 0:
                # 일을 안하는 경우
                dp[i][j][time] = max(dp[i][j][time], dp[i][j - 1][time - 1])
                # 일을 하는 경우
                ntime = time - 1 - time_board[i][j]
                if ntime >= 0 and dp[i][j - 1][ntime] != -1:
                    dp[i][j][time] = max(dp[i][j][time], dp[i][j - 1][ntime] + work_board[i][j])
            # 좌상
            if i - 1 >= 0 and j - 1 >= 0 and time - 1 >= 0:
                # 일을 안하는 경우
                dp[i][j][time] = max(dp[i][j][time], dp[i - 1][j - 1][time - 1])
                # 일을 하는 경우
                ntime = time - 1 - time_board[i][j]
                if ntime >= 0 and dp[i - 1][j - 1][ntime] != -1:
                    dp[i][j][time] = max(dp[i][j][time], dp[i - 1][j - 1][ntime] + work_board[i][j])

print(max(dp[N - 1][M - 1]))
