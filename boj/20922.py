import collections

N, K = map(int, input().split())
seq = list(map(int, input().split()))

table = collections.defaultdict(int)
left, right = 0, 0
max_length = 1

while right < N:
    if table[seq[right]] < K:
        table[seq[right]] += 1
        right += 1
    else:
        table[seq[left]] -= 1
        left += 1

    max_length = max(max_length, right - left)

print(max_length)
