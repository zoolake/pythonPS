BIG_NUMBER = 1e9 + 7

N = int(input())
word = input()

W, WH, WHE, WHEE = 0, 0, 0, 0
for char in word:
    if char == 'W':
        W += 1
    elif char == 'H':
        WH += W
    elif char == 'E':
        # 기존에 WHEE를 만들 수 있는 경우의 수가 있다면 2배가 되며,
        # 현재까지 WHE를 만들 수 있는 경우의 수를 더해준다.
        WHEE = (WHEE * 2 + WHE) % BIG_NUMBER
        WHE += WH

print(int(WHEE % BIG_NUMBER))
