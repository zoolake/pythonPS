# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.

import collections
import sys


def solution(W, K):
    n = len(W)
    # 순회를 하면서 인덱스 저장
    dict = collections.defaultdict(list)
    for index in range(n):
        alphabet = W[index]
        dict[alphabet].append(index)

    min_length = sys.maxsize
    max_length = -sys.maxsize
    for alphabet, index_list in dict.items():
        # K개 이상인 경우 검사 진행
        index_list_length = len(index_list)
        if index_list_length >= K:
            # 슬라이딩 윈도우 진행 (윈도우 크기는 K)
            for i in range(index_list_length):
                if i + K > index_list_length:
                    break
                window = index_list[i:i + K]
                min_length = min(min_length, window[-1] - window[0] + 1)
                max_length = max(max_length, window[-1] - window[0] + 1)

    if min_length == sys.maxsize and max_length == -sys.maxsize:
        print(-1)
    else:
        print(min_length, max_length)


T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    if K == 1:
        print(1, 1)
    else:
        solution(W, K)
