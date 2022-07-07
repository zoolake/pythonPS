import heapq
import sys

input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    value, time = map(int, input().split())
    classes.append((time, value))

classes.sort(key=lambda x: x[0])

heap = []
heap_size = 0
answer = 0
for time, value in classes:
    # 문제의 데드라인이 힙의 현재 사이즈보다 크다면 일단 풀 수 있다.
    if heap_size < time:
        heapq.heappush(heap, value)
        heap_size += 1
        answer += value
    else:
        min_value = heap[0]
        # 힙의 최소값보다 큰 경우에만 문제를 풀 수 있다.
        if min_value < value:
            heapq.heappop(heap)
            answer -= min_value
            heapq.heappush(heap, value)
            answer += value

print(answer)
