import string


def solution(msg):
    answer = []
    # 길이가 1인 사전 초기화
    dict = list(string.ascii_uppercase)

    left, right = 0, 1
    index = 0
    while left < len(msg) and right <= len(msg):
        w = msg[left:right]

        # 단어가 있다면
        if get_index(w, dict) >= 0:
            index = get_index(w, dict)
            right += 1
            # 마지막이라면
            if right == len(msg) + 1:
                answer.append(index + 1)
                break
        # 단어가 없다면
        else:
            answer.append(index + 1)
            dict.append(w)
            left = right - 1
            right = left + 1

    return answer


def get_index(word, dict):
    for i, w in enumerate(dict):
        if word == w:
            return i
    return -1
