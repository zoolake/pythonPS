def fn(x):
    total = 0
    for i in x:
        if i.isdigit():
            total += int(i)

    return total


N = int(input())
guitars = [input() for _ in range(N)]

guitars.sort(key=lambda x: (len(x), fn(x), x))

for guitar in guitars:
    print(guitar)