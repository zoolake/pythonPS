# 입력
N, X = map(int, input().rstrip().split())
visit_list = list(map(int, input().rstrip().split()))

window = visit_list[0:0 + X]
max_visit = sum(window)
visit = sum(window)
count = 1
for i in range(1, N - X + 1):
    visit -= visit_list[i - 1]
    visit += visit_list[i + X - 1]

    # 최대 방문자 수 갱신
    if visit > max_visit:
        max_visit = visit
        count = 1
    # 최대 방문자 수가 동일하다면 count+1
    elif visit != 0 and visit == max_visit:
        count += 1

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(count)
