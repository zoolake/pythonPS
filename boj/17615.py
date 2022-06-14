# 입력
import collections
import sys


def solution(N, ball_count, color):
    global answer
    window_list = [[index for index in range(0, ball_count)], [index for index in range(N - ball_count, N)]]

    for window in window_list:
        change_count = 0
        for ball_index, window_index in zip(dict[color], window):
            if ball_index != window_index:
                change_count += 1
        answer = min(answer, change_count)


N = int(input())
balls = input()

answer = sys.maxsize

dict = collections.defaultdict(list)
for index, ball in enumerate(balls):
    dict[ball].append(index)

red_count = len(dict['R'])
blue_count = N - red_count

# RED
solution(N, red_count, 'R')
# BLUE
solution(N, blue_count, 'B')

print(answer)
