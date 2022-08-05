import collections

N = int(input())
records = [list(map(int, input().split())) for _ in range(N)]
country_medal = collections.defaultdict(int)

records.sort(key=lambda x: -x[2])

medal = 0
for country, student, score in records:
    if country_medal[country] < 2 and medal < 3:
        country_medal[country] += 1
        medal += 1
        print(country, student)
