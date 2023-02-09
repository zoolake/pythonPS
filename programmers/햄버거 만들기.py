def make_burger(stack):
    for _ in range(4):
        stack.pop()


def solution(ingredients):
    answer = 0

    stack = []
    for ingredient in ingredients:
        # 재료를 스택에 넣어준다.
        stack.append(ingredient)

        # 빵-야채-고기-빵 검사
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            make_burger(stack)
            answer += 1

    return answer
