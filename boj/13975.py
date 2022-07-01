import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    heap = []
    for file in files:
        heapq.heappush(heap, file)

    answer = 0
    while len(heap) > 1:
        file_a = heapq.heappop(heap)
        file_b = heapq.heappop(heap)
        total = file_a + file_b
        answer += total
        heapq.heappush(heap, total)

    print(answer)
