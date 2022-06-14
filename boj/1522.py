import sys

answer = sys.maxsize

word = input()
n = len(word)

a_count = word.count('a')
b_count = n - a_count

for i in range(n):
    # 순환하는 구조가 아닌 경우
    if i + b_count <= n:
        window = word[i:i + b_count]
    else:
        window = word[i:n] + word[0:i + b_count - n]
    window_a_count = window.count('a')
    answer = min(answer, window_a_count)

print(answer)
