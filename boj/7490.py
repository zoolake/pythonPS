def solution(count, seq, N, formula, answer):
    op = ['+', '-', ' ']

    if count == N - 1:
        if eval(formula.replace(' ', '')) == 0:
            answer.append(formula)
        return

    for i in range(3):
        next_formula = formula + op[i] + str(seq[count + 1])
        solution(count + 1, seq, N, next_formula, answer)


T = int(input())

for _ in range(T):
    N = int(input())
    seq = [i for i in range(1, N + 1)]

    answer = []
    solution(0, seq, N, '1', answer)
    for data in sorted(answer):
        print(data)
    print()
