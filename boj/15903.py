import heapq

# input
N, M = map(int, input().split())
heap = list(map(int, input().split()))
# heapify
heapq.heapify(heap)
# solution
for _ in range(M):
    # 가장 작은 2개를 뺀다.
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    # 값을 갈아 끼우고 다시 삽입
    sum_result = x + y
    heapq.heappush(heap, sum_result)
    heapq.heappush(heap, sum_result)

print(sum(heap))
