import sys
import heapq


class P1:
    def __init__(self, problem, level):
        self.problem = problem
        self.level = level

    def __lt__(self, other):
        if self.level > other.level:
            return True
        elif self.level == other.level:
            return self.problem > other.problem
        else:
            return False


class P2:
    def __init__(self, problem, level):
        self.problem = problem
        self.level = level

    def __lt__(self, other):
        if self.level < other.level:
            return True
        elif self.level == other.level:
            return self.problem < other.problem
        else:
            return False


# input
input = sys.stdin.readline

N = int(input())
max_heap = []
min_heap = []
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(max_heap, P1(P, L))
    heapq.heappush(min_heap, P2(P, L))

solved = [False] * 100001
M = int(input())
for _ in range(M):
    line = input().split()
    if line[0] == 'recommend':
        if line[1] == '1':
            while solved[max_heap[0].problem]:
                P = heapq.heappop(max_heap)
                solved[P.problem] = False
            print(max_heap[0].problem)
        elif line[1] == '-1':
            while solved[min_heap[0].problem]:
                P = heapq.heappop(min_heap)
                solved[P.problem] = False
            print(min_heap[0].problem)
    elif line[0] == 'add':
        P, L = map(int, line[1:])
        heapq.heappush(max_heap, P1(P, L))
        heapq.heappush(min_heap, P2(P, L))
    elif line[0] == 'solved':
        P = int(line[1])
        solved[P] = True
