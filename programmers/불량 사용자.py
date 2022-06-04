import itertools


def solution(user_id, banned_id):
    answer = 0

    comb = itertools.combinations(user_id, len(banned_id))
    for c in comb:
        list_c = list(c)

        # 하나라도 일치하는 케이스가 있는지 확인
        perm = itertools.permutations(list_c)
        for p in perm:
            list_p = list(p)
            for i in zip(list_p, banned_id):
                if not check(i[0], i[1]):
                    break
            else:
                answer += 1
                break

    return answer


def check(user_id, banned_id):
    # 길이가 다르다면 false
    if len(user_id) != len(banned_id):
        return False

    # 순회하면서 비교
    size = len(user_id)
    for i in range(size):
        if banned_id[i] == '*':
            continue

        if user_id[i] != banned_id[i]:
            return False

    return True
