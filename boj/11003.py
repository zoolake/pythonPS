# 모노톤 큐 : https://www.youtube.com/watch?v=DfljaUwZsOk&ab_channel=NeetCode

import collections

N, L = map(int, input().split())
nums = list(map(int, input().split()))

answer = []
deque = collections.deque()
for index in range(N):
    if not deque:
        deque.append(index)
    else:
        while deque and deque[0] <= index - L:
            deque.popleft()
        while deque and nums[deque[-1]] > nums[index]:
            deque.pop()
        deque.append(index)
    answer.append(nums[deque[0]])

for i in answer:
    print(i, end=' ')
