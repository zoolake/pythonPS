S = list(input())
n = len(S)

zero, one = 0, 0
for num in S:
    if num == '0':
        zero += 1
    else:
        one += 1

half_zero, half_one = zero // 2, one // 2

for i in range(n):
    if S[i] == '1' and one > half_one:
        S[i] = 'X'
        one -= 1

for i in range(n - 1, -1, -1):
    if S[i] == '0' and zero > half_zero:
        S[i] = 'X'
        zero -= 1

answer = ''.join(S)
print(answer.replace('X', ''))
