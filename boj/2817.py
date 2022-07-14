import collections
import heapq
import string

X = int(input())  # 참여 인원
N = int(input())  # 후보

heap = []
staff_set = set()
for _ in range(N):
    line = input().split()
    staff, votes = line[0], int(line[1])

    # 득표율이 5% 미만
    if votes < (X * 0.05):
        continue

    for i in range(1, 15):
        score = votes // i
        heapq.heappush(heap, (-score, staff))
        staff_set.add(staff)

table = collections.defaultdict(int)
for _ in range(14):
    front = heapq.heappop(heap)
    staff = front[1]
    if staff in table:
        table[staff] += 1
    else:
        table[staff] = 1

for staff in list(string.ascii_uppercase):
    if staff not in staff_set:
        continue

    print(staff, table[staff])