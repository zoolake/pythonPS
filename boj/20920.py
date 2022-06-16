import collections
import heapq
import sys


class info:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        # 빈도가 높을수록 앞
        if self.count > other.count:
            return True
        # 길이가 길수록 앞
        elif self.count == other.count:
            if len(self.word) > len(other.word):
                return len(self.word) > len(other.word)
            # 사전순
            elif len(self.word) == len(other.word):
                return self.word < other.word

        return False


N, M = map(int, sys.stdin.readline().rstrip().split())

priority_queue = []
dict = collections.defaultdict(int)
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        dict[word] += 1

for word, count in dict.items():
    heapq.heappush(priority_queue, info(word, count))

while priority_queue:
    front = heapq.heappop(priority_queue)
    print(front.word)
