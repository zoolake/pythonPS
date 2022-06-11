import itertools

# 입력
N, K = map(int, input().split())
kits = list(map(int, input().split()))

# 모든 순열 생성
permutations = list(itertools.permutations(kits))

answer = 0
for case in permutations:
    weight = 500
    for kit in case:
        weight -= K
        weight += kit
        if weight < 500:
            break
    else:
        answer += 1

print(answer)
