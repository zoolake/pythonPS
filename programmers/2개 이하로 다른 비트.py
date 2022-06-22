def solution(numbers):
    answer = []

    for number in numbers:
        binary_number = bin(number)[2:]
        n = len(binary_number)
        for i in range(n - 1, -1, -1):
            if i == n - 1 and binary_number[i] == '0':
                answer.append(int('0b' + binary_number[:n - 1] + '1', 2))
                break
            if binary_number[i] == '0' and binary_number[i + 1] == '1':
                answer.append(int('0b' + binary_number[:i] + '10' + binary_number[i + 2:], 2))
                break
        else:
            answer.append(int('0b' + '10' + binary_number[1:], 2))

    return answer
