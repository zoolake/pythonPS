import itertools
import sys


def solution(n, info):
    answer = [-1]

    # i번 과녁을 맞췄는지에 대한 정보가 들어가있다.
    score_list = itertools.combinations_with_replacement(range(11), n)
    max_diff = -sys.maxsize
    for score in score_list:
        temp = [0 for _ in range(11)]
        lion_total, apeach_total = 0, 0
        for index in list(score):
            temp[index] += 1

        for index in range(11):
            # 둘 다 못맞히는 경우
            if temp[index] == info[index] == 0:
                continue
            # 라이언이 더 많이 맞춘 경우
            if temp[index] > info[index]:
                lion_total += (10 - index)
            # 어피치가 더 많이 맞춘 경우
            else:
                apeach_total += (10 - index)

        # 라이언 이기는데
        if lion_total > apeach_total:
            diff = lion_total - apeach_total
            # 새롭게 더 큰 차이로 이기는 경우가 있다면
            if max_diff < diff:
                max_diff = diff
                answer = temp
            # 이기는 점수 차이가 동일한 경우 검사 필요
            elif max_diff == diff:
                # 작은 점수부터 검사한다
                for index in range(10, -1, -1):
                    # 같다면 다음 검사 진행
                    if temp[index] == answer[index]:
                        continue
                    # 기존 정답이 가장 낮은 점수를 더 많이 맞힌 경우라면 종료
                    elif temp[index] < answer[index]:
                        break
                    # 새로운 정답 후보가 가장 낮은 점수를 더 많이 맞힌 경우라면 답 갱신 후 종료
                    elif temp[index] > answer[index]:
                        answer = temp
                        break

    return answer
