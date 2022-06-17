def solution():
    N = int(input())
    price = list(map(int, input().split()))
    answer = 0

    max_price = price[-1]
    for i in range(N - 2, -1, -1):
        # max_price 갱신
        if max_price < price[i]:
            max_price = price[i]
        # 차액 계산
        else:
            diff = 0 if max_price - price[i] <= 0 else max_price - price[i]
            answer += diff

    return answer


# 입력
T = int(input())
for _ in range(T):
    print(solution())
