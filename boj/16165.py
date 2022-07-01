import collections

N, M = map(int, input().split())

team_table = collections.defaultdict(list)
for _ in range(N):
    team_name = input()
    member_count = int(input())
    for _ in range(member_count):
        team_table[team_name].append(input())

for _ in range(M):
    name = input()
    quiz_type = int(input())
    # 해당 팀 멤버 사전순 출력
    if quiz_type == 0:
        team = team_table[name]
        for member in sorted(team):
            print(member)
    # 해당 멤버가 속한 팀 이름 출력
    else:
        for team_name, team in team_table.items():
            if name in team:
                print(team_name)
                break
