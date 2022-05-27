def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:
        answer.append(word.capitalize())

    return ' '.join(answer)