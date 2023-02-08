def solution(s, skip, index):
    answer = ''

    for alphabet in s:
        count = index
        current_alphabet_code = ord(alphabet) - 97  # 0 ~ 25

        while count > 0:
            # 알파벳 이동
            current_alphabet_code = (current_alphabet_code + 1) % 26
            # skip 반영
            if chr(current_alphabet_code + 97) not in skip:
                count -= 1

        answer += chr(current_alphabet_code + 97)

    return answer
