from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    # (유저-신고대상목록) 딕셔너리 생성
    dict = defaultdict(set)
    counter = defaultdict(int)
    for elem in report:
        user_report, user_reported = elem.split()
        if user_reported not in dict[user_report]:
            counter[user_reported] += 1
            dict[user_report].add(user_reported)

    for id in id_list:
        count = 0
        for user in dict[id]:
            if counter[user] >= k:
                count += 1
        answer.append(count)

    return answer