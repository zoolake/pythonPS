# 참고: https://prgms.tistory.com/101 (결정문제 증명 관련)

# 최악의 경우: 왕복 (10^5 * 2) * 금+은(10^9 * 2) = 4*1e14
def solution(a, b, g, s, w, t):
    n = len(g)  # 도시의 수

    left = 1
    right = 4 * 1e14
    while left <= right:
        mid = (right - left) // 2 + left

        # 각 도시별 검사
        total, total_gold, total_silver = 0, 0, 0
        for i in range(n):
            gold, silver, weight, time = g[i], s[i], w[i], t[i]
            # mid 시간을 기준으로 몇번 왕복 가능한지
            count = mid // (2 * time)
            # 만약에 편도로 한번 더 가능하면 추가
            if (mid % (2 * time)) >= time:
                count += 1
            total_gold += gold if gold < count * weight else count * weight
            total_silver += silver if silver < count * weight else count * weight
            total += (gold + silver) if (gold + silver) < count * weight else count * weight

        if total >= a + b and total_gold >= a and total_silver >= b:
            right = mid - 1
        else:
            left = mid + 1

    return int(left)
