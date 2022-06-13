import sys

# 입력
N, M = map(int, input().split())

s = set()
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    s.add(word)

# solution
for _ in range(M):
    words = sys.stdin.readline().rstrip().split(',')
    for word in words:
        if word in s:
            s.remove(word)

    print(len(s))
