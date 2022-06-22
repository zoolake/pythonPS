# input
import collections
import sys

T = int(input())

for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    teams_counter = collections.Counter(teams)
    teams_records = collections.defaultdict(list)

    score = 1
    for i in range(N):
        team = teams[i]
        # 팀 자격 미달
        if teams_counter[team] < 6:
            continue

        teams_records[team].append(score)
        score += 1

    min_score = sys.maxsize
    winner = 1
    for team, score_list in teams_records.items():
        total_score = sum(score_list[:4])
        if total_score < min_score:
            min_score = total_score
            winner = team
        elif total_score == min_score:
            # 5번째 선수 비교
            if teams_records[winner][4] > score_list[4]:
                winner = team

    print(winner)
