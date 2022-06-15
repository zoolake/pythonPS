def solution(S, T):
    if not T:
        return

    if S == T:
        print(1)
        exit(0)

    # 첫 글자가 B
    if T[0] == 'B':
        copy = T[::-1]
        solution(S, copy[:-1])
    # 마지막 글자가 A
    if T[-1] == 'A':
        copy = T[:]
        solution(S, copy[:-1])


# 입력
S = input()
T = input()

solution(S, T)
print(0)
