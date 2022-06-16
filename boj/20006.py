p, m = map(int, input().split())

rooms = []
for _ in range(p):
    line = input().split()
    level, name = int(line[0]), line[1]
    for room in rooms:
        # 입장 가능한 방이 있다면 다 찰 때까지 대기 (제일 먼저 생성된 방으로)
        if room[0][0] - 10 <= level <= room[0][0] + 10 and len(room) < m:
            room.append((level, name))
            break
    # 매칭 가능한 방이 없다면 방 생성 (-10 ~ +10)
    else:
        room = [(level, name)]
        rooms.append(room)

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    for player in sorted(room, key=lambda x: x[1]):
        print(player[0], player[1])
