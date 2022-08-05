import collections

N = int(input())
nums = [num for num in range(1, N + 1)]

answer = []
deque = collections.deque(nums)
while True:
    front = deque.popleft()
    answer.append(front)

    if not deque:
        break

    front = deque.popleft()
    deque.append(front)

print(*answer)
