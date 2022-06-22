# 같은 구성 (같은 문자들 + 같은 개수)
# 비슷한 구성 (한 단어에서 한 문자를 더하거나 / 빼거나 / 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우)

# input
import string


def make_dict(word):
    word_dict = {}
    for alphabet in string.ascii_uppercase:
        word_dict[alphabet] = 0
    for alphabet in word:
        word_dict[alphabet] += 1

    return word_dict


def check(first_word_dict, word_dict, chance):
    for alphabet in string.ascii_uppercase:
        diff = abs(first_word_dict[alphabet] - word_dict[alphabet])
        if diff == 0:
            continue

        if diff == 1 and chance >= 1:
            chance -= 1
        else:
            return False

    # 유사한 경우
    return True


N = int(input())
first_word = input().rstrip()
first_word_dict = make_dict(first_word)

answer = 0
for _ in range(N - 1):
    word = input().rstrip()
    word_dict = make_dict(word)

    # 길이 차이가 2이상 난다면 볼 필요도 없음
    length_diff = abs(len(word) - len(first_word))
    if length_diff >= 2:
        continue

    # 길이가 같은 경우
    if length_diff == 0:
        change_chance = 2
        if check(first_word_dict, word_dict, change_chance):
            answer += 1

    # 길이가 1차이
    if length_diff == 1:
        change_chance = 1
        if check(first_word_dict, word_dict, change_chance):
            answer += 1

print(answer)
