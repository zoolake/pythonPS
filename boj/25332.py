N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 누적합
sum_A, sum_B = [0] * N, [0] * N
sum_A[0], sum_B[0] = A[0], B[0]
for i in range(1, N):
    sum_A[i] = A[i] + sum_A[i - 1]
    sum_B[i] = B[i] + sum_B[i - 1]

# sum_a[0,j] - sum_b[0,j] == sum_a[0,i] - sum_b[0,i]
table = {0: 1}
answer = 0
for i in range(N):
    if sum_A[i] - sum_B[i] in table:
        answer += table[sum_A[i] - sum_B[i]]
        table[sum_A[i] - sum_B[i]] += 1
    else:
        table[sum_A[i] - sum_B[i]] = 1

print(answer)
