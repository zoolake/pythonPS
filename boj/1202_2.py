import sys
import heapq


class Stone:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __lt__(self, other):
        if self.weight > other.weight:
            return True
        elif self.weight == other.weight:
            return self.value > other.value
        else:
            return False


input = sys.stdin.readline
N, K = map(int, input().split())

stones = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(stones, Stone(weight, value))

bags = []
for _ in range(K):
    bag = int(input())
    heapq.heappush(bags, (-bag, bag))

answer = []
while stones:
    stone = heapq.heappop(stones)
    # 가방에 보석을 담을 수 있다면
    if bags and bags[0][1] >= stone.weight:
        if len(answer) >= K:
            heapq.heappop(answer)
        heapq.heappush(answer, stone.value)
        heapq.heappop(bags)
    # 가방에 보석을 담을 수 없다면
    else:
        # answer에 있는 가장 작은 가치보다 새로 들어오려는 보석의 가치가 더 크다면 교환해준다.
        if answer and answer[0] < stone.value:
            heapq.heappop(answer)
            heapq.heappush(answer, stone.value)

print(sum(answer))
