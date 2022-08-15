N, score, P = map(int, input().split())
cur_score_list = []
if N > 0:
    cur_score_list = list(map(int, input().split()))

score_list = [-1] * P
score_list[:N] = cur_score_list[:N]

rank = 1
is_valid = False
for i in range(P):
    if score < score_list[i]:
        rank += 1
    elif score == score_list[i]:
        continue
    else:
        is_valid = True
        break

if is_valid:
    print(rank)
else:
    print(-1)
