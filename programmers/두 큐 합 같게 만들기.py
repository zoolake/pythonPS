from collections import deque


def solution(queue1, queue2):
    dq1, dq2 = deque(queue1), deque(queue2)
    total_dq1, total_dq2 = sum(dq1), sum(dq2)

    total = total_dq1 + total_dq2

    if total % 2 == 1:
        return -1

    loop, max_loop = 0, 2 * (len(dq1) + len(dq2))
    while loop < max_loop:
        if total_dq1 == total_dq2:
            return loop

        if total_dq1 < total_dq2:
            front = dq2.popleft()
            dq1.append(front)
            total_dq1 += front
            total_dq2 -= front
        else:
            front = dq1.popleft()
            dq2.append(front)
            total_dq2 += front
            total_dq1 -= front

        loop += 1

    return -1
