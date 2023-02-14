def solution(babbling_list):
    answer = 0

    possible_list = ['aya', 'ye', 'woo', 'ma']
    impossible_list = ['ayaaya', 'yeye', 'woowoo', 'mama']
    for babbling in babbling_list:
        flag = True

        # 연속 발음 검사
        for impossible in impossible_list:
            if impossible in babbling:
                flag = False
                break

        # 연속 발음 검사를 통과한 경우
        if flag:
            temp = babbling
            for possible in possible_list:
                # case: ywooe
                # y'woo'e
                # 'ye'
                # ''
                temp = temp.replace(possible, ' ')

            # 공백을 다 제거하면
            temp = temp.replace(' ', '')
            if not temp:
                answer += 1

    return answer