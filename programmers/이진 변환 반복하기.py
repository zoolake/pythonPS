convert_count = 0
remove_zero_count = 0


def convert(s):
    global remove_zero_count
    # 모든 0을 제거
    zero_count = s.count('0')
    remove_zero_count += zero_count
    s = s.replace('0', '')
    # 길이를 2진법으로 표현한 문자열로 변경
    return bin(len(s))[2:]


def solution(s):
    global convert_count, remove_zero_count

    while True:
        if s == '1':
            break

        # 이진 변환
        s = convert(s)
        convert_count += 1

    return [convert_count, remove_zero_count]